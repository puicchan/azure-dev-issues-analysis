# PowerShell/pwsh Issues Analysis - Azure Developer CLI

**Report Generated:** August 06, 2025  
**Total Issues Analyzed:** 46  
**Open Issues (of the 46 analyzed): 15**
**Focus:** Customer struggles with `pwsh` vs `PowerShell` when PowerShell 7 is not installed

## Summary

This report analyzes GitHub issues from the Azure Developer CLI repository related to customers struggling with PowerShell configuration, specifically issues arising when users don't have PowerShell 7 installed and encounter `pwsh` command failures.

**Key Problem Areas:**

1. **`pwsh` Command Not Recognized** - Users without PowerShell 7 getting "command not found" errors

2. **Missing PowerShell 7 Installation Guidance** - Lack of clear instructions when PS7 is required

3. **Hook Execution Failures** - Scripts failing when PowerShell 7 is expected but not available

4. **Inconsistent Error Messages** - Poor user experience when PowerShell issues occur

---

## Issue Categories

### 1. "`pwsh` Command Not Recognized" Issues

These are the most critical issues where users encounter "pwsh is not recognized" errors because they don't have PowerShell 7 installed.

**Issues in this category:** 1

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#4653](https://github.com/Azure/azure-dev/issues/4653) | [Issue] Failed to deploy app when app name too long or different app name has sa... | 2024-12-26 | 223 | 1 | High | compose |

### 2. Hook Execution Failures

Issues where Azure DevOps hooks fail due to PowerShell version mismatches or missing installations.

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#3613](https://github.com/Azure/azure-dev/issues/3613) | [Issue/enhancement] Cross-platform shell commands behavior | 2024-03-28 | 496 | 2 | Medium | enhancement, extensibility, hooks |
| [#3006](https://github.com/Azure/azure-dev/issues/3006) | Packaging error: The "fileName" or "name" properties of emitted chunks and asset... | 2023-11-20 | 624 | 0 | High | bug, command, core |

### 3. Missing PowerShell 7 Suggestion Text

Issues where the system should show helpful suggestions for installing PowerShell 7 but doesn't.

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#4032](https://github.com/Azure/azure-dev/issues/4032) | Getting Started UX Improvements | 2024-06-21 | 410 | 2 | Medium | pm, user-study, ux improvements, ux impact |

### 4. General PowerShell-Related Issues

Other PowerShell-related issues that don't fit into the specific categories above.

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#4384](https://github.com/Azure/azure-dev/issues/4384) | A standard or better way to populate local environments with azd env variables | 2024-09-27 | 312 | 22 | Medium | feature, hooks |
| [#3397](https://github.com/Azure/azure-dev/issues/3397) | Conditional package/deploy a service | 2024-02-19 | 534 | 4 | Medium | command, extensibility, core |
| [#2846](https://github.com/Azure/azure-dev/issues/2846) | [Issue] Running `azd completion <shell> --help` does not print help related to i... | 2023-10-09 | 667 | 3 | Medium | enhancement, command, question, customer-reported, needs-team-attention, core |
| [#4031](https://github.com/Azure/azure-dev/issues/4031) | Installing azd on Windows Server using normal Windows PowerShell (non-admin) fai... | 2024-06-21 | 411 | 2 | Low | engsys, question, installer, customer-reported |
| [#3210](https://github.com/Azure/azure-dev/issues/3210) | [Issue] The typescript linting is stricter than the source code | 2024-01-19 | 564 | 2 | Medium | templates |
| [#2555](https://github.com/Azure/azure-dev/issues/2555) | core/host/functions.bicep - 'dotnetcore' is not a valid value for FUNCTIONS_WORK... | 2023-07-20 | 748 | 2 | High | bug, functions, Bicep, hacktoberfest |
| [#4837](https://github.com/Azure/azure-dev/issues/4837) | compose: cosmos db - containers | 2025-02-21 | 165 | 1 | Medium | discuss |
| [#5506](https://github.com/Azure/azure-dev/issues/5506) | [Issue] Problem deploying a simple static HTML app to SWA using azd | 2025-07-18 | 18 | 0 | Medium |  |
| [#4152](https://github.com/Azure/azure-dev/issues/4152) | [Issue] Link issue in azd -h | 2024-07-29 | 372 | 0 | High | bug, ux improvements |

## .NET Aspire-Specific PowerShell Issues

Issues specifically related to .NET Aspire applications and PowerShell/pwsh compatibility.

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#5201](https://github.com/Azure/azure-dev/issues/5201) | [Issue] azd Continues to Make /me Graph API Call and Prompts for Parameters in A... | 2025-05-15 | 83 | 14 | Low | question, pipelines, customer-reported, aspire |
| [#5507](https://github.com/Azure/azure-dev/issues/5507) | Broken .NET Aspire Azure CI/CD pipeline: error unmarshalling Bicep template para... | 2025-07-20 | 16 | 1 | Low | question, customer-reported |

## Key Findings and Recommendations

### 1. Root Cause Analysis

The primary issue is that when hooks have scripts that use/expect `pwsh` (PowerShell 7) and Windows users only have PowerShell 5.1 (`powershell.exe`) installed, this causes a frustrating experience that blocks progress.

- Users try to run hooks that specify `shell: pwsh`
- Templates assume PowerShell 7 is available
- Error messages don't clearly explain the problem or solution

### 2. Impact Assessment

- **Total PowerShell-related issues (analyzed):** 46
- **Open critical "pwsh not recognized" issues:** 1
- **Open PowerShell 7 installation/detection issues:** 0
- **Open hook failure issues:** 2
- **Open user experience issues:** 1
- **Open general PowerShell issues:** 9
- **Open .NET Aspire-specific issues:** 2

### 3. Recommended Solutions

#### Immediate (High Priority)

1. **Improve Error Messages**: When `pwsh` is not found, show clear installation instructions (we've done this)
2. **Fallback Mechanism**: Attempt to use `powershell.exe` when `pwsh` is not available for compatible scripts (in progress)
3. **Detection Logic**: Implement better PowerShell version detection and guidance

#### Other considerations

1. **Template Updates**: Review templates to use appropriate PowerShell versions
2. **Documentation**: Create clear guidance on PowerShell requirements in the azd context
3. **Hooks Enhancement**: Better error handling in hook execution

### 4. Success Metrics

- Reduction in "pwsh" issues
- Improved user satisfaction (no more pwsh issues logged by customrs)
- Better template adoption rates

---

**Analysis Methodology:**

- Analyzed all GitHub issues from Azure Developer CLI repository
- Filtered for PowerShell/pwsh-related keywords and error patterns
- Categorized by issue type and severity
- Prioritized by community engagement (comments) and impact

_This report supports Azure Developer CLI's strategic planning for improving PowerShell user experience._
