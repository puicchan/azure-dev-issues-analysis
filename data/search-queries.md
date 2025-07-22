# GitHub Search Queries for Azure Developer CLI Analysis

This document contains the GitHub search queries to be used for comprehensive issue analysis of the Azure/azure-dev repository.

## Core Issue Retrieval Queries

### All Issues with High Engagement
```
repo:Azure/azure-dev is:issue reactions:>5
```
*Purpose: Find issues that have significant community interest*

### Feature Requests
```
repo:Azure/azure-dev is:issue label:"enhancement" is:open
```
*Purpose: Identify requested features and improvements*

### High-Impact Bugs
```
repo:Azure/azure-dev is:issue label:"bug" reactions:>3
```
*Purpose: Find bugs that are affecting many users*

### Recent High-Priority Issues
```
repo:Azure/azure-dev is:issue created:>2024-01-01 reactions:>2
```
*Purpose: Identify emerging issues and recent pain points*

## Category-Specific Queries

### Authentication Issues
```
repo:Azure/azure-dev is:issue "auth" OR "login" OR "authentication"
```
*Purpose: Find all authentication-related problems*

```
repo:Azure/azure-dev is:issue "azd auth" OR "authentication failed" OR "login error"
```
*Purpose: Specific auth command issues*

### Environment Management Issues
```
repo:Azure/azure-dev is:issue "environment" OR "env" in:title
```
*Purpose: Environment setup and management problems*

```
repo:Azure/azure-dev is:issue "azd env" OR "environment variable" OR "env switch"
```
*Purpose: Specific environment command issues*

### Template and Scaffolding Issues
```
repo:Azure/azure-dev is:issue "template" OR "scaffold" in:title
```
*Purpose: Template-related problems*

```
repo:Azure/azure-dev is:issue "azd init" OR "template creation" OR "scaffold"
```
*Purpose: Project initialization issues*

### Documentation Requests
```
repo:Azure/azure-dev is:issue "documentation" OR "docs" OR "how to"
```
*Purpose: Documentation gaps and requests*

### VS Code Extension Issues
```
repo:Azure/azure-dev is:issue "vscode" OR "extension" in:title
```
*Purpose: VS Code integration problems*

### Deployment Issues
```
repo:Azure/azure-dev is:issue "azd deploy" OR "deployment failed" OR "deploy error"
```
*Purpose: Deployment-related problems*

```
repo:Azure/azure-dev is:issue "azd up" OR "provisioning" OR "infrastructure"
```
*Purpose: Infrastructure provisioning issues*

### Installation and Setup Issues
```
repo:Azure/azure-dev is:issue "install" OR "setup" OR "getting started"
```
*Purpose: Initial setup and installation problems*

### Docker and Container Issues
```
repo:Azure/azure-dev is:issue "docker" OR "container" OR "containerization"
```
*Purpose: Container-related issues*

### Azure Service Integration Issues
```
repo:Azure/azure-dev is:issue "azure" AND ("service" OR "integration" OR "resource")
```
*Purpose: Azure service integration problems*

## Advanced Analysis Queries

### Duplicate Issue Detection
```
repo:Azure/azure-dev is:issue "duplicate" OR "same as" OR "similar to"
```
*Purpose: Find issues marked as duplicates*

### Error Message Patterns
```
repo:Azure/azure-dev is:issue "error:" OR "failed:" OR "exception:"
```
*Purpose: Find issues with specific error patterns*

### User Experience Issues
```
repo:Azure/azure-dev is:issue "UX" OR "user experience" OR "confusing" OR "unclear"
```
*Purpose: Identify UX/usability problems*

### Performance Issues
```
repo:Azure/azure-dev is:issue "slow" OR "performance" OR "timeout" OR "hang"
```
*Purpose: Performance-related complaints*

### Platform-Specific Issues
```
repo:Azure/azure-dev is:issue "windows" OR "linux" OR "macos" OR "platform"
```
*Purpose: Platform-specific problems*

## Temporal Analysis Queries

### Issues by Time Period
```
repo:Azure/azure-dev is:issue created:2024-01-01..2024-03-31
repo:Azure/azure-dev is:issue created:2024-04-01..2024-06-30
repo:Azure/azure-dev is:issue created:2024-07-01..2024-09-30
repo:Azure/azure-dev is:issue created:2024-10-01..2024-12-31
```
*Purpose: Quarterly trend analysis*

### Recently Closed Issues
```
repo:Azure/azure-dev is:issue is:closed closed:>2024-06-01
```
*Purpose: Recently resolved issues for pattern analysis*

### Long-Standing Open Issues
```
repo:Azure/azure-dev is:issue is:open created:<2024-01-01
```
*Purpose: Persistent problems that need attention*

## Engagement Analysis Queries

### Most Commented Issues
```
repo:Azure/azure-dev is:issue comments:>10 sort:comments-desc
```
*Purpose: Issues generating most discussion*

### Most Reacted Issues
```
repo:Azure/azure-dev is:issue reactions:>10 sort:reactions-desc
```
*Purpose: Issues with highest community engagement*

### Recently Updated Issues
```
repo:Azure/azure-dev is:issue updated:>2024-06-01 sort:updated-desc
```
*Purpose: Active ongoing discussions*

## Label-Based Analysis

### Bug Analysis
```
repo:Azure/azure-dev is:issue label:bug is:open
repo:Azure/azure-dev is:issue label:bug is:closed
```

### Enhancement Requests
```
repo:Azure/azure-dev is:issue label:enhancement is:open
```

### Help Wanted
```
repo:Azure/azure-dev is:issue label:"help wanted" is:open
```

### Good First Issues
```
repo:Azure/azure-dev is:issue label:"good first issue" is:open
```

## Usage Instructions

1. **Sequential Execution**: Run these queries in order to build a comprehensive dataset
2. **Rate Limiting**: GitHub API has rate limits - space out queries appropriately
3. **Data Export**: Export results to CSV/JSON for further analysis
4. **Cross-Reference**: Use multiple queries to validate findings
5. **Manual Review**: Sample review of results to ensure query accuracy

## Data Collection Notes

- **Pagination**: Most queries will require pagination for complete results
- **API vs Web**: Some queries work better through GitHub API vs web interface
- **Authentication**: API access requires proper authentication for higher rate limits
- **Date Ranges**: Adjust date ranges based on analysis requirements
- **Sorting**: Different sort orders may reveal different insights

## Query Validation

Before running analysis:
1. Test each query manually to ensure it returns expected results
2. Verify date ranges are appropriate for analysis scope
3. Check that label names match repository's actual labels
4. Confirm query syntax is correct for chosen interface (API vs web)

---

*These queries are designed to provide comprehensive coverage of all issue types and patterns in the Azure/azure-dev repository for thorough analysis.*
