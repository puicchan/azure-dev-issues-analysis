We want to understand (beyond issue tags) what the most pressing areas are where customers have gaps in the azd product and what they need for their workflows. We want to know what issues are most recurring. This issue outlines our goals and describes what we want to evaluate. 

# Azure Developer CLI - GitHub Issues Analysis

## Objective

Analyze all GitHub issues in the Azure/azure-dev repository to identify customer pain points, prioritize feature requests, and optimize development efforts based on real user feedback.

### 1. Top Customer-Reported Issues and Struggles

**Goal**: Identify the most frequently reported problems and developer pain points.

**Instructions**:

- Retrieve all open and closed issues from the Azure/azure-dev repository
- Categorize issues by type: bugs, feature requests, documentation gaps, usability issues
- Count mentions, upvotes (👍 reactions), and comments as engagement metrics
- Rank issues by:
  - Total reactions (👍, ❤️, 🚀, 👀)
  - Number of comments
  - Number of duplicate/similar issues
  - Recency and frequency of reports

**Output Format**:
```
Top 10 Customer Issues
[Issue Title] - #1234
   - Type: Bug/Feature/Documentation
   - Reactions: 👍 25, ❤️ 5, 🚀 3
   - Comments: 15
   - Status: Open/Closed
   - Summary: Brief description of the issue
   - Impact: High/Medium/Low
```

### 2. Duplicate and Similar Issue Clustering
**Goal**: Group related issues that may be addressing the same underlying problem.

**Instructions**:
- Identify issues with similar titles, descriptions, or error messages
- Look for common keywords, error codes, or workflows
- Group beyond existing GitHub labels using semantic similarity
- Consider issues that might be different symptoms of the same root cause

**Categories to check**:
- Authentication/Login issues
- Environment management problems
- Deployment failures
- Template/scaffolding issues
- CLI installation/setup problems
- VS Code extension issues
- Docker/container related issues
- Azure service integration problems

**Output Format**:
```
Issue Clusters:
1. Authentication Issues (15 issues)
   - Primary: #1234 "azd auth login fails with..."
   - Related: #1235, #1236, #1237...
   - Common patterns: [list patterns]
   - Suggested consolidation: [recommendation]

2. Environment Management (12 issues)
   - Primary: #2345 "Cannot switch environments..."
   - Related: #2346, #2347...
```

### 3. Features Already Available vs. Requested
**Goal**: Identify features that exist but users aren't aware of them.

**Instructions**:
- Compare open feature requests against the Azure Developer CLI documentation at aka.ms/azd
- Check the CLI help output, README.md, and feature documentation
- Look for requests for features that already exist in the current version
- Identify communication/documentation gaps

**Research Areas**:
- CLI commands and flags available vs. requested
- VS Code extension features vs. requests
- Template capabilities vs. requests
- Environment management features vs. requests
- Authentication methods vs. requests
- Deployment options vs. requests

**Output Format**:
```
Existing Features Being Requested:
1. Feature: "Support for multiple environments"
   - Requested in: #1234, #1235, #1236
   - Already exists: Yes, via 'azd env' commands
   - Documentation: Link to docs
   - Gap: Users unaware of feature / poor discoverability

2. Feature: "Custom deployment hooks"
   - Requested in: #2345
   - Already exists: Yes, via azure.yaml hooks
   - Documentation: Link to docs
   - Gap: Documentation needs improvement
```

### 4. Documentation Gaps for Existing Features
**Goal**: Find features that exist and are documented but still generate support requests.

**Instructions**:
- Cross-reference documented features with open issues requesting help
- Look for patterns where users struggle despite documentation existing
- Identify areas where docs might be unclear, incomplete, or hard to find

**Analysis Points**:
- Features with both documentation AND open issues asking "how to..."
- Error messages that could be clearer
- Workflows that need better examples
- Integration scenarios that need more guidance

**Output Format**:
```
Documentation Improvement Opportunities:
1. Feature: Environment Variables
   - Documentation exists: Yes (link)
   - Open issues: #1234, #1235 (users still confused)
   - Problem: Documentation unclear about precedence order
   - Suggestion: Add more examples and troubleshooting section

2. Feature: Custom Templates
   - Documentation exists: Yes (link)
   - Open issues: #2345, #2346 (users struggling with setup)
   - Problem: Missing step-by-step tutorial
   - Suggestion: Create getting-started guide with video
```

### 5. Trend Analysis
**Goal**: Understand how issues evolve over time and identify emerging problems.

**Instructions**:
- Analyze issue creation dates to identify trends
- Look for seasonal patterns or version-related spikes
- Identify if certain types of issues are increasing/decreasing
- Correlate with CLI releases and major feature launches

**Output Format**:
```
Trend Analysis:
- Issue volume by month: [chart/data]
- Top growing issue categories: [list]
- Post-release issue patterns: [analysis]
- User adoption challenges: [insights]
```

### 6. Actionable Recommendations
**Goal**: Provide concrete next steps based on the analysis.

**Output Format**:
```
Priority Actions:
1. HIGH: Fix top 5 most-voted bugs
2. HIGH: Improve documentation for [specific features]
3. MEDIUM: Consolidate duplicate issues and communicate existing features
4. MEDIUM: Create better error messages for common failure scenarios
5. LOW: Consider new features based on validated demand

Quick Wins:
- Update documentation for features users don't know exist
- Add better examples to existing docs
- Improve error messages with actionable guidance
- Create troubleshooting guides for common issues
```

## Search Queries to Use

```
# Get all issues with high engagement
repo:Azure/azure-dev is:issue reactions:>5

# Find feature requests
repo:Azure/azure-dev is:issue label:"enhancement" is:open

# Find bugs with high impact
repo:Azure/azure-dev is:issue label:"bug" reactions:>3

# Authentication issues
repo:Azure/azure-dev is:issue "auth" OR "login" OR "authentication"

# Environment issues
repo:Azure/azure-dev is:issue "environment" OR "env" in:title

# Template issues
repo:Azure/azure-dev is:issue "template" OR "scaffold" in:title

# Documentation requests
repo:Azure/azure-dev is:issue "documentation" OR "docs" OR "how to"

# VS Code extension issues
repo:Azure/azure-dev is:issue "vscode" OR "extension" in:title

# Recent high-priority issues
repo:Azure/azure-dev is:issue created:>2024-01-01 reactions:>2
```

## Expected Deliverables

1. **Executive Summary**: Top 10 customer pain points with impact assessment
2. **Issue Clustering Report**: Grouped similar issues with consolidation recommendations  
3. **Feature Gap Analysis**: Comparison of requested vs. existing features
4. **Documentation Audit**: Features that need better docs despite existing
5. **Trend Report**: Issue volume and type trends over time
6. **Action Plan**: Prioritized recommendations with effort estimates

## Notes for Analysis
- Focus on customer impact over internal development convenience
- Consider the full user journey from installation to deployment
- Look for patterns that might indicate UX/design issues
- Pay attention to new user vs. experienced user issues
- Consider different user personas (individual developers, teams, enterprises)


