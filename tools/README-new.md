# GitHub Issues Analysis Tools

This directory contains tools for analyzing GitHub issues in the Azure Developer CLI repository.

## Quick Start

### Prerequisites
1. **Python 3.7+** with `requests` library installed
2. **GitHub Personal Access Token** with `public_repo` permissions

### Get a GitHub Token
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select `public_repo` scope for public repositories
4. Copy the generated token

### Option 1: Run Both Reports (Recommended)

**Windows:**
```bash
cd /d/prompts/github-issues-project/tools
set GITHUB_TOKEN=your_token_here
run_analysis.bat
```

**Linux/macOS:**
```bash
cd /d/prompts/github-issues-project/tools
export GITHUB_TOKEN="your_token_here"
./run_analysis.sh
```

### Option 2: Manual Command Line

**Generate both comprehensive and open-only reports:**
```bash
python run_queries.py --token "your_token_here" --both-reports --enrich
```

**Generate only comprehensive report (all issues):**
```bash
python run_queries.py --token "your_token_here" --enrich
```

**Generate only open issues report:**
```bash
python run_queries.py --token "your_token_here" --open-only --enrich
```

## Output Files

### Reports (in ../reports/)
- `comprehensive-issues-analysis.md` - Analysis of all issues (open + closed)
- `open-issues-analysis.md` - Analysis of only open issues

### Raw Data (in ./data/raw-data/)
- `*_all_issues.json` - Complete issue data for all issues
- `*_open_only.json` - Complete issue data for open issues only
- `*_summary.csv` - Spreadsheet-friendly summaries

## Report Sections

Both reports include:

1. **Executive Summary** - Key findings and metrics
2. **Usage Tracking Analysis** - How azd tracks client usage (desktop, GitHub Actions, etc.)
3. **Detailed Category Analysis** - Authentication, environment management, templates, etc.
4. **Temporal Analysis** - Issue trends over time
5. **Community Engagement** - Most commented and reacted issues
6. **Strategic Recommendations** - Prioritized action items
7. **Implementation Roadmap** - Timeline for improvements

## Comparison: All Issues vs. Open Issues

### Comprehensive Report (All Issues)
- **Purpose:** Historical analysis and trend understanding
- **Use Case:** Strategic planning, pattern recognition
- **Includes:** All issues ever created (open + closed)
- **Best For:** Understanding what has been resolved and overall project health

### Open Issues Report
- **Purpose:** Current priorities and immediate action items
- **Use Case:** Sprint planning, immediate problem-solving
- **Includes:** Only currently open issues
- **Best For:** Understanding current pain points and workload

## Command Line Options

```
python run_queries.py [OPTIONS]

Required:
  --token TOKEN          GitHub personal access token

Optional:
  --both-reports         Generate both comprehensive and open-only reports
  --open-only           Analyze only open issues (single report mode)
  --enrich              Include detailed issue data (slower but more complete)
  --output-dir DIR      Output directory for raw data (default: ./data/raw-data)
  --repo-owner OWNER    Repository owner (default: Azure)
  --repo-name NAME      Repository name (default: azure-dev)
```

## Rate Limiting

The script implements conservative rate limiting:
- 1 request per second (3,600 requests/hour)
- GitHub allows 5,000 requests/hour for authenticated users
- Analysis typically requires 200-500 requests depending on repository size

## Configuration

Edit `config.yaml` to customize:
- Query parameters
- Output formats
- Rate limiting settings
- Analysis categories

## Troubleshooting

### Common Issues

1. **"Rate limit exceeded"**
   - Wait and try again
   - The script automatically handles rate limiting

2. **"Authentication failed"**
   - Check your GitHub token
   - Ensure token has `public_repo` permissions

3. **"Repository not found"**
   - Verify repository owner/name
   - Check if repository is public

4. **"Empty results"**
   - Repository might have no issues matching the queries
   - Check if repository exists and has issues

### Getting Help

If you encounter issues:
1. Check the error messages for specific guidance
2. Verify your GitHub token permissions
3. Ensure Python and required packages are installed
4. Try running with `--verbose` flag for detailed logging

## Examples

### Analysis for Different Repositories
```bash
# Analyze different repository
python run_queries.py --token "token" --repo-owner "microsoft" --repo-name "vscode" --both-reports

# Quick analysis without enrichment (faster)
python run_queries.py --token "token" --both-reports

# Only get high-engagement issues
python run_queries.py --token "token" --open-only
```

### Using Environment Variables
```bash
# Set token once
export GITHUB_TOKEN="your_token_here"

# Run multiple analyses
python run_queries.py --both-reports --enrich
python run_queries.py --open-only --enrich --repo-name "azure-cli"
```

---

**Created by:** GitHub Issues Analysis Framework
**Updated:** July 21, 2025
