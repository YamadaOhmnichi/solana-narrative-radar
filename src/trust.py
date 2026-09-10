#!/usr/bin/env python3
"""Impostor/star-farm filter.

Brands are frequently impersonated by scam repos (e.g. 'MetaMask-AI',
'com-phantom', '*-Drainer-Tool'). A repo whose owner or name matches a
protected brand but is NOT published by the canonical org, or whose name
matches known malware patterns, is flagged impersonation-suspect and
excluded from legit narrative scoring (reported separately as a threat
signal). This raises signal quality instead of raw volume.
"""
CANONICAL = {
    "metamask": "MetaMask",
    "phantom": "phantom",
    "trustwallet": "trustwallet",
    "solana": "solana-labs",
    "solana-foundation": "solana-foundation",
    "solanafoundation": "solana-foundation",
    "solanalabs": "solana-labs",
    "jupiter": "JupiterAg",
    "raydium": "raydium-io",
    "marginedger": None,
}
MALWARE_PATTERNS = [r"drainer", r"stealer", r"grabber", r"nft-?steal", r"\brug\b.*(bot|tool)"]

def flag(repo):
    text = (repo["full_name"] + " " + (repo.get("description") or "")).lower()
    for pat in MALWARE_PATTERNS:
        import re
        if re.search(pat, text):
            return "malware-pattern"
    owner = repo["full_name"].split("/")[0].lower()
    canonical_orgs = {c.lower() for c in CANONICAL.values() if c}
    if owner in canonical_orgs:
        return None  # the canonical org itself
    for brand, canon in CANONICAL.items():
        if brand in owner and canon and owner.lower() != canon.lower():
            return "brand-impersonation"
    if repo.get("stars_per_day", 0) > 200 and repo.get("age_days", 99) <= 7:
        return "velocity-anomaly"
    return None

def split(repos):
    legit, flagged = [], []
    for r in repos:
        f = flag(r)
        (flagged if f else legit).append({**r, "flag": f} if f else r)
    return legit, flagged
