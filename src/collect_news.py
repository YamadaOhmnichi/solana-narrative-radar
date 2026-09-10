#!/usr/bin/env python3
"""News/RSS collector for Solana-ecosystem headlines (offchain social signal)."""
import json, re, urllib.request
import xml.etree.ElementTree as ET

FEEDS = {
    "cointelegraph": "https://cointelegraph.com/rss/tag/solana",
    "decrypt":       "https://decrypt.co/feed",
    "cryptonews":    "https://cointelegraph.com/rss/tag/defi",
}

def collect(per_feed=12):
    out = {}
    for name, url in FEEDS.items():
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            xml = urllib.request.urlopen(req, timeout=30).read()
            root = ET.fromstring(xml)
            items = []
            for it in root.iter("item"):
                title = (it.findtext("title") or "").strip()
                pub = (it.findtext("pubDate") or "").strip()
                link = (it.findtext("link") or "").strip()
                if title:
                    items.append({"title": title, "pub": pub, "link": link})
                if len(items) >= per_feed: break
            out[name] = items
        except Exception as e:
            print("feed failed:", name, e)
    return out

if __name__ == "__main__":
    out = collect()
    json.dump(out, open("data/news.json", "w"), indent=1)
    for f, items in out.items():
        print(f, len(items), "items; latest:", items[0]["title"][:60] if items else "-")
