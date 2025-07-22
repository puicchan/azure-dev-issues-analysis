# GitHub Action Failure Analysis Prompt

## Objective

Analyze the failed GitHub Action run and create a comprehensive report for the template author to help them fix their failing template.

## Context

Repository: Azure/ai-app-templates  
Failed Action Run: <https://github.com/Azure/ai-app-templates/actions/runs/16093417318/job/45412998826#logs>

## Instructions for GitHub Copilot

Please analyze the failed GitHub Action run and provide a detailed report following this structure:

### 1. Failure Summary

- **Action Run ID**: [Extract from URL]
- **Job ID**: [Extract from URL]
- **Template/Workflow Name**: [Identify which template is being tested]
- **Failure Type**: [Build failure, test failure, deployment failure, etc.]
- **Timestamp**: [When the failure occurred]

### 2. Root Cause Analysis

- **Primary Error**: [Main error message from logs]
- **Error Location**: [File, line number, or step where error occurred]
- **Error Category**: [Dependency issue, configuration error, code bug, etc.]
- **Contributing Factors**: [Additional issues that may have contributed]

### 3. Detailed Log Analysis

Please examine the logs and provide:

- **Pre-failure Context**: What was happening before the failure
- **Failure Point**: Exact moment and reason for failure
- **Error Messages**: All relevant error messages with context
- **Stack Traces**: If applicable, include relevant stack traces
- **Environment Information**: OS, runtime versions, dependencies

### 4. Impact Assessment

- **Affected Components**: Which parts of the template are impacted
- **Severity Level**: Critical/High/Medium/Low
- **User Impact**: How this affects users trying to use the template
- **Regression Analysis**: Is this a new issue or existing problem

### 5. Recommended Fixes

Provide actionable recommendations:

- **Immediate Fixes**: Quick solutions to resolve the issue
- **Code Changes**: Specific code modifications needed
- **Configuration Updates**: Required config file changes
- **Dependency Updates**: Package or version updates needed
- **Documentation Updates**: Any docs that need updating

### 6. Prevention Strategies

- **Testing Improvements**: Suggest additional tests to catch similar issues
- **CI/CD Enhancements**: Workflow improvements to prevent future failures
- **Code Quality**: Code review or quality gate recommendations
- **Monitoring**: Suggest monitoring or alerting improvements

### 7. Reproduction Steps

Provide clear steps to:

- **Reproduce the Issue**: How to recreate the failure locally
- **Verify the Fix**: How to test that the proposed solution works
- **Test Scenarios**: Edge cases and scenarios to test

### 8. Technical Details

- **Dependencies**: List all relevant dependencies and versions
- **Environment Variables**: Required env vars and their values
- **Configuration Files**: Relevant config files and their contents
- **Build/Deploy Commands**: Commands used in the failing process

### 9. Additional Resources

- **Related Issues**: Links to similar GitHub issues
- **Documentation**: Relevant docs or guides
- **Community Discussions**: Stack Overflow or forum discussions
- **Best Practices**: Industry best practices for the identified issue

## Output Format

Please structure your analysis as a professional bug report that includes:

1. **Executive Summary** (2-3 sentences)
2. **Technical Analysis** (detailed findings)
3. **Action Items** (prioritized list of fixes)
4. **Verification Plan** (how to confirm fixes work)

## Additional Instructions

- Use clear, professional language suitable for template authors
- Include code snippets where relevant
- Provide specific file paths and line numbers when possible
- Suggest both quick fixes and long-term improvements
- Consider the impact on template users
- Include any security or performance implications

## Template for Report Output

```markdown
# GitHub Action Failure Analysis Report

## Executive Summary
[Brief overview of the issue and impact]

## Failure Details
**Repository**: Azure/ai-app-templates
**Action Run**: [URL]
**Template**: [Template name]
**Failure Type**: [Type]
**Severity**: [Level]

## Root Cause
[Detailed explanation of what went wrong]

## Error Analysis
[Specific errors and their context]

## Recommended Fixes
### Immediate Actions
1. [Fix 1]
2. [Fix 2]

### Long-term Improvements
1. [Improvement 1]
2. [Improvement 2]

## Code Changes Required
[Specific code modifications with examples]

## Testing Recommendations
[How to test the fixes]

## Prevention Measures
[How to avoid similar issues in the future]
```

---

**Note**: Please access the GitHub Action logs directly and perform a thorough analysis based on the actual failure details found in the logs.
