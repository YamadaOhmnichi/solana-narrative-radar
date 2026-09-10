#!/usr/bin/env python3
"""Full pipeline: collect -> trust-filter -> analyze -> generate."""
import json, subprocess, sys, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for s in ["collect_github.py", "collect_market.py", "collect_news.py"]:
    subprocess.run([sys.executable, f"src/{s}"], check=False)
sys.path.insert(0, "src")
from trust import split
repos = json.load(open("data/github_repos.json"))
legit, flagged = split(repos)
json.dump(legit, open("data/github_repos.json", "w"), indent=1)
json.dump(flagged, open("data/threats.json", "w"), indent=1)
print(f"trust filter: {len(legit)} legit, {len(flagged)} flagged")
subprocess.run([sys.executable, "src/generate.py"], check=False)
