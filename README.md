# Azure Developer CLI - GitHub Issues Analysis Project

## Overview
This project contains the comprehensive analysis of GitHub issues in the Azure/azure-dev repository as outlined in [Issue #4445](https://github.com/Azure/azure-dev/issues/4445). The goal is to understand customer pain points, prioritize feature requests, and optimize development efforts based on real user feedback.

## Project Structure
```
github-issues-project/
├── README.md                           # This file - project overview
├── analysis/
│   ├── 01-top-customer-issues.md       # Top customer-reported issues and struggles
│   ├── 02-issue-clustering.md          # Duplicate and similar issue clustering
│   ├── 03-feature-gap-analysis.md      # Features already available vs. requested
│   ├── 04-documentation-gaps.md        # Documentation gaps for existing features
│   ├── 05-trend-analysis.md            # Trend analysis over time
│   └── 06-actionable-recommendations.md # Actionable recommendations
├── data/
│   ├── search-queries.md               # GitHub search queries used
│   ├── raw-data/                       # Raw issue data collected
│   └── processed-data/                 # Cleaned and categorized data
├── reports/
│   ├── issue-analysis-report.md        # High-level report analysis of all issues
│   ├── powershell-pwsh-issues...       # Detailed findings for PowerShell issues
│   ├── multi-env (comprehensive)       # Full report of env issues
│   ├── multi-env (focused)             # Env report focused on customer reported
│   └── env-issues (detailed)           # Env report detailed   
└── tools/
    ├── issue-collector.md              # Scripts/tools for data collection
    └── analysis-helpers.md             # Helper tools and utilities
```

## Objectives

### 1. Top Customer-Reported Issues and Struggles
Identify the most frequently reported problems and developer pain points by analyzing:
- All open and closed issues from Azure/azure-dev repository
- Issue categorization (bugs, feature requests, documentation gaps, usability)
- Engagement metrics (reactions, comments, duplicates)
- Priority ranking based on impact and frequency

### 2. Duplicate and Similar Issue Clustering
Group related issues that may be addressing the same underlying problem:
- Issues with similar titles, descriptions, or error messages
- Common keywords, error codes, or workflows
- Semantic similarity beyond existing GitHub labels
- Root cause analysis for grouped issues

### 3. Features Already Available vs. Requested
Identify features that exist but users aren't aware of them:
- Compare feature requests against existing Azure Developer CLI documentation
- Check CLI help output, README.md, and feature documentation
- Identify communication and documentation gaps

### 4. Documentation Gaps for Existing Features
Find features that exist and are documented but still generate support requests:
- Cross-reference documented features with open issues
- Identify unclear, incomplete, or hard-to-find documentation
- Analyze error messages and workflow guidance needs

### 5. Trend Analysis
Understand how issues evolve over time:
- Issue creation patterns and seasonal trends
- Version-related issue spikes
- Category trends (increasing/decreasing)
- Correlation with CLI releases and feature launches

### 6. Actionable Recommendations
Provide concrete next steps based on the analysis:
- Priority actions with effort estimates
- Quick wins for immediate impact
- Long-term strategic recommendations

## Key Research Areas

### Issue Categories to Analyze:
- Authentication/Login issues
- Environment management problems
- Deployment failures
- Template/scaffolding issues
- CLI installation/setup problems
- VS Code extension issues
- Docker/container related issues
- Azure service integration problems

### User Personas to Consider:
- Individual developers
- Development teams
- Enterprise users
- New users vs. experienced users

## Expected Deliverables

1. **Executive Summary**: Top 10 customer pain points with impact assessment
2. **Issue Clustering Report**: Grouped similar issues with consolidation recommendations
3. **Feature Gap Analysis**: Comparison of requested vs. existing features
4. **Documentation Audit**: Features that need better docs despite existing
5. **Trend Report**: Issue volume and type trends over time
6. **Action Plan**: Prioritized recommendations with effort estimates

## Analysis Methodology

### Data Collection
- Systematic retrieval of all issues from Azure/azure-dev repository
- Engagement metrics collection (reactions, comments, views)
- Issue metadata analysis (labels, assignees, milestones)
- Cross-reference with official documentation

### Analysis Framework
- Quantitative analysis of issue volume and patterns
- Qualitative analysis of issue content and user sentiment
- Comparative analysis of requested vs. existing features
- Temporal analysis of trends and patterns

### Quality Assurance
- Multiple validation passes on categorization
- Cross-verification of findings
- Stakeholder review of recommendations

## Getting Started

1. **Setup**: Review the search queries in `data/search-queries.md`
2. **Data Collection**: Use the tools in `tools/` directory to collect issue data
3. **Analysis**: Follow the analysis templates in `analysis/` directory
4. **Reporting**: Generate final reports using templates in `reports/` directory

## Success Criteria

- [ ] Root causes clearly identified for top issues
- [ ] Specific actionable fixes provided
- [ ] Code examples included where applicable
- [ ] Prevention strategies suggested
- [ ] Reports ready for stakeholder consumption
- [ ] Recommendations prioritized by impact and effort

## Notes

- Focus on customer impact
- Consider the full user journey from installation to deployment
- Look for patterns that might indicate UX/design issues
- Pay attention to different user experience levels
- Prioritize issues that block user success

## Contributing

This analysis is part of the Azure Developer CLI team's ongoing efforts to improve the product based on user feedback. All findings and recommendations will be used to inform future roadmap decisions.

---

*This project was initiated based on [Azure/azure-dev Issue #4445](https://github.com/Azure/azure-dev/issues/4445).*
