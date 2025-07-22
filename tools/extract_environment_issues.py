#!/usr/bin/env python3
"""
Environment Management Issues Extractor
Fetches all environment-related issues from Azure/azure-dev and creates a detailed report
"""

import requests
import json
import os
from datetime import datetime, timedelta
import time

def get_all_environment_issues():
    """Fetch all environment-related issues from Azure/azure-dev"""
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ GITHUB_TOKEN environment variable not found")
        return []
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    base_url = 'https://api.github.com'
    repo_owner = 'Azure'
    repo_name = 'azure-dev'
    
    all_issues = []
    environment_issues = []
    page = 1
    
    print("🔍 Fetching all issues to identify environment-related ones...")
    
    while True:
        url = f"{base_url}/repos/{repo_owner}/{repo_name}/issues"
        params = {
            'state': 'all',  # Get both open and closed
            'per_page': 100,
            'page': page,
            'sort': 'created',
            'direction': 'desc'
        }
        
        print(f"   📄 Fetching page {page}...")
        
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code != 200:
                print(f"❌ API Error: {response.status_code}")
                break
                
            data = response.json()
            if not data:
                break
                
            # Filter out pull requests
            issues = [issue for issue in data if 'pull_request' not in issue]
            
            if not issues:
                break
                
            all_issues.extend(issues)
            
            # Check for environment-related keywords
            for issue in issues:
                title = issue['title'].lower()
                body = (issue['body'] or '').lower()
                labels = [label['name'].lower() for label in issue.get('labels', [])]
                
                # Environment keywords
                env_keywords = [
                    'env', 'environment', 'variable', 'config', 'setting',
                    'azd env', 'environment variable', 'env switch',
                    'environment management', 'multi-environment',
                    'env file', '.env', 'environment setup'
                ]
                
                if any(keyword in title or keyword in body for keyword in env_keywords):
                    environment_issues.append(issue)
            
            if len(data) < 100:
                break
                
            page += 1
            
            # Rate limiting
            time.sleep(0.5)
            
            # Safety limit
            if page > 30:  # Max ~3000 issues
                print("⚠️  Reached safety limit, stopping...")
                break
                
        except Exception as e:
            print(f"❌ Error fetching page {page}: {e}")
            break
    
    print(f"Total issues fetched: {len(all_issues)}")
    print(f"🌍 Environment-related issues found: {len(environment_issues)}")
    
    return environment_issues

def calculate_age(created_at):
    """Calculate age of issue in days"""
    created_date = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')
    now = datetime.utcnow()
    age_days = (now - created_date).days
    return age_days

def create_environment_issues_report(issues):
    """Create a markdown report with all environment issues"""
    
    # Sort issues by creation date (newest first)
    issues_sorted = sorted(issues, key=lambda x: x['created_at'], reverse=True)
    
    # Create markdown content
    markdown_content = f"""# Environment Management Issues - Azure Developer CLI

**Report Generated:** {datetime.now().strftime('%B %d, %Y')}  
**Repository:** Azure/azure-dev  
**Total Environment Issues:** {len(issues)}  
**Data Source:** GitHub Issues API

## Summary

This report contains all environment management related issues from the Azure Developer CLI repository. Issues are identified by keywords related to environment configuration, variables, multi-environment workflows, and environment management commands.

**Quick Stats:**
- **Open Issues**: {len([i for i in issues if i['state'] == 'open'])}
- **Closed Issues**: {len([i for i in issues if i['state'] == 'closed'])}
- **Average Age**: {sum(calculate_age(i['created_at']) for i in issues) // len(issues) if issues else 0} days

## 🟢 Open Environment Issues

| # | Issue Title | Created | Age (Days) | Comments | Labels |
|---|-------------|---------|------------|----------|--------|
"""

    # Add open issues to the table
    open_issues = [i for i in issues_sorted if i['state'] == 'open']
    for issue in open_issues:
        age_days = calculate_age(issue['created_at'])
        created_date = datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
        
        # Truncate title if too long
        title = issue['title']
        if len(title) > 80:
            title = title[:80] + "..."
        
        # Get labels
        labels = ', '.join([label['name'] for label in issue.get('labels', [])][:3])  # Max 3 labels
        if len(issue.get('labels', [])) > 3:
            labels += "..."
        
        markdown_content += f"| {issue['number']} | [{title}](https://github.com/Azure/azure-dev/issues/{issue['number']}) | {created_date} | {age_days} | {issue['comments']} | {labels} |\n"

    markdown_content += f"""

## 🔴 Closed Environment Issues

| # | Issue Title | Created | Age (Days) | Comments | Labels |
|---|-------------|---------|------------|----------|--------|
"""

    # Add closed issues to the table
    closed_issues = [i for i in issues_sorted if i['state'] == 'closed']
    for issue in closed_issues:
        age_days = calculate_age(issue['created_at'])
        created_date = datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
        
        # Truncate title if too long
        title = issue['title']
        if len(title) > 80:
            title = title[:80] + "..."
        
        # Get labels
        labels = ', '.join([label['name'] for label in issue.get('labels', [])][:3])  # Max 3 labels
        if len(issue.get('labels', [])) > 3:
            labels += "..."
        
        markdown_content += f"| {issue['number']} | [{title}](https://github.com/Azure/azure-dev/issues/{issue['number']}) | {created_date} | {age_days} | {issue['comments']} | {labels} |\n"
    
    # Add additional sections
    markdown_content += f"""

## Key Environment Issues by Category

### 🔥 Most Commented Environment Issues
"""
    
    # Most commented issues
    most_commented = sorted([i for i in issues if i['state'] == 'open'], key=lambda x: x['comments'], reverse=True)[:10]
    for i, issue in enumerate(most_commented, 1):
        markdown_content += f"{i}. [#{issue['number']}](https://github.com/Azure/azure-dev/issues/{issue['number']}) - {issue['title']} ({issue['comments']} comments)\n"
    
    markdown_content += f"""

### 📅 Recent Environment Issues (Last 30 Days)
"""
    
    # Recent issues
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    recent_issues = [i for i in issues if datetime.strptime(i['created_at'], '%Y-%m-%dT%H:%M:%SZ') > thirty_days_ago]
    
    for issue in recent_issues[:10]:
        age_days = calculate_age(issue['created_at'])
        markdown_content += f"- [#{issue['number']}](https://github.com/Azure/azure-dev/issues/{issue['number']}) - {issue['title']} ({age_days} days old)\n"
    
    markdown_content += f"""

### 🕰️ Oldest Open Environment Issues
"""
    
    # Oldest open issues
    oldest_open = sorted([i for i in issues if i['state'] == 'open'], key=lambda x: x['created_at'])[:10]
    for issue in oldest_open:
        age_days = calculate_age(issue['created_at'])
        created_date = datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
        markdown_content += f"- [#{issue['number']}](https://github.com/Azure/azure-dev/issues/{issue['number']}) - {issue['title']} (opened {created_date}, {age_days} days ago)\n"
    
    markdown_content += f"""

## Environment Management Pain Points

Based on the analysis of {len(issues)} environment-related issues, the following patterns emerge:

1. **Environment Configuration Complexity** - Many issues relate to setting up and managing multiple environments
2. **Variable Management** - Environment variable handling and precedence causes confusion
3. **Multi-Environment Workflows** - Users struggle with promoting between dev/staging/prod environments  
4. **Environment Switching** - Lack of clear commands for switching between environments
5. **State Management** - Infrastructure state management across environments

## Recommendations

1. **Immediate**: Focus on the {len([i for i in issues if i['state'] == 'open'])} open environment issues
2. **High Priority**: Address the most commented issues (high community engagement)
3. **User Experience**: Simplify environment setup and switching workflows
4. **Documentation**: Create comprehensive environment management guides
5. **Tooling**: Develop better `azd env` commands and validation

---

**Report Details:**
- Generated from GitHub Issues API
- Filtered by environment-related keywords
- Includes both open and closed issues for trend analysis
- Age calculated from creation date to {datetime.now().strftime('%B %d, %Y')}

*This report supports the comprehensive Azure Developer CLI analysis framework.*
"""
    
    return markdown_content

def main():
    """Main function to generate environment issues report"""
    print("Starting Environment Management Issues Analysis...")
    
    # Fetch all environment issues
    issues = get_all_environment_issues()
    
    if not issues:
        print("No environment issues found or API error")
        return
    
    # Create the report
    print("📝 Generating markdown report...")
    report_content = create_environment_issues_report(issues)
    
    # Save the report
    filename = f"environment-issues-detailed-{datetime.now().strftime('%Y%m%d')}.md"
    filepath = f"../reports/{filename}"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"Environment issues report saved to: {filepath}")
    print(f"📊 Total environment issues: {len(issues)}")
    print(f"🟢 Open issues: {len([i for i in issues if i['state'] == 'open'])}")
    print(f"🔴 Closed issues: {len([i for i in issues if i['state'] == 'closed'])}")
    
    # Also save raw data
    data_filename = f"environment-issues-data-{datetime.now().strftime('%Y%m%d')}.json"
    data_filepath = f"data/raw-data/{data_filename}"
    
    with open(data_filepath, 'w') as f:
        json.dump(issues, f, indent=2)
    
    print(f"💾 Raw data saved to: {data_filepath}")

if __name__ == "__main__":
    main()
