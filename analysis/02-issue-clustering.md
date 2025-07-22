# Duplicate and Similar Issue Clustering

## Analysis Framework

**Goal**: Group related issues that may be addressing the same underlying problem to identify opportunities for consolidation and root cause resolution.

## Methodology

### Clustering Approach
- Identify issues with similar titles, descriptions, or error messages
- Look for common keywords, error codes, or workflows
- Group beyond existing GitHub labels using semantic similarity
- Consider issues that might be different symptoms of the same root cause

### Categories to Analyze

#### Authentication/Login Issues
- Login failures
- Token problems
- Permission errors
- Multi-tenant authentication

#### Environment Management Problems
- Environment switching
- Variable configuration
- State management
- Cleanup issues

#### Deployment Failures
- Infrastructure provisioning
- Service deployment
- Configuration errors
- Resource conflicts

#### Template/Scaffolding Issues
- Template initialization
- Customization problems
- Template updates
- Missing templates

#### CLI Installation/Setup Problems
- Installation failures
- Path issues
- Dependency conflicts
- Version mismatches

#### VS Code Extension Issues
- Extension activation
- Command failures
- Integration problems
- UI issues

#### Docker/Container Related Issues
- Container build failures
- Registry problems
- Image issues
- Container runtime errors

#### Azure Service Integration Problems
- Service connectivity
- API failures
- Configuration issues
- Resource management

## Analysis Template

### Issue Cluster #1: [Cluster Name] ([count] issues)

#### Primary Issue
- **Issue**: #[number] - [title]
- **Created**: [date]
- **Status**: [Open/Closed]
- **Reactions**: [count]
- **Comments**: [count]
- **Summary**: [description of main issue]

#### Related Issues
- **#[number]**: [brief title] - [similarity reason]
- **#[number]**: [brief title] - [similarity reason]
- **#[number]**: [brief title] - [similarity reason]

#### Common Patterns
- **Error Messages**: [common error patterns]
- **Keywords**: [recurring terms]
- **Workflows**: [common user scenarios]
- **Environment**: [common setup/configuration]

#### Root Cause Analysis
- **Likely Root Cause**: [analysis of underlying issue]
- **Contributing Factors**: [what makes this happen]
- **User Impact**: [how this affects users]

#### Suggested Consolidation
- **Recommended Primary Issue**: #[number]
- **Issues to Close as Duplicates**: #[list]
- **New Issue Needed**: Yes/No - [description if needed]
- **Action Required**: [specific steps to consolidate]

---

### Issue Cluster #2: [Cluster Name] ([count] issues)

[Same template structure as above]

---

[Continue for all identified clusters...]

## Clustering Summary

### Total Clusters Identified: [number]

### High-Priority Clusters (>5 issues)
1. **[Cluster Name]**: [count] issues - [brief description]
2. **[Cluster Name]**: [count] issues - [brief description]
3. **[Cluster Name]**: [count] issues - [brief description]

### Medium-Priority Clusters (3-5 issues)
1. **[Cluster Name]**: [count] issues - [brief description]
2. **[Cluster Name]**: [count] issues - [brief description]

### Low-Priority Clusters (2 issues)
1. **[Cluster Name]**: [count] issues - [brief description]

## Cross-Category Analysis

### Multi-Category Issues
Issues that span multiple categories:
- **Authentication + Environment**: [count] issues
- **Deployment + Templates**: [count] issues
- **VS Code + CLI**: [count] issues

### Systemic Issues
Patterns that appear across categories:
- **Configuration Management**: Issues across [categories]
- **Error Handling**: Poor error messages across [categories]
- **Documentation**: Missing guidance across [categories]

## Root Cause Patterns

### Technical Debt
- **Legacy Code Issues**: [description]
- **Architecture Limitations**: [description]
- **Dependency Problems**: [description]

### User Experience Issues
- **Workflow Confusion**: [description]
- **Missing Feedback**: [description]
- **Inconsistent Behavior**: [description]

### Documentation/Communication
- **Feature Discovery**: [description]
- **Error Message Clarity**: [description]
- **Troubleshooting Guidance**: [description]

## Consolidation Recommendations

### Immediate Actions
1. **Close Duplicates**: [count] issues can be closed as duplicates
   - Save [estimated hours] of maintenance effort
   - Reduce noise for users searching for solutions

2. **Merge Similar Issues**: [count] issues should be merged
   - Create comprehensive issues with full context
   - Better tracking of resolution progress

3. **Create Master Issues**: [count] new master issues needed
   - Track complex multi-faceted problems
   - Better coordinate resolution efforts

### Process Improvements
1. **Issue Templates**: Update templates to capture clustering information
2. **Labeling Strategy**: Improve labels to reduce future clustering needs
3. **Triage Process**: Include clustering check in triage workflow

### Long-term Strategies
1. **Root Cause Focus**: Address underlying causes rather than symptoms
2. **Proactive Monitoring**: Set up alerts for potential duplicate patterns
3. **User Education**: Improve documentation to prevent recurring issues

## Impact Assessment

### Effort Reduction
- **Triage Time Saved**: [estimated hours per week]
- **Development Focus**: [estimated hours redirected to solutions]
- **Support Burden**: [estimated reduction in support requests]

### User Experience Improvement
- **Faster Resolution**: Consolidated issues get more focused attention
- **Better Search**: Users find existing solutions more easily
- **Clearer Status**: Single source of truth for issue status

### Team Efficiency
- **Reduced Context Switching**: Fewer duplicate investigations
- **Better Prioritization**: Clearer picture of actual issue frequency
- **Improved Planning**: Better understanding of recurring problems

## Implementation Plan

### Phase 1: Quick Wins (Week 1-2)
- Close obvious duplicates
- Merge simple similar issues
- Update labels for clarity

### Phase 2: Complex Consolidation (Week 3-4)
- Create master issues for complex clusters
- Consolidate related discussions
- Update documentation links

### Phase 3: Process Improvement (Week 5-6)
- Implement improved triage process
- Update issue templates
- Train team on new clustering approach

### Phase 4: Monitoring (Ongoing)
- Track clustering effectiveness
- Monitor for new patterns
- Continuous improvement

## Success Metrics

### Quantitative
- Reduction in total open issues: [target %]
- Decrease in duplicate reports: [target %]
- Faster time to resolution: [target improvement]

### Qualitative
- Improved user satisfaction with issue resolution
- Clearer development priorities
- Better team focus on actual problems

---

*This clustering analysis is part of the comprehensive GitHub issues review outlined in [Issue #4445](https://github.com/Azure/azure-dev/issues/4445).*
