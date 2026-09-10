#!/usr/bin/env python3
"""Narrative detection & scoring engine.

Methodology (transparent, rule-based):
 1. Classify each GitHub repo into narrative buckets via keyword taxonomy
    (topics + description).
 2. Score bucket momentum: normalized star velocity of member repos.
 3. Cross-confirm with market data (CoinGecko category 7d momentum) and
    news headlines (keyword hits within last N days).
 4. Rank narratives by composite signal score; flag confidence by
    cross-source confirmation count (2+ sources => High).
"""
import json, re, math
from datetime import datetime, timezone

# ---- Narrative taxonomy: bucket name -> keyword regexes (checked against
# repo full_name/description/topics). Deliberately small and explainable.
TAXONOMY = {
    "AI Agents on Solana":        [r"\bai\b", r"agent", r"agenti", r"chatbot", r"llm", r"gpt", r"assistant"],
    "DePIN & Physical Infra":     [r"depin", r"iot", r"sensor", r"mesh", r"helium", r"render", r"gpu"],
    "Payments & Stablecoins":     [r"pay", r"checkout", r"invoice", r"usdc", r"usdt", r"stablecoin", r"remitt"],
    "RWA & Tokenization":         [r"rwa", r"tokeni[sz]", r"real.?world", r"treasury", r"bond", r"commodity"],
    "DeFi / Trading Infra":       [r"defi", r"swap", r"amm", r"lp", r"vault", r"yield", r"perp", r"dex", r"trading", r"bot"],
    "Consumer & Social":          [r"social", r"creator", r"nft", r"game", r"pfp", r"collect"],
    "Wallets & UX":               [r"wallet", r"onboard", r"embed", r"sdk", r"auth"],
    "Security & Threats":         [r"drainer", r"scam", r"phish", r"rug", r"exploit", r"audit", r"malware"],
    "Meme & Speculation":         [r"meme", r"pump", r"launchpad", r"airdrop", r"sniper"],
    "Dev Tooling & Infra":        [r"sdk", r"cli", r"indexer", r"rpc", r"node", r"explorer", r"anchor", r"framework"],
}

MARKET_MAP = {
    "solana-meme-coins": "Meme & Speculation",
    "solana-ecosystem":  None,  # broad; used for overall context only
}

NEWS_KEYWORDS = {
    "AI Agents on Solana":        [r"\bai agent", r"\bagent\b", r"\bai\b"],
    "Payments & Stablecoins":     [r"payment", r"stablecoin", r"usdc", r"visa", r"mastercard"],
    "DeFi / Trading Infra":       [r"defi", r"perp", r"dex", r"trading", r"vault"],
    "RWA & Tokenization":         [r"rwa", r"tokeni[sz]", r"real.?world asset"],
    "Meme & Speculation":         [r"meme", r"pump\.fun", r"fomo", r"memecoin", r"launchpad"],
    "Security & Threats":         [r"hack", r"exploit", r"drain", r"breach", r"scam", r"phish"],
    "Consumer & Social":          [r"nft", r"game", r"social"],
    "DePIN & Physical Infra":     [r"depin", r"helium", r"render"],
    "Wallets & UX":               [r"wallet", r"onboard"],
}

def _match(text, patterns):
    t = text.lower()
    return any(re.search(p, t) for p in patterns)

def classify_repos(repos):
    buckets = {name: [] for name in TAXONOMY}
    for r in repos:
        text = " ".join([r["full_name"], r.get("description") or "", " ".join(r.get("topics") or [])])
        for name, pats in TAXONOMY.items():
            if _match(text, pats):
                buckets[name].append(r)
    return buckets

def news_hits(news):
    hits = {name: [] for name in TAXONOMY}
    for feed, items in news.items():
        for it in items:
            t = it["title"]
            for name, pats in NEWS_KEYWORDS.items():
                if _match(t, pats):
                    hits[name].append(t)
    return hits

def market_momentum(market):
    mom = {}
    for cat, rows in market.items():
        nav = MARKET_MAP.get(cat)
        if not nav or not rows: continue
        vals = [r["chg_7d"] for r in rows if r.get("chg_7d") is not None]
        mom[nav] = {
            "avg_7d": round(sum(vals)/len(vals), 2) if vals else None,
            "top": rows[0]["symbol"] if rows else None,
            "top_vol_ratio": rows[0]["volume_mcap_ratio"] if rows else None,
        }
    return mom

def analyze(repos, market, news):
    buckets = classify_repos(repos)
    hits = news_hits(news)
    mom = market_momentum(market)
    narratives = []
    for name, members in buckets.items():
        if not members: continue
        gh_vel = sum(m["stars_per_day"] for m in members[:10])   # top-10 velocity
        n_hits = len(hits.get(name, []))
        mk = mom.get(name, {})
        mk_7d = mk.get("avg_7d")
        sources = sum([gh_vel > 3, n_hits >= 2, mk_7d is not None and abs(mk_7d) > 5])
        score = round(gh_vel * 1.0 + n_hits * 8 + (abs(mk_7d) * 2 if mk_7d is not None else 0), 1)
        conf = "High" if sources >= 2 else ("Medium" if sources == 1 else "Low")
        evidence = {
            "github_repos": len(members),
            "github_top_velocity": round(gh_vel, 2),
            "headline_hits": n_hits,
            "sample_headlines": hits.get(name, [])[:3],
            "market_avg_7d_pct": mk_7d,
            "sources_confirming": sources,
        }
        narratives.append({
            "narrative": name,
            "score": score,
            "confidence": conf,
            "evidence": evidence,
            "member_repos": [{"full_name": m["full_name"], "stars_per_day": m["stars_per_day"], "url": m["url"]}
                             for m in sorted(members, key=lambda x: -x["stars_per_day"])[:5]],
        })
    narratives.sort(key=lambda x: -x["score"])
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "narratives": narratives,
        "methodology_version": "0.1",
    }

if __name__ == "__main__":
    repos = json.load(open("data/github_repos.json"))
    market = json.load(open("data/market.json"))
    news = json.load(open("data/news.json"))
    result = analyze(repos, market, news)
    json.dump(result, open("data/narratives.json", "w"), indent=1)
    for n in result["narratives"][:8]:
        ev = n["evidence"]
        print(f"{n['score']:>7.1f} [{n['confidence']:<6}] {n['narrative']} "
              f"(repos={ev['github_repos']}, headlines={ev['headline_hits']}, mkt7d={ev['market_avg_7d_pct']})")
