import json

with open('semgrep-results.json') as f:
    data = json.load(f)

critical_issues = [res for res in data.get("results", []) if res["severity"].lower() == "error"]

if critical_issues:
    print(" Deployment blocked: Critical vulnerabilities found.")
    exit(1)
else:
    print("No critical issues.")
    exit(0)
