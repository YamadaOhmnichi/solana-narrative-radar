#!/usr/bin/env python3
"""GitHub developer-activity collector for Solana Narrative Radar.
Pulls recently-created Solana-ecosystem repos and computes star velocity."""
import json, time, urllib.request
from datetime import datetime, timedelta, timezone

GH_TOKEN = None  # optional; set env GH_TOKEN for higher rate limits
QUERIES = [
    "solana created:>=",
    "solana program created:>=",
    "solana agent OR ai created:>=",
    "solana defi created:>=",
    "anchor solana created:>=",
]

def http(url, headers=None):
    h = {"User-Agent": "solana-narrative-radar/0.1", "Accept": "application/vnd.github+json"}
    if GH_TOKEN: h["Authorization"] = "token " + GH_TOKEN
    if headers: h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def collect(days=60, per_query=30):
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    repos = {}
    for q in QUERIES:
        url = ("https://api.github.com/search/repositories?q=" + urllib.parse.quote(q + since)
               + f"&sort=stars&order=desc&per_page={per_query}")
        try:
            d = http(url)
        except Exception as e:
            print("query failed:", q, e); continue
        for r in d.get("items", []):
            created = datetime.fromisoformat(r["created_at"].replace("Z", "+00:00"))
            age_days = max((datetime.now(timezone.utc) - created).days, 1)
            repos[r["full_name"]] = {
                "full_name": r["full_name"],
                "url": r["html_url"],
                "description": (r.get("description") or "")[:200],
                "stars": r["stargazers_count"],
                "created": r["created_at"],
                "language": r.get("language"),
                "stars_per_day": round(r["stargazers_count"] / age_days, 2),
                "age_days": age_days,
                "topics": r.get("topics", [])[:8],
            }
        time.sleep(2.5)  # respect search rate limit
    ranked = sorted(repos.values(), key=lambda x: -x["stars_per_day"])
    return ranked

if __name__ == "__main__":
    import urllib.parse, os, sys
    GH_TOKEN = os.environ.get("GH_TOKEN")
    out = collect()
    json.dump(out, open("data/github_repos.json", "w"), indent=1)
    print(f"collected {len(out)} repos; top 5:")
    for r in out[:5]:
        print(f"  {r['stars_per_day']:>7.2f} stars/day  {r['full_name']}")
