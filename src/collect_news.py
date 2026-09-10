#!/usr/bin/env python3
"""News/RSS collector for Solana-ecosystem headlines (offchain social signal)."""
import json, re, urllib.request
import xml.etree.ElementTree as ET

# Proxy fallback: RU networks reset foreign TLS; retry through local proxy egress.
def _open_with_fallback(req, timeout=30):
    try:
        return urllib.request.urlopen(req, timeout=timeout)
    except Exception:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler(
            {"http": "http://127.0.0.1:10891", "https": "http://127.0.0.1:10891"}))
        return opener.open(req, timeout=timeout)


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
            xml = _open_with_fallback(req).read()
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
