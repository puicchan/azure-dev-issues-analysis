# SAML Authentication Fix - Step by Step Guide

## Problem: Cannot Access Azure/azure-dev Repository Data

The Azure organization has **SAML Single Sign-On (SSO) enforcement** enabled, which blocks standard GitHub API access.

## ✅ Solution: Choose Your Authentication Method

### Option 1: GitHub CLI (Easiest - Recommended)

#### Step 1: Install GitHub CLI
```bash
# Windows
winget install GitHub.cli

# Or download from: https://cli.github.com/
```

#### Step 2: Authenticate with SAML support
```bash
# This handles SAML automatically
gh auth login --web
```

#### Step 3: Test access
```bash
# Test repository access
gh repo view Azure/azure-dev

# Test issue access  
gh issue list --repo Azure/azure-dev --limit 5
```

#### Step 4: Run analysis with GitHub CLI
```bash
# The framework can use GitHub CLI instead of direct API
python run_queries.py --use-cli
```

---

### Option 2: Personal Access Token with SAML Authorization

#### Step 1: Create GitHub Personal Access Token
1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token (classic)"**
3. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read org membership, teams, etc.)
   - ✅ `read:user` (Read user profile data)
4. Click **"Generate token"**
5. **Copy the token immediately** (you won't see it again)

#### Step 2: Authorize Token for Azure Organization SAML
1. On the same tokens page, find your new token
2. Click **"Configure SSO"** next to it
3. Click **"Authorize"** for the **"Azure"** organization
4. You'll be redirected to Azure SSO login
5. Complete the Microsoft/Azure authentication flow
6. Return to GitHub - you should see "Authorized" status

#### Step 3: Set Environment Variable
```bash
# Windows (Command Prompt)
set GITHUB_TOKEN=your_token_here

# Windows (PowerShell)
$env:GITHUB_TOKEN="your_token_here"

# Bash (WSL/Git Bash)
export GITHUB_TOKEN="your_token_here"
```

#### Step 4: Test Authentication
```bash
python test_auth.py
```

You should see:
```
✅ SUCCESS! Access confirmed to Azure/azure-dev
📊 Repository: Azure/azure-dev
📈 Open Issues: 839
```

#### Step 5: Run Full Analysis
```bash
python run_queries.py
```

---

### Option 3: Request Azure Organization Membership

#### If you're working with Azure frequently:
1. Contact Azure DevRel team or repository maintainers
2. Request to be added to the Azure organization
3. Accept invitation and link your Microsoft account
4. Once a member, regular tokens work without SAML authorization

---

## 🔧 Troubleshooting Common Issues

### "Resource not accessible by integration"
- **Cause:** Token not authorized for Azure org SAML
- **Fix:** Complete Step 2 above (Configure SSO)

### "Bad credentials" 
- **Cause:** Token expired or invalid
- **Fix:** Generate new token and authorize for SAML

### "API rate limit exceeded"
- **Cause:** Too many unauthenticated requests
- **Fix:** Use proper authentication (Option 1 or 2)

### "Repository not found"
- **Cause:** SAML enforcement blocking access
- **Fix:** Complete SAML authorization flow

---

## 🚀 Quick Test Commands

### Test with curl:
```bash
curl -H "Authorization: token YOUR_TOKEN" \
     "https://api.github.com/repos/Azure/azure-dev" | jq '.open_issues_count'
```

### Test with GitHub CLI:
```bash
gh api /repos/Azure/azure-dev | jq '.open_issues_count'
```

### Test with Python:
```bash
python test_auth.py
```

---

## ⚡ Next Steps After Authentication Success

1. **Run the analysis:**
   ```bash
   python run_queries.py
   ```

2. **Generate reports:**
   ```bash
   python run_analysis.py
   ```

3. **Review results:**
   - Check `data/raw-data/` for collected issue data
   - Check `reports/` for generated analysis reports
   - All placeholder data will be replaced with real insights

4. **Customize analysis:**
   - Edit `config.yaml` to focus on specific categories
   - Modify time ranges in `run_queries.py`
   - Add custom queries for your specific needs

---

## 📞 Need Help?

If you're still having authentication issues:

1. **Check Azure organization access:** Visit https://github.com/orgs/Azure/people
2. **Verify token scopes:** Ensure `repo` and `read:org` are selected
3. **Try GitHub CLI:** Often easier than token management
4. **Contact Azure team:** For organization membership requests

Once authentication is working, the framework will replace all placeholder data with real insights from the 839+ open issues in the Azure/azure-dev repository!
