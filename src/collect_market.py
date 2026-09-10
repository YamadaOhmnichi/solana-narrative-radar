#!/usr/bin/env python3
"""Market-signal collector: CoinGecko category trends for the Solana ecosystem."""
import json, urllib.request, urllib.parse

def http(url):
    req = urllib.request.Request(url, headers={"User-Agent": "solana-narrative-radar/0.1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

SOLANA_CATEGORIES = ["solana-meme-coins", "solana-ecosystem", "pump-fun-ecosystem"]

def collect():
    out = {}
    for cat in SOLANA_CATEGORIES:
        try:
            d = http("https://api.coingecko.com/api/v3/coins/markets?"
                     + urllib.parse.urlencode({
                         "vs_currency": "usd", "category": cat,
                         "order": "market_cap_desc", "per_page": 10, "page": 1,
                         "price_change_percentage": "24h,7d,30d"}))
            out[cat] = [{
                "id": c["id"], "symbol": c["symbol"], "name": c["name"],
                "market_cap": c.get("market_cap"), "rank": c.get("market_cap_rank"),
                "chg_24h": c.get("price_change_percentage_24h_in_currency"),
                "chg_7d": c.get("price_change_percentage_7d_in_currency"),
                "chg_30d": c.get("price_change_percentage_30d_in_currency"),
                "volume_mcap_ratio": round((c.get("total_volume") or 0) / (c.get("market_cap") or 1), 3),
            } for c in d]
        except Exception as e:
            print("category failed:", cat, e)
    return out

if __name__ == "__main__":
    out = collect()
    json.dump(out, open("data/market.json", "w"), indent=1)
    for cat, rows in out.items():
        print(cat, "top:", [(r["symbol"], r["chg_7d"]) for r in rows[:3]])
