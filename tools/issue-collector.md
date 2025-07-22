# Issue Collection Tools and Scripts

## Overview
This document provides tools, scripts, and methodologies for collecting and processing GitHub issues data from the Azure/azure-dev repository.

## Data Collection Strategy

### GitHub API Approach
The most efficient way to collect comprehensive issue data is through the GitHub REST API, which provides:
- Complete issue metadata
- Reaction counts and types
- Comment counts and content
- Label and milestone information
- Timeline data
- Cross-reference information

### Manual Collection Methods
For smaller-scale analysis or when API limits are a concern:
- GitHub search interface with saved queries
- GitHub CLI (`gh`) commands
- Browser automation tools
- CSV export from GitHub Projects

## GitHub API Collection Script

### Prerequisites
```bash
# Install required tools
npm install -g @octokit/rest
pip install requests pandas

# Set up authentication
export GITHUB_TOKEN="your_personal_access_token"
```

### Basic Issue Collection (Node.js)
```javascript
const { Octokit } = require("@octokit/rest");

const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN,
});

async function collectAllIssues() {
  const issues = [];
  let page = 1;
  
  while (true) {
    const response = await octokit.rest.issues.listForRepo({
      owner: "Azure",
      repo: "azure-dev",
      state: "all", // Get both open and closed
      per_page: 100,
      page: page,
      sort: "created",
      direction: "desc"
    });
    
    if (response.data.length === 0) break;
    
    issues.push(...response.data);
    page++;
  }
  
  return issues;
}

async function enrichIssueData(issue) {
  // Get reactions for each issue
  const reactions = await octokit.rest.reactions.listForIssue({
    owner: "Azure",
    repo: "azure-dev",
    issue_number: issue.number
  });
  
  // Get comments for each issue
  const comments = await octokit.rest.issues.listComments({
    owner: "Azure",
    repo: "azure-dev",
    issue_number: issue.number
  });
  
  return {
    ...issue,
    reaction_details: reactions.data,
    comment_details: comments.data
  };
}
```

### Python Collection Script
```python
import requests
import pandas as pd
import time
import os

class GitHubIssueCollector:
    def __init__(self):
        self.token = os.environ.get('GITHUB_TOKEN')
        self.headers = {'Authorization': f'token {self.token}'}
        self.base_url = 'https://api.github.com'
        
    def get_all_issues(self, owner='Azure', repo='azure-dev'):
        issues = []
        page = 1
        
        while True:
            url = f'{self.base_url}/repos/{owner}/{repo}/issues'
            params = {
                'state': 'all',
                'per_page': 100,
                'page': page,
                'sort': 'created',
                'direction': 'desc'
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            data = response.json()
            
            if not data:
                break
                
            issues.extend(data)
            page += 1
            
            # Rate limiting
            time.sleep(0.1)
            
        return issues
    
    def process_issues_to_dataframe(self, issues):
        processed = []
        
        for issue in issues:
            processed.append({
                'number': issue['number'],
                'title': issue['title'],
                'state': issue['state'],
                'created_at': issue['created_at'],
                'updated_at': issue['updated_at'],
                'closed_at': issue.get('closed_at'),
                'labels': [label['name'] for label in issue['labels']],
                'assignees': [assignee['login'] for assignee in issue['assignees']],
                'milestone': issue['milestone']['title'] if issue['milestone'] else None,
                'comments_count': issue['comments'],
                'reactions_total': issue['reactions']['total_count'],
                'reactions_plus_one': issue['reactions']['+1'],
                'reactions_minus_one': issue['reactions']['-1'],
                'reactions_laugh': issue['reactions']['laugh'],
                'reactions_hooray': issue['reactions']['hooray'],
                'reactions_confused': issue['reactions']['confused'],
                'reactions_heart': issue['reactions']['heart'],
                'reactions_rocket': issue['reactions']['rocket'],
                'reactions_eyes': issue['reactions']['eyes'],
                'body_length': len(issue['body']) if issue['body'] else 0,
                'is_pull_request': 'pull_request' in issue,
                'html_url': issue['html_url']
            })
            
        return pd.DataFrame(processed)
```

## GitHub CLI Collection

### Basic Commands
```bash
# Get all issues with basic info
gh issue list --repo Azure/azure-dev --state all --limit 1000 --json number,title,state,createdAt,updatedAt,labels,assignees,milestone,comments

# Get specific issue details
gh issue view 1234 --repo Azure/azure-dev --json number,title,body,comments,reactions

# Search for specific types of issues
gh issue list --repo Azure/azure-dev --search "label:bug" --state all --limit 500

# Export to CSV
gh issue list --repo Azure/azure-dev --state all --limit 1000 --json number,title,state,createdAt,labels > issues.json
```

### Batch Processing Script
```bash
#!/bin/bash

# Collect all issues in batches
REPO="Azure/azure-dev"
OUTPUT_DIR="./raw-data"
mkdir -p $OUTPUT_DIR

# Get issue numbers first
gh issue list --repo $REPO --state all --limit 2000 --json number | jq -r '.[].number' > $OUTPUT_DIR/issue_numbers.txt

# Process in batches of 100
split -l 100 $OUTPUT_DIR/issue_numbers.txt $OUTPUT_DIR/batch_

for batch_file in $OUTPUT_DIR/batch_*; do
    batch_name=$(basename $batch_file)
    echo "Processing batch: $batch_name"
    
    while IFS= read -r issue_number; do
        gh issue view $issue_number --repo $REPO --json number,title,body,state,createdAt,updatedAt,closedAt,labels,assignees,milestone,comments,reactions >> $OUTPUT_DIR/${batch_name}_details.jsonl
    done < $batch_file
    
    # Rate limiting
    sleep 1
done
```

## Web Scraping Alternative

### Selenium-based Collection
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

class GitHubWebScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login_to_github(self, username, password):
        self.driver.get("https://github.com/login")
        # Add login logic here
        
    def scrape_issues_page(self, url):
        self.driver.get(url)
        
        issues = []
        issue_elements = self.driver.find_elements(By.CSS_SELECTOR, "[data-hovercard-type='issue']")
        
        for element in issue_elements:
            # Extract issue data from DOM
            issue_data = {
                'title': element.text,
                'url': element.get_attribute('href'),
                # Add more fields as needed
            }
            issues.append(issue_data)
            
        return issues
```

## Data Processing Pipeline

### 1. Raw Data Validation
```python
def validate_issue_data(df):
    """Validate collected issue data for completeness and accuracy"""
    
    # Check for required fields
    required_fields = ['number', 'title', 'state', 'created_at']
    missing_fields = [field for field in required_fields if field not in df.columns]
    
    if missing_fields:
        raise ValueError(f"Missing required fields: {missing_fields}")
    
    # Check for duplicates
    duplicates = df.duplicated(subset=['number']).sum()
    if duplicates > 0:
        print(f"Warning: {duplicates} duplicate issues found")
    
    # Validate data types
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['updated_at'] = pd.to_datetime(df['updated_at'])
    
    return df
```

### 2. Data Enrichment
```python
def enrich_issue_data(df):
    """Add computed fields and categorizations"""
    
    # Calculate age in days
    df['age_days'] = (pd.Timestamp.now() - df['created_at']).dt.days
    
    # Categorize by engagement
    df['engagement_score'] = (
        df['reactions_total'] * 2 + 
        df['comments_count'] * 1.5
    )
    
    # Categorize by labels
    df['is_bug'] = df['labels'].apply(lambda x: 'bug' in x)
    df['is_enhancement'] = df['labels'].apply(lambda x: 'enhancement' in x)
    df['is_documentation'] = df['labels'].apply(lambda x: any('doc' in label.lower() for label in x))
    
    # Calculate priority score
    df['priority_score'] = (
        df['reactions_plus_one'] * 3 +
        df['reactions_heart'] * 2 +
        df['reactions_rocket'] * 2 +
        df['comments_count'] * 1 +
        (df['age_days'] > 365) * 2  # Boost old issues
    )
    
    return df
```

### 3. Data Export
```python
def export_processed_data(df, output_dir):
    """Export data in multiple formats for analysis"""
    
    # Full dataset
    df.to_csv(f'{output_dir}/all_issues.csv', index=False)
    df.to_json(f'{output_dir}/all_issues.json', orient='records')
    
    # Category-specific exports
    bugs = df[df['is_bug'] == True]
    bugs.to_csv(f'{output_dir}/bug_issues.csv', index=False)
    
    enhancements = df[df['is_enhancement'] == True]
    enhancements.to_csv(f'{output_dir}/enhancement_requests.csv', index=False)
    
    high_engagement = df[df['engagement_score'] > df['engagement_score'].quantile(0.8)]
    high_engagement.to_csv(f'{output_dir}/high_engagement_issues.csv', index=False)
```

## Rate Limiting and Best Practices

### GitHub API Limits
- **Authenticated requests**: 5,000 requests per hour
- **Search API**: 30 requests per minute
- **Secondary rate limits**: Avoid concurrent requests

### Optimization Strategies
```python
import time
from functools import wraps

def rate_limit(calls_per_second=1):
    """Decorator to enforce rate limiting"""
    def decorator(func):
        last_called = [0.0]
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            left_to_wait = 1.0 / calls_per_second - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kwargs)
            last_called[0] = time.time()
            return ret
        return wrapper
    return decorator

@rate_limit(calls_per_second=0.5)  # 2 seconds between calls
def get_issue_details(issue_number):
    # API call here
    pass
```

## Data Quality Checks

### Automated Validation
```python
def run_data_quality_checks(df):
    """Run comprehensive data quality checks"""
    
    checks = {
        'total_issues': len(df),
        'duplicate_issues': df.duplicated(subset=['number']).sum(),
        'missing_titles': df['title'].isna().sum(),
        'future_dates': (df['created_at'] > pd.Timestamp.now()).sum(),
        'negative_reactions': (df['reactions_total'] < 0).sum(),
        'missing_labels': df['labels'].apply(lambda x: len(x) == 0).sum(),
        'data_collection_date': pd.Timestamp.now().isoformat()
    }
    
    # Save quality report
    with open('data_quality_report.json', 'w') as f:
        json.dump(checks, f, indent=2)
    
    return checks
```

## Usage Instructions

### 1. Setup Environment
```bash
# Install dependencies
pip install -r requirements.txt
npm install

# Set up authentication
export GITHUB_TOKEN="your_token_here"

# Create output directories
mkdir -p raw-data processed-data
```

### 2. Run Collection
```bash
# Option 1: Python script
python collect_issues.py

# Option 2: Node.js script
node collect_issues.js

# Option 3: GitHub CLI
./collect_with_gh.sh
```

### 3. Process Data
```bash
python process_issues.py
```

### 4. Validate Results
```bash
python validate_data.py
```

## Troubleshooting

### Common Issues
1. **Rate limiting errors**: Increase sleep times between requests
2. **Authentication failures**: Verify token permissions
3. **Memory issues**: Process data in smaller batches
4. **Network timeouts**: Add retry logic with exponential backoff

### Recovery Strategies
```python
def robust_api_call(func, max_retries=3, backoff_factor=2):
    """Wrapper for robust API calls with retry logic"""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            wait_time = backoff_factor ** attempt
            time.sleep(wait_time)
```

---

*These tools support the comprehensive GitHub issues analysis outlined in [Issue #4445](https://github.com/Azure/azure-dev/issues/4445).*
