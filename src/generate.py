#!/usr/bin/env python3
"""Generate report.md and a self-contained dashboard.html from narratives."""
import json, os, html
from analyze import analyze
from ideas import ideas_for

REPOS = json.load(open("data/github_repos.json"))
ONCHAIN = json.load(open("data/onchain.json"))
THREATS = json.load(open("data/threats.json"))
MARKET = json.load(open("data/market.json"))
NEWS = json.load(open("data/news.json"))
RESULT = analyze(REPOS, MARKET, NEWS)
json.dump(RESULT, open("data/narratives.json", "w"), indent=1)

def esc(s): return html.escape(str(s))

# ---------- report.md ----------
lines = []
lines.append("# Solana Narrative Radar — Fortnightly Report")
lines.append("")
lines.append(f"Generated: {RESULT['generated_at']}  |  Methodology v{RESULT['methodology_version']}")
lines.append("")
lines.append("## On-chain context (live, public RPC)")
lines.append("")
oc = ONCHAIN or {}
lines.append(f"- Network throughput: **{oc.get('tps_avg')} TPS avg** (30 recent samples, non-vote share tracked)  ")
lines.append(f"- TPS trend across samples: **{oc.get('tps_trend_pct')}%**  ")
lines.append(f"- Solana core: **{oc.get('version')}**")
lines.append("")
lines.append("## Detected Narratives (ranked)")
lines.append("")
for i, n in enumerate(RESULT["narratives"][:8], 1):
    ev = n["evidence"]
    lines.append(f"### {i}. {n['narrative']}  —  confidence: {n['confidence']}  (score {n['score']})")
    lines.append("")
    lines.append(f"- GitHub repos matching: **{ev['github_repos']}**  (top velocity {ev['github_top_velocity']} stars/day)")
    lines.append(f"- Headline mentions (last fortnight): **{ev['headline_hits']}**")
    if ev.get("market_avg_7d_pct") is not None:
        lines.append(f"- Market 7d avg change: **{ev['market_avg_7d_pct']}%**")
    lines.append(f"- Cross-source confirmation: **{ev['sources_confirming']}/3**")
    if ev.get("sample_headlines"):
        lines.append("")
        lines.append("  Sample headlines:")
        for h in ev["sample_headlines"]:
            lines.append(f"  - {h}")
    lines.append("")
    lines.append("  Top repos:")
    for m in n["member_repos"][:3]:
        lines.append(f"  - [{m['full_name']}]({m['url']}) — {m['stars_per_day']} stars/day")
    lines.append("")
    lines.append("  **Build ideas:**")
    for idea in ideas_for(n, 3):
        lines.append(f"  - {idea}")
    lines.append("")
open("report.md", "w").write("\n".join(lines))
print("wrote report.md")

# ---------- dashboard.html ----------
def bar(score, maxs):
    w = max(2, int(220 * score / maxs))
    return f'<div class="bar" style="width:{w}px"></div>'

maxs = max([n["score"] for n in RESULT["narratives"]] + [1])
cards = []
for n in RESULT["narratives"][:8]:
    ev = n["evidence"]
    ideas_html = "".join(f"<li>{esc(a)}</li>" for a in ideas_for(n, 3))
    heads = "".join(f"<li class='head'>{esc(h)}</li>" for h in ev.get("sample_headlines", [])[:3])
    cards.append(f"""
    <div class="card">
      <div class="card-head">
        <span class="name">{esc(n['narrative'])}</span>
        <span class="conf conf-{esc(n['confidence'].lower())}">{esc(n['confidence'])}</span>
      </div>
      <div class="score">{esc(n['score'])} {bar(n['score'], maxs)}</div>
      <div class="ev">
        <span>{ev['github_repos']} repos</span> ·
        <span>{ev['github_top_velocity']}★/d</span> ·
        <span>{ev['headline_hits']} headlines</span> ·
        <span>{ev['sources_confirming']}/3 sources</span>
      </div>
      {('<ul class="heads">'+heads+'</ul>') if heads else ''}
      <div class="ideas"><b>Build ideas</b><ul>{ideas_html}</ul></div>
    </div>""")

html_doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Solana Narrative Radar</title>
<style>
 body{{font-family:-apple-system,Segoe UI,Roboto,sans-serif;margin:0;background:#0b0e14;color:#e6e9ef;padding:32px}}
 h1{{color:#14f195;font-size:26px}} .sub{{color:#8b94a7;margin-bottom:24px}}
 .onchain{{display:flex;flex-wrap:wrap;gap:14px;background:#101522;border:1px solid #232b3a;border-radius:12px;padding:14px 18px;margin-bottom:22px;font-size:13px;color:#b9c0cf}}
 .onchain b{{color:#14f195}} .onchain .warn{{color:#f5a623}}
 .card{{background:#141925;border:1px solid #232b3a;border-radius:12px;padding:18px}}
 .card-head{{display:flex;justify-content:space-between;align-items:center}}
 .name{{font-weight:700;font-size:16px}} .conf{{font-size:12px;padding:2px 8px;border-radius:6px}}
 .conf-high{{background:#14f19522;color:#14f195}} .conf-medium{{background:#f5a62322;color:#f5a623}}
 .conf-low{{background:#e5484d22;color:#e5484d}}
 .score{{display:flex;align-items:center;gap:8px;color:#9945ff;font-weight:700;margin:8px 0}}
 .bar{{height:8px;background:linear-gradient(90deg,#9945ff,#14f195);border-radius:4px}}
 .ev{{color:#8b94a7;font-size:13px;margin:6px 0}}
 .heads,.ideas ul{{margin:6px 0;padding-left:18px;font-size:13px;color:#b9c0cf}}
 .heads li.head{{color:#f5a623;font-style:italic}} .ideas b{{color:#14f195}}
</style></head><body>
<h1>Solana Narrative Radar</h1>
<div class="sub">Fortnightly autonomous trend detection · generated {esc(RESULT['generated_at'])} · v{esc(RESULT['methodology_version'])}</div>
<div class="onchain">
 <span>Live network: <b>{esc(ONCHAIN.get('tps_avg'))} TPS avg</b> (30 RPC samples)</span>
 <span>TPS trend: <b>{esc(ONCHAIN.get('tps_trend_pct'))}%</b></span>
 <span>Core: <b>{esc(ONCHAIN.get('version'))}</b></span>
 <span>Trust gate: <b>{len(REPOS)} legit</b> repos · <span class="warn">{len(THREATS)} flagged threats</span> excluded from signals</span>
</div>
<div class="grid">{''.join(cards)}</div>
</body></html>"""
open("dashboard.html", "w").write(html_doc)
print("wrote dashboard.html")
