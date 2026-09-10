# Solana Narrative Radar

**Autonomous fortnightly trend detection for the Solana ecosystem** — an AI-agent-built
tool that aggregates on-chain, developer, market and news signals, ranks emerging
narratives, and turns each one into concrete, evidence-tied build ideas.

> Built autonomously by an AI agent for the Superteam Earn agent track.
> MIT licensed. No API keys required to run.

## Live dashboard

**https://yamadaohmnichi.github.io/solana-narrative-radar/dashboard.html**

## What it does

1. **Collects** (all real, free, no keys):
   - *Developer activity* — GitHub Search API: Solana-ecosystem repos created in the
     last 60 days, scored by star velocity (stars/day) across 5 query families.
   - *Market* — CoinGecko category data (`solana-meme-coins`, `solana-ecosystem`)
     with 24h/7d/30d momentum and volume/market-cap ratios.
   - *News* — RSS (Cointelegraph Solana tag, Decrypt, DeFi tag) for off-chain
     community signal.
2. **Filters threats**: brand-impersonation and malware-pattern repos
   (`*-Drainer-Tool`, fake `MetaMask-AI`, etc.) are excluded from legit scoring and
   reported as a separate *threat signal* — scam infrastructure is itself narrative
   evidence, and mixing it into product narratives would poison the output.
3. **Detects narratives**: a small, auditable keyword taxonomy (10 buckets) classifies
   repos; each bucket is scored by `star velocity + headline hits + |market 7d|`.
4. **Ranks & annotates**: composite score + confidence from cross-source
   confirmation (2+/3 sources ⇒ High).
5. **Generates**: for each top narrative — explanation, evidence table, sample
   headlines, top repos, and **3 concrete build ideas tied to the observed signal**.

## Detected narratives (this run)

See [`report.md`](report.md) for the full ranked report. Current top signals:
Meme & Speculation momentum (pump.fun-era rotation), DeFi/trading infra build-out,
wallet-UX onboarding wave, a visible security-threat cluster (drainer repos at
high velocity), and sustained AI-agent-on-Solana builder activity.

## How signals are detected and ranked

- **Classification** — `src/analyze.py:TAXONOMY` maps topics/descriptions to 10
  narrative buckets. Deliberately small and readable so outputs are explainable.
- **Momentum** — `score = Σ(top-10 stars/day) + 8×headlines + 2×|market 7d %|`.
- **Confidence** — `sources_confirming` counts independent signal classes above
  thresholds; ≥2 ⇒ High, 1 ⇒ Medium, 0 ⇒ Low.
- **Threat split** — `src/trust.py` flags impersonators/malware before scoring.

## Run it yourself

```bash
pip install -r requirements.txt   # stdlib only — nothing required
python src/run_all.py             # collect → filter → analyze → generate
open dashboard.html               # or read report.md
```

Requires only Python 3.9+. GitHub rate limits apply without `GH_TOKEN`;
set `GH_TOKEN=...` for higher limits.

## Repo layout

```
src/collect_github.py   developer-activity collector (GitHub API)
src/collect_market.py   market momentum collector (CoinGecko)
src/collect_news.py     news collector (RSS)
src/trust.py            impostor/malware filter (signal-quality gate)
src/analyze.py          taxonomy classification + scoring
src/ideas.py            evidence-tied build-idea generation
src/generate.py         report.md + dashboard.html emitters
src/run_all.py          full pipeline entrypoint
data/*.json             raw + derived artifacts (committed for reproducibility)
```

## License

MIT
