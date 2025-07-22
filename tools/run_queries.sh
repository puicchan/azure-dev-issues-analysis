#!/bin/bash

# GitHub Issues Query Runner for Azure Developer CLI Analysis
# Shell script version using GitHub CLI (gh command)
#
# Prerequisites:
#   - GitHub CLI installed: https://cli.github.com/
#   - Authenticated with GitHub: gh auth login
#
# Usage:
#   ./run_queries.sh
#   ./run_queries.sh --repo Azure/azure-dev --output-dir ./data/raw-data

set -e  # Exit on any error

# Default configuration
REPO_OWNER="Azure"
REPO_NAME="azure-dev"
OUTPUT_DIR="./data/raw-data"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --repo)
            REPO="$2"
            REPO_OWNER=$(echo "$REPO" | cut -d'/' -f1)
            REPO_NAME=$(echo "$REPO" | cut -d'/' -f2)
            shift 2
            ;;
        --output-dir)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        --help)
            echo "Usage: $0 [--repo OWNER/REPO] [--output-dir DIR]"
            echo ""
            echo "Options:"
            echo "  --repo         Repository in format owner/repo (default: Azure/azure-dev)"
            echo "  --output-dir   Output directory for results (default: ./data/raw-data)"
            echo "  --help         Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check prerequisites
check_prerequisites() {
    print_status "Checking prerequisites..."
    
    # Check if gh is installed
    if ! command -v gh &> /dev/null; then
        print_error "GitHub CLI (gh) is not installed"
        print_error "Install it from: https://cli.github.com/"
        exit 1
    fi
    
    # Check if user is authenticated
    if ! gh auth status &> /dev/null; then
        print_error "Not authenticated with GitHub CLI"
        print_error "Run: gh auth login"
        exit 1
    fi
    
    print_success "Prerequisites check passed"
}

# Function to create output directory
setup_output_dir() {
    print_status "Setting up output directory: $OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"
    
    # Create subdirectories for different query types
    mkdir -p "$OUTPUT_DIR/core"
    mkdir -p "$OUTPUT_DIR/category"
    mkdir -p "$OUTPUT_DIR/temporal"
    mkdir -p "$OUTPUT_DIR/engagement"
    mkdir -p "$OUTPUT_DIR/combined"
}

# Function to run a query and save results
run_query() {
    local query_name="$1"
    local query="$2"
    local output_subdir="$3"
    local sort_option="$4"
    
    print_status "Running query: $query_name"
    echo "  Query: $query"
    
    local output_file="$OUTPUT_DIR/$output_subdir/${query_name}_${TIMESTAMP}.json"
    
    # Build the gh command
    local gh_command="gh search issues --repo $REPO_OWNER/$REPO_NAME"
    
    # Add sort option if provided
    if [[ -n "$sort_option" ]]; then
        gh_command="$gh_command --sort $sort_option"
    fi
    
    # Add the query
    gh_command="$gh_command --limit 1000 --json number,title,body,state,createdAt,updatedAt,closedAt,labels,assignees,milestone,comments,reactions,url"
    
    # Execute the query
    if echo "$query" | $gh_command > "$output_file" 2>/dev/null; then
        local count=$(jq length "$output_file" 2>/dev/null || echo "0")
        print_success "  Retrieved $count issues -> $output_file"
        echo "$count" # Return count for summary
    else
        print_warning "  Query failed or returned no results"
        echo "0"
    fi
    
    # Add a small delay to avoid rate limiting
    sleep 1
}

# Function to run core queries
run_core_queries() {
    print_status "=== Running Core Issue Queries ==="
    
    local total=0
    
    # High engagement issues
    local count=$(run_query "high_engagement" "reactions:>5" "core" "reactions")
    total=$((total + count))
    
    # Feature requests
    count=$(run_query "feature_requests" "label:enhancement is:open" "core" "created")
    total=$((total + count))
    
    # High impact bugs
    count=$(run_query "high_impact_bugs" "label:bug reactions:>3" "core" "reactions")
    total=$((total + count))
    
    # Recent priority issues
    count=$(run_query "recent_priority" "created:>2024-01-01 reactions:>2" "core" "created")
    total=$((total + count))
    
    print_success "Core queries completed: $total total issues"
}

# Function to run category-specific queries
run_category_queries() {
    print_status "=== Running Category-Specific Queries ==="
    
    local total=0
    
    # Authentication issues
    local count=$(run_query "auth_issues" "auth OR login OR authentication in:title,body" "category" "created")
    total=$((total + count))
    
    count=$(run_query "auth_specific" "\"azd auth\" OR \"authentication failed\" OR \"login error\"" "category" "created")
    total=$((total + count))
    
    # Environment management
    count=$(run_query "env_management" "environment OR env in:title" "category" "created")
    total=$((total + count))
    
    count=$(run_query "env_specific" "\"azd env\" OR \"environment variable\" OR \"env switch\"" "category" "created")
    total=$((total + count))
    
    # Template issues
    count=$(run_query "template_issues" "template OR scaffold in:title" "category" "created")
    total=$((total + count))
    
    count=$(run_query "template_specific" "\"azd init\" OR \"template creation\" OR scaffold" "category" "created")
    total=$((total + count))
    
    # Documentation
    count=$(run_query "documentation" "documentation OR docs OR \"how to\"" "category" "created")
    total=$((total + count))
    
    # VS Code issues
    count=$(run_query "vscode_issues" "vscode OR extension in:title" "category" "created")
    total=$((total + count))
    
    # Deployment issues
    count=$(run_query "deployment_issues" "\"azd deploy\" OR \"deployment failed\" OR \"deploy error\"" "category" "created")
    total=$((total + count))
    
    count=$(run_query "provisioning" "\"azd up\" OR provisioning OR infrastructure" "category" "created")
    total=$((total + count))
    
    # Installation
    count=$(run_query "installation" "install OR setup OR \"getting started\"" "category" "created")
    total=$((total + count))
    
    # Docker issues
    count=$(run_query "docker_issues" "docker OR container OR containerization" "category" "created")
    total=$((total + count))
    
    # Azure integration
    count=$(run_query "azure_integration" "azure service OR azure integration OR azure resource" "category" "created")
    total=$((total + count))
    
    print_success "Category queries completed: $total total issues"
}

# Function to run temporal queries
run_temporal_queries() {
    print_status "=== Running Temporal Analysis Queries ==="
    
    local total=0
    
    # Quarterly analysis for 2024
    local count=$(run_query "q1_2024" "created:2024-01-01..2024-03-31" "temporal" "created")
    total=$((total + count))
    
    count=$(run_query "q2_2024" "created:2024-04-01..2024-06-30" "temporal" "created")
    total=$((total + count))
    
    count=$(run_query "q3_2024" "created:2024-07-01..2024-09-30" "temporal" "created")
    total=$((total + count))
    
    count=$(run_query "q4_2024" "created:2024-10-01..2024-12-31" "temporal" "created")
    total=$((total + count))
    
    # 2025 quarters
    count=$(run_query "q1_2025" "created:2025-01-01..2025-03-31" "temporal" "created")
    total=$((total + count))
    
    count=$(run_query "q2_2025" "created:2025-04-01..2025-06-30" "temporal" "created")
    total=$((total + count))
    
    # Recently closed
    count=$(run_query "recently_closed" "is:closed closed:>2024-06-01" "temporal" "updated")
    total=$((total + count))
    
    # Long standing open issues
    count=$(run_query "long_standing" "is:open created:<2024-01-01" "temporal" "created")
    total=$((total + count))
    
    print_success "Temporal queries completed: $total total issues"
}

# Function to run engagement queries
run_engagement_queries() {
    print_status "=== Running Engagement Analysis Queries ==="
    
    local total=0
    
    # Most commented
    local count=$(run_query "most_commented" "comments:>10" "engagement" "comments")
    total=$((total + count))
    
    # Most reacted
    count=$(run_query "most_reacted" "reactions:>10" "engagement" "reactions")
    total=$((total + count))
    
    # Recently updated
    count=$(run_query "recently_updated" "updated:>2024-06-01" "engagement" "updated")
    total=$((total + count))
    
    print_success "Engagement queries completed: $total total issues"
}

# Function to combine all results
combine_results() {
    print_status "=== Combining Results ==="
    
    local combined_file="$OUTPUT_DIR/combined/all_queries_${TIMESTAMP}.json"
    local summary_file="$OUTPUT_DIR/combined/summary_${TIMESTAMP}.csv"
    
    # Create a combined JSON file
    echo "{" > "$combined_file"
    
    local first=true
    for subdir in core category temporal engagement; do
        for file in "$OUTPUT_DIR/$subdir"/*.json; do
            if [[ -f "$file" ]]; then
                local basename=$(basename "$file" .json | cut -d'_' -f1-2)
                
                if [[ "$first" = true ]]; then
                    first=false
                else
                    echo "," >> "$combined_file"
                fi
                
                echo "  \"$basename\": " >> "$combined_file"
                cat "$file" >> "$combined_file"
            fi
        done
    done
    
    echo "}" >> "$combined_file"
    
    print_success "Combined results saved to: $combined_file"
    
    # Create summary CSV
    create_summary_csv "$summary_file"
}

# Function to create summary CSV
create_summary_csv() {
    local summary_file="$1"
    
    print_status "Creating summary CSV..."
    
    # CSV header
    echo "query_source,number,title,state,created_at,updated_at,closed_at,labels,assignees,comments_count,reactions_total,reactions_plus_one,reactions_heart,reactions_rocket,url" > "$summary_file"
    
    # Process all JSON files
    for subdir in core category temporal engagement; do
        for file in "$OUTPUT_DIR/$subdir"/*.json; do
            if [[ -f "$file" ]]; then
                local query_name=$(basename "$file" .json | cut -d'_' -f1-2)
                
                # Use jq to convert JSON to CSV rows
                jq -r --arg query "$query_name" '
                    .[] | [
                        $query,
                        .number,
                        (.title | gsub(","; ";")),
                        .state,
                        .createdAt,
                        .updatedAt,
                        .closedAt,
                        ([.labels[]?.name] | join(";")),
                        ([.assignees[]?.login] | join(";")),
                        .comments,
                        .reactions.total_count,
                        .reactions["+1"],
                        .reactions.heart,
                        .reactions.rocket,
                        .url
                    ] | @csv
                ' "$file" >> "$summary_file" 2>/dev/null || true
            fi
        done
    done
    
    print_success "Summary CSV saved to: $summary_file"
}

# Function to generate analysis report
generate_report() {
    print_status "=== Generating Analysis Report ==="
    
    local report_file="$OUTPUT_DIR/analysis_report_${TIMESTAMP}.md"
    
    cat > "$report_file" << EOF
# GitHub Issues Analysis Report

**Repository**: $REPO_OWNER/$REPO_NAME  
**Analysis Date**: $(date)  
**Output Directory**: $OUTPUT_DIR  

## Query Results Summary

EOF
    
    # Count issues in each category
    for subdir in core category temporal engagement; do
        echo "### ${subdir^} Queries" >> "$report_file"
        echo "" >> "$report_file"
        
        for file in "$OUTPUT_DIR/$subdir"/*.json; do
            if [[ -f "$file" ]]; then
                local query_name=$(basename "$file" .json | cut -d'_' -f1-2)
                local count=$(jq length "$file" 2>/dev/null || echo "0")
                echo "- **$query_name**: $count issues" >> "$report_file"
            fi
        done
        echo "" >> "$report_file"
    done
    
    cat >> "$report_file" << EOF

## Files Generated

- **Raw Data**: Individual JSON files in subdirectories
- **Combined Data**: \`combined/all_queries_${TIMESTAMP}.json\`
- **Summary CSV**: \`combined/summary_${TIMESTAMP}.csv\`
- **This Report**: \`analysis_report_${TIMESTAMP}.md\`

## Next Steps

1. Review the summary CSV for high-level patterns
2. Use the combined JSON for detailed analysis
3. Follow the analysis templates in the \`analysis/\` directory
4. Generate actionable recommendations based on findings

---

*Report generated by GitHub Issues Query Runner*
EOF
    
    print_success "Analysis report saved to: $report_file"
}

# Main execution function
main() {
    echo "=== GitHub Issues Analysis Query Runner ==="
    echo "Repository: $REPO_OWNER/$REPO_NAME"
    echo "Output Directory: $OUTPUT_DIR"
    echo "Timestamp: $TIMESTAMP"
    echo "================================================"
    
    # Check prerequisites
    check_prerequisites
    
    # Setup output directory
    setup_output_dir
    
    # Run all query categories
    run_core_queries
    run_category_queries
    run_temporal_queries
    run_engagement_queries
    
    # Combine results
    combine_results
    
    # Generate report
    generate_report
    
    print_success "✅ Analysis complete!"
    print_status "📁 Results are available in: $OUTPUT_DIR"
    print_status "📊 Start with the summary CSV for an overview"
    print_status "🔍 Use individual JSON files for detailed analysis"
}

# Handle Ctrl+C gracefully
trap 'print_warning "\n⚠️  Analysis interrupted by user"; exit 1' INT

# Run main function
main "$@"
