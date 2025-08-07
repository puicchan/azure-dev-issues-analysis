# PowerShell/pwsh Issues Analysis - Azure Developer CLI

**Report Generated:** August 06, 2025  
**Total Issues Analyzed:** 46  
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

**Issues in this category:** 3

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#4982](https://github.com/Azure/azure-dev/issues/4982) | [Issue] postdeploy hook is unable to find pwsh even though it is installed and i... | 2025-03-25 | 133 | 1 | High |  |
| [#4653](https://github.com/Azure/azure-dev/issues/4653) | [Issue] Failed to deploy app when app name too long or different app name has sa... | 2024-12-26 | 223 | 1 | High | compose |
| [#4560](https://github.com/Azure/azure-dev/issues/4560) | [Issue] warn users when they need to install powershell 7 (or fallback to powers... | 2024-11-15 | 264 | 1 | High | error handling, ux improvements, hooks |

### 2. PowerShell 7 Installation and Detection Issues

Issues related to detecting PowerShell 7 installation and providing guidance to users.

**Issues in this category:** 5

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#3037](https://github.com/Azure/azure-dev/issues/3037) | [Issue] azd pipeline config for azdo fails "ERROR: ensuring git remote: Looking ... | 2023-11-29 | 615 | 20 | Medium | enhancement, question, azdo, pipelines, customer-reported |
| [#2640](https://github.com/Azure/azure-dev/issues/2640) | `azd pipeline config` login issues | 2023-08-17 | 719 | 8 | High | bug, azdo, pipelines, authn |
| [#4592](https://github.com/Azure/azure-dev/issues/4592) | [Issue] Powershell scripts should be executed with the -NoProfile switch | 2024-11-27 | 252 | 3 | Low | question, customer-reported |
| [#4714](https://github.com/Azure/azure-dev/issues/4714) | [Issue] Installing 1.11.1 returns as version 1.10.1 | 2025-01-21 | 196 | 1 | Low | question, customer-reported |
| [#5453](https://github.com/Azure/azure-dev/issues/5453) | PowerShell 7 suggestion text not showing for service-level hooks | 2025-07-08 | 28 | 0 | Medium | error handling, ux improvements, hooks |

### 3. Hook Execution Failures

Issues where Azure DevOps hooks fail due to PowerShell version mismatches or missing installations.

**Issues in this category:** 5

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#4844](https://github.com/Azure/azure-dev/issues/4844) | AZD deploy getting stuck on (Uploading deployment package) as of 2024/02/24 | 2025-02-25 | 162 | 10 | Low | question, needs-triage, customer-reported, app service |
| [#4382](https://github.com/Azure/azure-dev/issues/4382) | [Issue] `azd hooks run` not respecting `interactive` configuration | 2024-09-26 | 313 | 7 | High | bug, hooks |
| [#3613](https://github.com/Azure/azure-dev/issues/3613) | [Issue/enhancement] Cross-platform shell commands behavior | 2024-03-28 | 496 | 2 | Medium | enhancement, extensibility, hooks |
| [#3344](https://github.com/Azure/azure-dev/issues/3344) | predeploy hook not triggering | 2024-02-12 | 540 | 1 | Medium | blocker, regression, extensibility |
| [#3006](https://github.com/Azure/azure-dev/issues/3006) | Packaging error: The "fileName" or "name" properties of emitted chunks and asset... | 2023-11-20 | 624 | 0 | High | bug, command, core |

### 4. Missing PowerShell 7 Suggestion Text

Issues where the system should show helpful suggestions for installing PowerShell 7 but doesn't.

**Issues in this category:** 1

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#4032](https://github.com/Azure/azure-dev/issues/4032) | Getting Started UX Improvements | 2024-06-21 | 410 | 2 | Medium | pm, user-study, ux improvements, ux impact |


### 5. General PowerShell-Related Issues

Other PowerShell-related issues that don't fit into the specific categories above.

**Issues in this category:** 16

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#4384](https://github.com/Azure/azure-dev/issues/4384) | A standard or better way to populate local environments with azd env variables | 2024-09-27 | 312 | 22 | Medium | feature, hooks |
| [#4107](https://github.com/Azure/azure-dev/issues/4107) | Fail to start api and web  | 2024-07-11 | 391 | 7 | Medium | templates |
| [#3397](https://github.com/Azure/azure-dev/issues/3397) | Conditional package/deploy a service | 2024-02-19 | 534 | 4 | Medium | command, extensibility, core |
| [#3193](https://github.com/Azure/azure-dev/issues/3193) | [Issue] azd package hangs(?) when host is container app | 2024-01-11 | 573 | 4 | Low | command, question, customer-reported, core |
| [#4429](https://github.com/Azure/azure-dev/issues/4429) | [Issue] WinGet upgrade does not have 1.10.2 | 2024-10-11 | 299 | 3 | Medium | engsys, upstream deps |
| [#4062](https://github.com/Azure/azure-dev/issues/4062) | [Issue] Docker buildargs does not support interpolation | 2024-07-03 | 399 | 3 | Medium | enhancement, aca |
| [#2846](https://github.com/Azure/azure-dev/issues/2846) | [Issue] Running `azd completion <shell> --help` does not print help related to i... | 2023-10-09 | 667 | 3 | Medium | enhancement, command, question, customer-reported, needs-team-attention, core |
| [#4031](https://github.com/Azure/azure-dev/issues/4031) | Installing azd on Windows Server using normal Windows PowerShell (non-admin) fai... | 2024-06-21 | 411 | 2 | Low | engsys, question, installer, customer-reported |
| [#3882](https://github.com/Azure/azure-dev/issues/3882) | [Issue]When `azd auth login`, x509 error occured in WSL(ERROR: logging in: faile... | 2024-05-09 | 454 | 2 | Low | question, needs-author-feedback, customer-reported, core, authn |
| [#3210](https://github.com/Azure/azure-dev/issues/3210) | [Issue] The typescript linting is stricter than the source code | 2024-01-19 | 564 | 2 | Medium | templates |
| [#2635](https://github.com/Azure/azure-dev/issues/2635) | ERROR: logging in: failed to authenticate: failed to decrypt data: Key not valid... | 2023-08-16 | 721 | 2 | Low | question, customer-reported |
| [#2555](https://github.com/Azure/azure-dev/issues/2555) | core/host/functions.bicep - 'dotnetcore' is not a valid value for FUNCTIONS_WORK... | 2023-07-20 | 748 | 2 | High | bug, functions, Bicep, hacktoberfest |
| [#4837](https://github.com/Azure/azure-dev/issues/4837) | compose: cosmos db - containers | 2025-02-21 | 165 | 1 | Medium | discuss |
| [#3992](https://github.com/Azure/azure-dev/issues/3992) | [Issue] azd up for azd-aistudio-starter have different result in github workflow | 2024-06-11 | 421 | 1 | Medium | templates, Bicep, ai |
| [#2684](https://github.com/Azure/azure-dev/issues/2684) | Allow for azd auth on clouds other than AzureCloud | 2023-08-31 | 705 | 1 | Low | question, customer-reported |
| [#5506](https://github.com/Azure/azure-dev/issues/5506) | [Issue] Problem deploying a simple static HTML app to SWA using azd | 2025-07-18 | 18 | 0 | Medium |  |
| [#4152](https://github.com/Azure/azure-dev/issues/4152) | [Issue] Link issue in azd -h | 2024-07-29 | 372 | 0 | High | bug, ux improvements |

---

## .NET Aspire-Specific PowerShell Issues

Issues specifically related to .NET Aspire applications and PowerShell/pwsh compatibility.

**Issues in this category:** 12

| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |
|---------|-------|---------|------------|----------|----------|--------|
| [#5201](https://github.com/Azure/azure-dev/issues/5201) | [Issue] azd Continues to Make /me Graph API Call and Prompts for Parameters in A... | 2025-05-15 | 83 | 14 | Low | question, pipelines, customer-reported, aspire |
| [#3158](https://github.com/Azure/azure-dev/issues/3158) | [WebToolsE2E][Aspire] Deploying aspire starter app using 'azd up', the status of... | 2023-12-22 | 593 | 8 | Low | question, customer-reported, aspire |
| [#3850](https://github.com/Azure/azure-dev/issues/3850) | [Issue] azd deploy fails in azdo build pipeline when connection string value is ... | 2024-05-03 | 459 | 11 | Low | question, azdo, pipelines, customer-reported, issue-addressed, aspire |
| [#3891](https://github.com/Azure/azure-dev/issues/3891) | [Issue] [aspire] `azd infra synth` ignored by `azd deploy` in azdo ci/cd pipelin... | 2024-05-09 | 453 | 8 | High | bug, question, pipelines, customer-reported, aspire |
| [#4739](https://github.com/Azure/azure-dev/issues/4739) | [Issue] azd provision and azd deploy Seem to Ignore AZD_INITIAL_ENVIRONMENT_CONF... | 2025-01-29 | 188 | 7 | Low | question, pipelines, customer-reported, aspire |
| [#3581](https://github.com/Azure/azure-dev/issues/3581) | [Issue] UnmatchedPrincipalType in .NET Aspire application with azd provision in ... | 2024-03-23 | 501 | 7 | Low | question, pipelines, customer-reported, issue-addressed, aspire |
| [#3705](https://github.com/Azure/azure-dev/issues/3705) | azd init errors when trying to process the web project | 2024-04-13 | 480 | 6 | Low | question, no-recent-activity, needs-author-feedback, customer-reported, needs-team-attention, aspire, easy-init |
| [#3951](https://github.com/Azure/azure-dev/issues/3951) | [WebToolsE2E][Aspire][Linux] When running the 'azd pipeline config' command, an ... | 2024-05-24 | 439 | 4 | Low | question, pipelines, customer-reported, issue-addressed, aspire |
| [#2752](https://github.com/Azure/azure-dev/issues/2752) | Create pipeline skeleton on pipeline config | 2023-09-15 | 690 | 4 | Medium | feature, pipelines, aspire |
| [#3868](https://github.com/Azure/azure-dev/issues/3868) | [WebToolsE2E][Aspire]Error "failed to add files..." pop up after run command "az... | 2024-05-07 | 456 | 3 | Medium | vs, pipelines, issue-addressed, aspire |
| [#4151](https://github.com/Azure/azure-dev/issues/4151) | [Issue] Error "panic: don't know how to prompt for type *survey.Password" on dep... | 2024-07-26 | 376 | 10 | Low | question, customer-reported, issue-addressed, aspire |
| [#3571](https://github.com/Azure/azure-dev/issues/3571) | ContainerBaseImage from azurecr.io authentication | 2024-03-21 | 502 | 1 | Low | question, customer-reported, aspire |
| [#3678](https://github.com/Azure/azure-dev/issues/3678) | [Issue] azd doesn't support args with Aspire on project.v0 resource | 2024-04-09 | 483 | 0 | Medium | enhancement, aspire |
| [#5507](https://github.com/Azure/azure-dev/issues/5507) | Broken .NET Aspire Azure CI/CD pipeline: error unmarshalling Bicep template para... | 2025-07-20 | 16 | 1 | Low | question, customer-reported |

---

## Key Findings and Recommendations

### 1. Root Cause Analysis

The primary issue is that when hooks have scripts that use/expect `pwsh` (PowerShell 7) and Windows users only have PowerShell 5.1 (`powershell.exe`) installed, this causes a frustrating experience that blocks progress.

- Users try to run hooks that specify `shell: pwsh`
- Templates assume PowerShell 7 is available
- Error messages don't clearly explain the problem or solution

### 2. Impact Assessment

- **Total PowerShell-related issues:** 46
- **Critical "pwsh not recognized" issues:** 3
- **PowerShell 7 installation/detection issues:** 5
- **Hook failure issues:** 5
- **User experience issues:** 1
- **General PowerShell issues:** 16
- **.NET Aspire-specific issues:** 14

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

*This report supports Azure Developer CLI's strategic planning for improving PowerShell user experience.*
