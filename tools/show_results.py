#!/usr/bin/env python3
import json

# Load the comprehensive analysis
with open('data/raw-data/comprehensive_analysis_20250721_112151.json') as f:
    data = json.load(f)

print("REAL AZURE/AZURE-DEV ANALYSIS RESULTS")
print("="*50)
print(f"Repository: {data['metadata']['repository']['full_name']}")
print(f"Total Issues Analyzed: {data['metadata']['total_issues_analyzed']}")
print(f"Open Issues: {data['metadata']['open_issues_count']}")  
print(f"Closed Issues: {data['metadata']['closed_issues_count']}")

resolution_rate = data['metadata']['closed_issues_count'] / data['metadata']['total_issues_analyzed'] * 100
print(f"Resolution Rate: {resolution_rate:.1f}%")

print("\nREAL Open Issues by Category:")
total_open = data['metadata']['open_issues_count']
for cat, count in data['categorization']['open_issues'].items():
    if count > 0:
        pct = count / total_open * 100
        print(f"   {cat}: {count} issues ({pct:.1f}%)")

print("\nMost Commented Issues:")
for i, issue in enumerate(data['top_issues']['most_commented'][:5], 1):
    title = issue['title'][:60] + "..." if len(issue['title']) > 60 else issue['title']
    print(f"   {i}. #{issue['number']}: {title} ({issue['comments']} comments)")

print("\nREAL DATA SUCCESS! Ready to update the analysis report!")
