#!/usr/bin/env python3
"""
GitHub Authentication Test for Azure Organization
Tests whether current GitHub authentication can access Azure/azure-dev repository
"""

import requests
import os
import sys

def test_github_access():
    """Test GitHub API access to Azure organization repository"""
    print("🔍 Testing GitHub API access to Azure/azure-dev repository...")
    
    # Check for GitHub token
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ No GITHUB_TOKEN environment variable found")
        print("💡 Set your token: export GITHUB_TOKEN='your_token_here'")
        return False
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Test basic repository access
    print("📡 Making API request to Azure/azure-dev...")
    response = requests.get(
        'https://api.github.com/repos/Azure/azure-dev',
        headers=headers
    )
    
    if response.status_code == 200:
        data = response.json()
        print("✅ SUCCESS! Access confirmed to Azure/azure-dev")
        print(f"📊 Repository: {data['full_name']}")
        print(f"📈 Open Issues: {data['open_issues_count']}")
        print(f"⭐ Stars: {data['stargazers_count']}")
        print(f"🍴 Forks: {data['forks_count']}")
        print(f"📅 Created: {data['created_at']}")
        return True
        
    elif response.status_code == 404:
        print("❌ SAML AUTHENTICATION ISSUE")
        print("🔒 The Azure organization has SAML SSO enforcement enabled")
        print("🔧 SOLUTION:")
        print("   1. Go to: https://github.com/settings/tokens")
        print("   2. Find your token and click 'Configure SSO'")
        print("   3. Authorize for 'Azure' organization")
        print("   4. Complete Azure SSO login flow")
        return False
        
    elif response.status_code == 401:
        print("❌ INVALID TOKEN")
        print("🔧 SOLUTION:")
        print("   1. Check your token is correct")
        print("   2. Ensure token has 'repo' and 'read:org' scopes")
        print("   3. Generate new token if needed")
        return False
        
    else:
        print(f"❌ API ERROR: {response.status_code}")
        print(f"📄 Response: {response.text}")
        return False

def test_issue_access():
    """Test access to repository issues"""
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        return False
        
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    print("\n🔍 Testing issue access...")
    response = requests.get(
        'https://api.github.com/repos/Azure/azure-dev/issues?state=open&per_page=5',
        headers=headers
    )
    
    if response.status_code == 200:
        issues = response.json()
        print(f"✅ Successfully accessed {len(issues)} recent issues")
        for i, issue in enumerate(issues[:3], 1):
            print(f"   {i}. #{issue['number']}: {issue['title'][:60]}...")
        return True
    else:
        print(f"❌ Cannot access issues: {response.status_code}")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print("🚀 Azure Developer CLI - GitHub Authentication Test")
    print("=" * 60)
    
    # Test repository access
    repo_access = test_github_access()
    
    if repo_access:
        # Test issue access
        issue_access = test_issue_access()
        
        if issue_access:
            print("\n🎉 ALL TESTS PASSED!")
            print("✅ Ready to run the analysis framework")
            print("▶️  Next step: python run_queries.py")
        else:
            print("\n⚠️  Repository access OK, but issue access failed")
    else:
        print("\n❌ Authentication setup required before running analysis")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
