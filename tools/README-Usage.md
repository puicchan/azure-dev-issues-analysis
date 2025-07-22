# Azure Developer CLI GitHub Issues Analysis - Usage Guide

## Overview

This project provides a comprehensive framework for analyzing GitHub issues in the Azure/azure-dev repository. The framework has been updated to cover the complete repository history from July 2022 through July 2025.

## Repository Information

**Target Repository:** Azure/azure-dev
- **Purpose:** Developer CLI that reduces the time it takes to get started on Azure
- **Created:** July 5, 2022
- **Language:** Go
- **Current Open Issues:** 839
- **Community:** 466 stars, 234 forks

## Key Analysis Areas

### 1. Client Usage Tracking
Understanding how Azure Developer CLI (azd) tracks usage across different environments:
- **Desktop CLI:** Direct command-line execution
- **GitHub Actions:** CI/CD pipeline integration
- **VS Code Extension:** IDE development scenarios  
- **CloudShell:** Browser-based development
- **Jenkins/Azure DevOps:** Enterprise CI/CD platforms

### 2. Authentication Patterns
Analysis of authentication-related issues across platforms:
- Cross-platform authentication challenges
- Service principal configuration
- Multi-tenant scenarios
- Browser vs. CLI authentication flows

### 3. Environment Management
Template system and deployment orchestration issues:
- Template discovery and selection
- Environment configuration management
- Resource provisioning patterns
- Multi-environment workflows

## How to Run the Analysis

### Prerequisites
- Python 3.7+
- GitHub Personal Access Token with appropriate permissions
- Access to Azure organization repositories (requires SAML authentication)

### Setup Instructions

1. **Clone or download the analysis framework:**
   ```bash
   cd github-issues-project/tools
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your GitHub token:**
   ```bash
   # Option 1: Environment variable
   export GITHUB_TOKEN="your_token_here"
   
   # Option 2: Config file
   cp config_template.yaml config.yaml
   # Edit config.yaml with your token
   ```

### Running the Analysis

#### Complete Analysis (All Issues)
```bash
python run_queries.py --token YOUR_GITHUB_TOKEN
```

#### Open Issues Only
```bash
python run_queries.py --token YOUR_GITHUB_TOKEN --state open
```

#### Using Configuration File
```bash
python run_queries.py --config config.yaml
```

### Expected Output

The analysis will generate:

1. **Raw Data:** JSON files in `data/raw-data/`
   - `all_queries_combined_TIMESTAMP.json`
   - `category_queries_TIMESTAMP.json`
   - `temporal_queries_TIMESTAMP.json`

2. **Analysis Reports:**
   - `reports/issue-analysis-report.md` (comprehensive analysis)
   - `reports/open-issues-analysis.md` (open issues only)
   - `reports/action-plan.md` (strategic recommendations)

## Important Notes

### Azure Organization Access
The Azure/azure-dev repository requires SAML authentication through the Azure organization. You may encounter this error:

```
403 Resource protected by organization SAML enforcement. 
You must grant your OAuth token access to this organization.
```

**Solution:** Ensure your GitHub token has been authorized for the Azure organization through their SAML SSO requirements.

### Rate Limiting
The script implements conservative rate limiting (1 request per second) to avoid GitHub API limits. For large analyses, expect runtime of 30-60 minutes.

### Analysis Scope

The framework has been updated to cover:
- **Historical Period:** July 2022 - July 2025 (complete repository history)
- **Temporal Analysis:** Quarterly breakdowns from 2022 through 2025
- **Client Tracking:** Focus on user-agent and header analysis for different platforms
- **Authentication:** Cross-platform authentication pattern analysis

## Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Verify your GitHub token has appropriate permissions
   - Check if Azure organization SAML access is required

2. **Rate Limiting**
   - The script automatically handles rate limits with delays
   - For repeated failures, check your API quota

3. **Empty Results**
   - Verify repository name and permissions
   - Check that your token can access the Azure organization

### Getting Help

1. Check the generated log files for detailed error information
2. Verify your GitHub token permissions in GitHub Settings
3. Review the Azure organization's SAML requirements

## Framework Capabilities

This analysis framework can process:
- **Issue Categories:** Authentication, environment, templates, documentation, etc.
- **Temporal Patterns:** Quarterly and yearly trends
- **Engagement Metrics:** Community reactions, comments, and priority indicators
- **Client Usage:** Platform-specific usage patterns and challenges
- **Resolution Tracking:** Issue lifecycle and resolution patterns

The framework generates actionable insights for product teams to prioritize improvements and understand user pain points across different usage scenarios.
