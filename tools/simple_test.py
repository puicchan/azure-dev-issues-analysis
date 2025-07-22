#!/usr/bin/env python3
"""
Simple test to get real Azure/azure-dev issues data
"""

import requests
import json
import os

def get_real_issues():
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ No GITHUB_TOKEN found")
        return
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Get basic repository info
    print("🔍 Getting repository information...")
    repo_response = requests.get(
        'https://api.github.com/repos/Azure/azure-dev',
        headers=headers
    )
    
    if repo_response.status_code == 200:
        repo_data = repo_response.json()
        print(f"✅ Repository: {repo_data['full_name']}")
        print(f"📈 Open Issues: {repo_data['open_issues_count']}")
        print(f"⭐ Stars: {repo_data['stargazers_count']}")
        print(f"🍴 Forks: {repo_data['forks_count']}")
        
        # Get some actual issues
        print("\n🔍 Getting recent open issues...")
        issues_response = requests.get(
            'https://api.github.com/repos/Azure/azure-dev/issues?state=open&per_page=10',
            headers=headers
        )
        
        if issues_response.status_code == 200:
            issues = issues_response.json()
            print(f"✅ Retrieved {len(issues)} issues:")
            
            auth_issues = 0
            env_issues = 0
            template_issues = 0
            
            for issue in issues[:5]:
                print(f"   #{issue['number']}: {issue['title'][:60]}...")
                
                # Simple categorization
                title_lower = issue['title'].lower()
                if 'auth' in title_lower or 'login' in title_lower:
                    auth_issues += 1
                if 'env' in title_lower or 'environment' in title_lower:
                    env_issues += 1
                if 'template' in title_lower or 'scaffold' in title_lower:
                    template_issues += 1
            
            print(f"\n📊 Quick Analysis (from first 10 issues):")
            print(f"   🔐 Authentication-related: {auth_issues}")
            print(f"   🌍 Environment-related: {env_issues}")
            print(f"   📋 Template-related: {template_issues}")
            
            # Save sample data
            with open('sample_real_data.json', 'w') as f:
                json.dump({
                    'repository': repo_data,
                    'sample_issues': issues[:10],
                    'analysis_timestamp': '2025-07-21',
                    'total_open_issues': repo_data['open_issues_count']
                }, f, indent=2)
            
            print(f"\n💾 Saved sample data to: sample_real_data.json")
            print(f"🎉 SUCCESS: We have access to REAL Azure/azure-dev data!")
            
        else:
            print(f"❌ Failed to get issues: {issues_response.status_code}")
    else:
        print(f"❌ Failed to get repo: {repo_response.status_code}")

if __name__ == "__main__":
    get_real_issues()
