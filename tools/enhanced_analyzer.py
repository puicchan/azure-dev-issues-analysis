#!/usr/bin/env python3
"""
Enhanced GitHub Issues Analysis for Azure Developer CLI
Robust version that handles search API limitations and collects comprehensive real data
"""

import requests
import json
import time
import os
from datetime import datetime, timedelta
from pathlib import Path

class EnhancedGitHubAnalyzer:
    def __init__(self, token: str, output_dir: str = "./data/raw-data"):
        self.token = token
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        self.base_url = 'https://api.github.com'
        self.repo_owner = 'Azure'
        self.repo_name = 'azure-dev'
        
        # Rate limiting
        self.rate_limit_remaining = 5000
        self.last_request_time = 0
        
    def make_request(self, url: str, params: dict = None):
        """Make API request with rate limiting and error handling"""
        # Rate limiting
        time_since_last = time.time() - self.last_request_time
        if time_since_last < 1.0:  # Max 1 req/second for search API
            time.sleep(1.0 - time_since_last)
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            self.last_request_time = time.time()
            
            # Check rate limits
            if 'X-RateLimit-Remaining' in response.headers:
                self.rate_limit_remaining = int(response.headers['X-RateLimit-Remaining'])
                print(f"📊 Rate limit remaining: {self.rate_limit_remaining}")
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                print("⚠️  Rate limit exceeded, waiting...")
                time.sleep(60)  # Wait 1 minute
                return self.make_request(url, params)
            else:
                print(f"❌ API Error {response.status_code}: {response.text[:200]}")
                return None
        except Exception as e:
            print(f"❌ Request failed: {e}")
            return None

    def get_all_issues(self, state='all', per_page=100):
        """Get all issues using the direct repository API (more reliable than search)"""
        all_issues = []
        page = 1
        
        print(f"🔍 Collecting all {state} issues...")
        
        while True:
            url = f"{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/issues"
            params = {
                'state': state,
                'per_page': per_page,
                'page': page,
                'sort': 'created',
                'direction': 'desc'
            }
            
            print(f"   📄 Fetching page {page}...")
            data = self.make_request(url, params)
            
            if not data:
                break
                
            # Filter out pull requests (they appear in issues API)
            issues = [issue for issue in data if 'pull_request' not in issue]
            
            if not issues:
                break
                
            all_issues.extend(issues)
            
            if len(data) < per_page:
                break
                
            page += 1
            
            # Safety limit
            if page > 50:  # Max ~5000 issues
                print("⚠️  Reached safety limit, stopping...")
                break
        
        print(f"✅ Collected {len(all_issues)} total issues")
        return all_issues

    def categorize_issues(self, issues):
        """Categorize issues based on title and body content"""
        categories = {
            'authentication': [],
            'environment': [],
            'templates': [],
            'documentation': [],
            'deployment': [],
            'vscode': [],
            'github_actions': [],
            'errors_bugs': [],
            'feature_requests': [],
            'other': []
        }
        
        print("🏷️  Categorizing issues...")
        
        for issue in issues:
            title = issue['title'].lower()
            body = (issue['body'] or '').lower()
            labels = [label['name'].lower() for label in issue.get('labels', [])]
            
            # Count how many categories this issue matches
            matches = []
            
            # Authentication issues
            if any(keyword in title or keyword in body for keyword in 
                   ['auth', 'login', 'authentication', 'credential', 'token', 'oauth']):
                matches.append('authentication')
            
            # Environment issues  
            if any(keyword in title or keyword in body for keyword in 
                   ['env', 'environment', 'variable', 'config', 'setting']):
                matches.append('environment')
            
            # Template issues
            if any(keyword in title or keyword in body for keyword in 
                   ['template', 'scaffold', 'init', 'boilerplate', 'starter']):
                matches.append('templates')
            
            # Documentation issues
            if any(keyword in title or keyword in body for keyword in 
                   ['doc', 'documentation', 'guide', 'tutorial', 'readme', 'how to']):
                matches.append('documentation')
            
            # Deployment issues
            if any(keyword in title or keyword in body for keyword in 
                   ['deploy', 'deployment', 'provision', 'infrastructure', 'bicep', 'arm']):
                matches.append('deployment')
            
            # VS Code issues
            if any(keyword in title or keyword in body for keyword in 
                   ['vscode', 'vs code', 'extension', 'ide']):
                matches.append('vscode')
            
            # GitHub Actions issues
            if any(keyword in title or keyword in body for keyword in 
                   ['github actions', 'workflow', 'ci/cd', 'pipeline', 'action']):
                matches.append('github_actions')
            
            # Feature requests
            if any(keyword in title or keyword in labels for keyword in 
                   ['feature', 'enhancement', 'request', 'improvement']):
                matches.append('feature_requests')
            
            # Bugs/Errors
            if any(keyword in title or keyword in labels for keyword in 
                   ['bug', 'error', 'fail', 'crash', 'issue', 'problem']):
                matches.append('errors_bugs')
            
            # Assign to primary category (or 'other' if no matches)
            if matches:
                primary_category = matches[0]  # Use first match as primary
                categories[primary_category].append(issue)
            else:
                categories['other'].append(issue)
        
        # Print summary
        print("📊 Issue categorization summary:")
        total_categorized = 0
        for category, issues_list in categories.items():
            count = len(issues_list)
            total_categorized += count
            if count > 0:
                print(f"   {category}: {count} issues")
        
        return categories

    def analyze_temporal_trends(self, issues):
        """Analyze issue trends over time"""
        print("📈 Analyzing temporal trends...")
        
        temporal_data = {}
        
        for issue in issues:
            created_date = datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            year_month = f"{created_date.year}-{created_date.month:02d}"
            
            if year_month not in temporal_data:
                temporal_data[year_month] = []
            temporal_data[year_month].append(issue)
        
        # Sort by date
        sorted_months = sorted(temporal_data.keys())
        
        print(f"📅 Issue trends by month (last 12 months):")
        for month in sorted_months[-12:]:
            count = len(temporal_data[month])
            print(f"   {month}: {count} issues")
        
        return temporal_data

    def generate_comprehensive_report(self):
        """Generate comprehensive analysis report"""
        print("🚀 Starting comprehensive Azure/azure-dev analysis...")
        
        # Get repository info
        repo_url = f"{self.base_url}/repos/{self.repo_owner}/{self.repo_name}"
        repo_data = self.make_request(repo_url)
        
        if not repo_data:
            print("❌ Failed to get repository data")
            return
        
        print(f"✅ Repository: {repo_data['full_name']}")
        print(f"📊 Open Issues: {repo_data['open_issues_count']}")
        print(f"⭐ Stars: {repo_data['stargazers_count']}")
        print(f"🍴 Forks: {repo_data['forks_count']}")
        
        # Get all issues
        all_issues = self.get_all_issues(state='all')
        open_issues = [issue for issue in all_issues if issue['state'] == 'open']
        closed_issues = [issue for issue in all_issues if issue['state'] == 'closed']
        
        print(f"📋 Total Issues Found: {len(all_issues)}")
        print(f"📈 Open Issues: {len(open_issues)}")
        print(f"✅ Closed Issues: {len(closed_issues)}")
        
        # Categorize issues
        open_categories = self.categorize_issues(open_issues)
        all_categories = self.categorize_issues(all_issues)
        
        # Temporal analysis
        temporal_data = self.analyze_temporal_trends(all_issues)
        
        # Generate comprehensive data structure
        analysis_results = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'repository': repo_data,
                'total_issues_analyzed': len(all_issues),
                'open_issues_count': len(open_issues),
                'closed_issues_count': len(closed_issues)
            },
            'categorization': {
                'open_issues': {cat: len(issues) for cat, issues in open_categories.items()},
                'all_issues': {cat: len(issues) for cat, issues in all_categories.items()}
            },
            'temporal_trends': {
                month: len(issues) for month, issues in temporal_data.items()
            },
            'top_issues': {
                'most_commented': sorted(open_issues, key=lambda x: x['comments'], reverse=True)[:10],
                'most_recent': sorted(open_issues, key=lambda x: x['created_at'], reverse=True)[:10],
                'oldest_open': sorted(open_issues, key=lambda x: x['created_at'])[:10]
            },
            'sample_issues_by_category': {}
        }
        
        # Add sample issues for each category
        for category, issues_list in open_categories.items():
            if issues_list:
                analysis_results['sample_issues_by_category'][category] = [
                    {
                        'number': issue['number'],
                        'title': issue['title'],
                        'created_at': issue['created_at'],
                        'comments': issue['comments'],
                        'labels': [label['name'] for label in issue.get('labels', [])]
                    }
                    for issue in issues_list[:5]  # Top 5 per category
                ]
        
        # Save comprehensive analysis
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"comprehensive_analysis_{timestamp}.json"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w') as f:
            json.dump(analysis_results, f, indent=2)
        
        print(f"💾 Comprehensive analysis saved to: {filepath}")
        
        # Print summary for immediate reference
        print("\n" + "="*60)
        print("📊 REAL DATA ANALYSIS SUMMARY")
        print("="*60)
        print(f"Repository: {repo_data['full_name']}")
        print(f"Total Issues Analyzed: {len(all_issues)}")
        print(f"Current Open Issues: {len(open_issues)}")
        print(f"Resolution Rate: {len(closed_issues)/len(all_issues)*100:.1f}%")
        print("\n🏷️  Open Issues by Category:")
        for category, count in analysis_results['categorization']['open_issues'].items():
            if count > 0:
                percentage = count / len(open_issues) * 100
                print(f"   {category}: {count} issues ({percentage:.1f}%)")
        
        print(f"\n🎉 SUCCESS! Analyzed {len(all_issues)} real issues from Azure/azure-dev")
        return analysis_results

def main():
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ GITHUB_TOKEN environment variable not found")
        print("Set it with: export GITHUB_TOKEN='your_token_here'")
        return
    
    analyzer = EnhancedGitHubAnalyzer(token)
    results = analyzer.generate_comprehensive_report()
    
    if results:
        print("\n✅ Analysis complete! Ready to update reports with real data.")
        print("📁 Check ./data/raw-data/ for detailed JSON results")

if __name__ == "__main__":
    main()
