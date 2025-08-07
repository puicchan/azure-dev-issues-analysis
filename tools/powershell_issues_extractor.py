#!/usr/bin/env python3
"""
PowerShell Issues Extractor for Azure Developer CLI
Extracts and analyzes issues related to PowerShell/pwsh struggles
"""

import json
import os
import re
from datetime import datetime
from typing import List, Dict, Any
from pathlib import Path

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Load and parse JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return {}

def is_powershell_related(issue: Dict[str, Any]) -> bool:
    """Check if an issue is related to PowerShell/pwsh problems"""
    powershell_keywords = [
        'pwsh', 'powershell', 'PowerShell', 'powershell.exe', 'pwsh.exe',
        'PowerShell 7', 'powershell 7', 'PS7', 'PS 7',
        'Expand-Archive', 'shell: pwsh'
    ]
    
    error_patterns = [
        r"pwsh.*not.*recognized",
        r"powershell.*not.*recognized", 
        r"pwsh.*not.*found",
        r"powershell.*not.*found",
        r"install.*powershell.*7",
        r"Expand-Archive.*error",
        r"fallback.*powershell",
        r"PowerShell.*suggestion",
        r"shell.*pwsh.*error"
    ]
    
    # Check title
    title = (issue.get('title') or '').lower()
    body = (issue.get('body') or '').lower()
    
    # Keyword matching
    text_to_search = f"{title} {body}"
    
    # Check for keywords
    for keyword in powershell_keywords:
        if keyword.lower() in text_to_search:
            # Additional validation for PowerShell-specific issues
            if any(pattern in text_to_search for pattern in [
                'not recognized', 'not found', 'install', 'error', 
                'fail', 'suggestion', 'hook', 'fallback'
            ]):
                return True
    
    # Check for error patterns
    for pattern in error_patterns:
        if re.search(pattern, text_to_search, re.IGNORECASE):
            return True
    
    return False

def extract_powershell_issues(data_dir: str) -> List[Dict[str, Any]]:
    """Extract PowerShell-related issues from all JSON files"""
    powershell_issues = []
    data_path = Path(data_dir)
    
    # Process all JSON files in the data directory
    json_files = list(data_path.rglob('*.json'))
    
    for json_file in json_files:
        print(f"Processing {json_file}...")
        data = load_json_file(str(json_file))
        
        if isinstance(data, list):
            # Direct list of issues
            issues = data
        elif isinstance(data, dict):
            # May be wrapped in another structure
            issues = data.get('issues', data.get('items', [data] if 'number' in data else []))
        else:
            continue
        
        for issue in issues:
            if isinstance(issue, dict) and is_powershell_related(issue):
                # Add source file info
                issue['_source_file'] = str(json_file.name)
                powershell_issues.append(issue)
    
    # Remove duplicates based on issue number
    seen_numbers = set()
    unique_issues = []
    for issue in powershell_issues:
        issue_number = issue.get('number')
        if issue_number and issue_number not in seen_numbers:
            seen_numbers.add(issue_number)
            unique_issues.append(issue)
    
    return sorted(unique_issues, key=lambda x: x.get('number', 0), reverse=True)

def calculate_age_days(created_at: str) -> int:
    """Calculate age of issue in days"""
    try:
        created = datetime.strptime(created_at.replace('Z', '+00:00'), '%Y-%m-%dT%H:%M:%S%z')
        now = datetime.now(created.tzinfo)
        return (now - created).days
    except:
        return 0

def format_labels(labels: List[Dict[str, Any]]) -> str:
    """Format labels for display"""
    if not labels:
        return ""
    return ", ".join([label.get('name', '') for label in labels])

def get_issue_severity(issue: Dict[str, Any]) -> str:
    """Determine issue severity based on labels and content"""
    labels = [label.get('name', '').lower() for label in issue.get('labels', [])]
    body = (issue.get('body') or '').lower()
    
    if 'bug' in labels or 'error' in labels:
        return "High"
    elif 'enhancement' in labels or 'feature' in labels:
        return "Medium"
    elif 'question' in labels or 'documentation' in labels:
        return "Low"
    elif 'not recognized' in body or 'not found' in body:
        return "High"
    else:
        return "Medium"

def generate_markdown_report(issues: List[Dict[str, Any]], output_file: str):
    """Generate a comprehensive markdown report"""
    
    # Group issues by category
    categories = {
        "pwsh_not_found": [],
        "ps7_missing": [],
        "hook_failures": [],
        "expand_archive": [],
        "suggestion_missing": [],
        "general_powershell": []
    }
    
    for issue in issues:
        title = (issue.get('title') or '').lower()
        body = (issue.get('body') or '').lower()
        text = f"{title} {body}"
        
        if 'not recognized' in text or 'not found' in text:
            categories["pwsh_not_found"].append(issue)
        elif 'powershell 7' in text or 'install powershell' in text:
            categories["ps7_missing"].append(issue)
        elif 'hook' in text and ('fail' in text or 'error' in text):
            categories["hook_failures"].append(issue)
        elif 'expand-archive' in text:
            categories["expand_archive"].append(issue)
        elif 'suggestion' in text and 'powershell' in text:
            categories["suggestion_missing"].append(issue)
        else:
            categories["general_powershell"].append(issue)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"""# PowerShell/pwsh Issues Analysis - Azure Developer CLI

**Report Generated:** {datetime.now().strftime('%B %d, %Y')}  
**Total Issues Analyzed:** {len(issues)}  
**Focus:** Customer struggles with `pwsh` vs `PowerShell` when PowerShell 7 is not installed

## Executive Summary

This report analyzes GitHub issues from the Azure Developer CLI repository related to customers struggling with PowerShell configuration, specifically issues arising when users don't have PowerShell 7 installed and encounter `pwsh` command failures.

**Key Problem Areas:**
1. **`pwsh` Command Not Recognized** - Users without PowerShell 7 getting "command not found" errors
2. **Missing PowerShell 7 Installation Guidance** - Lack of clear instructions when PS7 is required
3. **Hook Execution Failures** - Scripts failing when PowerShell 7 is expected but not available
4. **Inconsistent Error Messages** - Poor user experience when PowerShell issues occur

---

## Issue Categories

""")

        # Category 1: pwsh Not Found/Recognized
        f.write(f"""### 1. "`pwsh` Command Not Recognized" Issues

These are the most critical issues where users encounter "pwsh is not recognized" errors because they don't have PowerShell 7 installed.

**Issues in this category:** {len(categories["pwsh_not_found"])}

""")
        
        if categories["pwsh_not_found"]:
            f.write("| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |\n")
            f.write("|---------|-------|---------|------------|----------|----------|--------|\n")
            
            for issue in sorted(categories["pwsh_not_found"], key=lambda x: x.get('comments', 0), reverse=True):
                age = calculate_age_days(issue.get('created_at', ''))
                severity = get_issue_severity(issue)
                labels = format_labels(issue.get('labels', []))
                
                f.write(f"| [#{issue.get('number')}]({issue.get('html_url')}) | {issue.get('title', '')[:80]}{'...' if len(issue.get('title', '')) > 80 else ''} | {issue.get('created_at', '')[:10]} | {age} | {issue.get('comments', 0)} | {severity} | {labels} |\n")
        
        # Category 2: PowerShell 7 Missing
        f.write(f"""

### 2. PowerShell 7 Installation and Detection Issues

Issues related to detecting PowerShell 7 installation and providing guidance to users.

**Issues in this category:** {len(categories["ps7_missing"])}

""")
        
        if categories["ps7_missing"]:
            f.write("| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |\n")
            f.write("|---------|-------|---------|------------|----------|----------|--------|\n")
            
            for issue in sorted(categories["ps7_missing"], key=lambda x: x.get('comments', 0), reverse=True):
                age = calculate_age_days(issue.get('created_at', ''))
                severity = get_issue_severity(issue)
                labels = format_labels(issue.get('labels', []))
                
                f.write(f"| [#{issue.get('number')}]({issue.get('html_url')}) | {issue.get('title', '')[:80]}{'...' if len(issue.get('title', '')) > 80 else ''} | {issue.get('created_at', '')[:10]} | {age} | {issue.get('comments', 0)} | {severity} | {labels} |\n")

        # Category 3: Hook Failures
        f.write(f"""

### 3. Hook Execution Failures

Issues where Azure DevOps hooks fail due to PowerShell version mismatches or missing installations.

**Issues in this category:** {len(categories["hook_failures"])}

""")
        
        if categories["hook_failures"]:
            f.write("| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |\n")
            f.write("|---------|-------|---------|------------|----------|----------|--------|\n")
            
            for issue in sorted(categories["hook_failures"], key=lambda x: x.get('comments', 0), reverse=True):
                age = calculate_age_days(issue.get('created_at', ''))
                severity = get_issue_severity(issue)
                labels = format_labels(issue.get('labels', []))
                
                f.write(f"| [#{issue.get('number')}]({issue.get('html_url')}) | {issue.get('title', '')[:80]}{'...' if len(issue.get('title', '')) > 80 else ''} | {issue.get('created_at', '')[:10]} | {age} | {issue.get('comments', 0)} | {severity} | {labels} |\n")

        # Category 4: Expand-Archive Issues
        f.write(f"""

### 4. Expand-Archive Specific Issues

Issues specifically related to `Expand-Archive` command failing in `pwsh` but working in `powershell.exe`.

**Issues in this category:** {len(categories["expand_archive"])}

""")
        
        if categories["expand_archive"]:
            f.write("| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |\n")
            f.write("|---------|-------|---------|------------|----------|----------|--------|\n")
            
            for issue in sorted(categories["expand_archive"], key=lambda x: x.get('comments', 0), reverse=True):
                age = calculate_age_days(issue.get('created_at', ''))
                severity = get_issue_severity(issue)
                labels = format_labels(issue.get('labels', []))
                
                f.write(f"| [#{issue.get('number')}]({issue.get('html_url')}) | {issue.get('title', '')[:80]}{'...' if len(issue.get('title', '')) > 80 else ''} | {issue.get('created_at', '')[:10]} | {age} | {issue.get('comments', 0)} | {severity} | {labels} |\n")

        # Category 5: Missing Suggestion Text
        f.write(f"""

### 5. Missing PowerShell 7 Suggestion Text

Issues where the system should show helpful suggestions for installing PowerShell 7 but doesn't.

**Issues in this category:** {len(categories["suggestion_missing"])}

""")
        
        if categories["suggestion_missing"]:
            f.write("| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |\n")
            f.write("|---------|-------|---------|------------|----------|----------|--------|\n")
            
            for issue in sorted(categories["suggestion_missing"], key=lambda x: x.get('comments', 0), reverse=True):
                age = calculate_age_days(issue.get('created_at', ''))
                severity = get_issue_severity(issue)
                labels = format_labels(issue.get('labels', []))
                
                f.write(f"| [#{issue.get('number')}]({issue.get('html_url')}) | {issue.get('title', '')[:80]}{'...' if len(issue.get('title', '')) > 80 else ''} | {issue.get('created_at', '')[:10]} | {age} | {issue.get('comments', 0)} | {severity} | {labels} |\n")

        # Category 6: General PowerShell Issues
        f.write(f"""

### 6. General PowerShell-Related Issues

Other PowerShell-related issues that don't fit into the specific categories above.

**Issues in this category:** {len(categories["general_powershell"])}

""")
        
        if categories["general_powershell"]:
            f.write("| Issue # | Title | Created | Age (Days) | Comments | Severity | Labels |\n")
            f.write("|---------|-------|---------|------------|----------|----------|--------|\n")
            
            for issue in sorted(categories["general_powershell"], key=lambda x: x.get('comments', 0), reverse=True):
                age = calculate_age_days(issue.get('created_at', ''))
                severity = get_issue_severity(issue)
                labels = format_labels(issue.get('labels', []))
                
                f.write(f"| [#{issue.get('number')}]({issue.get('html_url')}) | {issue.get('title', '')[:80]}{'...' if len(issue.get('title', '')) > 80 else ''} | {issue.get('created_at', '')[:10]} | {age} | {issue.get('comments', 0)} | {severity} | {labels} |\n")

        # Detailed issue descriptions
        f.write("""

---

## Detailed Issue Analysis

### Most Critical Issues

""")

        # Find top issues by comment count
        top_issues = sorted(issues, key=lambda x: x.get('comments', 0), reverse=True)[:5]
        
        for i, issue in enumerate(top_issues, 1):
            f.write(f"""
#### {i}. Issue #{issue.get('number')}: {issue.get('title')}
- **URL:** {issue.get('html_url')}
- **Created:** {issue.get('created_at', '')[:10]}
- **Comments:** {issue.get('comments', 0)}
- **State:** {issue.get('state', '')}
- **Labels:** {format_labels(issue.get('labels', []))}

**Description:**
{issue.get('body', '')[:500]}{'...' if len(issue.get('body', '')) > 500 else ''}

""")

        # Summary and recommendations
        f.write(f"""

---

## Key Findings and Recommendations

### 1. Root Cause Analysis

The primary issue is that Azure Developer CLI uses `pwsh` (PowerShell 7) by default in many scenarios, but many Windows users only have PowerShell 5.1 (`powershell.exe`) installed. This creates a poor user experience when:

- Users try to run hooks that specify `shell: pwsh`
- Templates assume PowerShell 7 is available
- Error messages don't clearly explain the problem or solution

### 2. Impact Assessment

- **Total PowerShell-related issues:** {len(issues)}
- **Critical "pwsh not recognized" issues:** {len(categories["pwsh_not_found"])}
- **User experience issues:** {len(categories["suggestion_missing"])}
- **Hook failure issues:** {len(categories["hook_failures"])}

### 3. Recommended Solutions

#### Immediate (High Priority)
1. **Improve Error Messages**: When `pwsh` is not found, show clear installation instructions
2. **Fallback Mechanism**: Attempt to use `powershell.exe` when `pwsh` is not available for compatible scripts
3. **Detection Logic**: Implement better PowerShell version detection and guidance

#### Medium Term
1. **Template Updates**: Review templates to use appropriate PowerShell versions
2. **Documentation**: Create clear guidance on PowerShell requirements
3. **Hooks Enhancement**: Better error handling in hook execution

#### Long Term
1. **Cross-platform Consistency**: Standardize shell usage across platforms
2. **User Preference**: Allow users to configure preferred PowerShell version
3. **Installation Automation**: Consider auto-installing PowerShell 7 where appropriate

### 4. Success Metrics

- Reduction in "pwsh not recognized" issues
- Improved user satisfaction in onboarding
- Decreased support burden related to PowerShell configuration
- Better template adoption rates

---

**Analysis Methodology:**
- Analyzed all GitHub issues from Azure Developer CLI repository
- Filtered for PowerShell/pwsh-related keywords and error patterns
- Categorized by issue type and severity
- Prioritized by community engagement (comments) and impact

*This report supports Azure Developer CLI's strategic planning for improving PowerShell user experience.*
""")

def main():
    """Main execution function"""
    
    # Configuration
    data_dir = "data/raw-data"
    output_file = "../reports/powershell-pwsh-issues-analysis.md"
    
    print("Extracting PowerShell-related issues...")
    
    # Extract issues
    powershell_issues = extract_powershell_issues(data_dir)
    
    print(f"Found {len(powershell_issues)} PowerShell-related issues")
    
    # Generate report
    print(f"Generating report: {output_file}")
    generate_markdown_report(powershell_issues, output_file)
    
    print("Report generation completed!")
    
    # Print summary
    print(f"\nSummary:")
    print(f"- Total PowerShell issues found: {len(powershell_issues)}")
    print(f"- Report saved to: {output_file}")

if __name__ == "__main__":
    main()
