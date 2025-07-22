#!/bin/bash
# GitHub Issues Analysis Runner
# This script runs both comprehensive and open-only issue analyses

echo "🚀 Azure Developer CLI Issues Analysis"
echo "======================================"

# Check if token is provided as environment variable
if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ Error: GITHUB_TOKEN environment variable not set"
    echo ""
    echo "To get a GitHub token:"
    echo "1. Go to https://github.com/settings/tokens"
    echo "2. Click 'Generate new token (classic)'"
    echo "3. Select 'public_repo' scope"
    echo "4. Copy the token and set it as an environment variable:"
    echo "   export GITHUB_TOKEN='your_token_here'"
    echo ""
    echo "Then run this script again."
    exit 1
fi

echo "✅ GitHub token found"
echo "📂 Creating output directories..."

# Create necessary directories
mkdir -p ./data/raw-data
mkdir -p ../reports

echo "🔍 Starting comprehensive GitHub issues analysis..."
echo "⏱️  This may take several minutes due to API rate limiting..."
echo ""

# Run the analysis
python run_queries.py \
    --token "$GITHUB_TOKEN" \
    --both-reports \
    --enrich \
    --output-dir "./data/raw-data"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Analysis completed successfully!"
    echo ""
    echo "📋 Generated Reports:"
    echo "  📄 Comprehensive Analysis: ../reports/comprehensive-issues-analysis.md"
    echo "  📄 Open Issues Only: ../reports/open-issues-analysis.md"
    echo ""
    echo "📊 Raw Data Files:"
    echo "  📁 Data directory: ./data/raw-data/"
    echo ""
    echo "💡 Next Steps:"
    echo "  1. Review both reports in the ../reports/ directory"
    echo "  2. Compare insights between all issues vs. open issues"
    echo "  3. Use findings to prioritize development efforts"
else
    echo ""
    echo "❌ Analysis failed. Check the error messages above."
    exit 1
fi
