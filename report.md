# Solana Narrative Radar — Fortnightly Report

Generated: 2026-10-31T05:43:56+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 252.6)

- GitHub repos matching: **46**  (top velocity 188.55 stars/day)
- Headline mentions (last fortnight): **8**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours
  - The UK needs a workable route to regulated DeFi access

  Top repos:
  - [tapoooooty/hypergrad](https://github.com/tapoooooty/hypergrad) — 132.0 stars/day
  - [Piratelord54942/Telegram-Channel-Admin-rpocket](https://github.com/Piratelord54942/Telegram-Channel-Admin-rpocket) — 16.0 stars/day
  - [cxmza/windle](https://github.com/cxmza/windle) — 9.05 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 46 trading-infrastructure repos at 188.55 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (8 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Meme & Speculation  —  confidence: High  (score 193.1)

- GitHub repos matching: **13**  (top velocity 172.39 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-10.34%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [tapoooooty/hypergrad](https://github.com/tapoooooty/hypergrad) — 132.0 stars/day
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 11.22 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 8.96 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -10.34%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -10.34% so traders see which launches have real retention vs. pure rotation.

### 3. Security & Threats  —  confidence: Medium  (score 81.2)

- GitHub repos matching: **4**  (top velocity 1.2 stars/day)
- Headline mentions (last fortnight): **10**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Binance Hack Shows Why Offshore Exchanges Need US Oversight, CFTC Chair Says
  - Worried About Crypto Hacks? Buy Bitcoin Proxies in Stock Market Instead, Say Wall Street Firms
  - Binance Hack: Why Bitcoin Didn't Crash Like It Did in 2018

  Top repos:
  - [BadmonLano/meme-sniper](https://github.com/BadmonLano/meme-sniper) — 0.57 stars/day
  - [RedDuckTeam/redduck-solana-audit](https://github.com/RedDuckTeam/redduck-solana-audit) — 0.5 stars/day
  - [TodorBonchev/rust-auditor](https://github.com/TodorBonchev/rust-auditor) — 0.07 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 1.2 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (10 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 4. AI Agents on Solana  —  confidence: High  (score 69.9)

- GitHub repos matching: **24**  (top velocity 37.91 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - Capital starting to rotate back to crypto from AI: Raoul Pal
  - Intel Stock Suffers Worst Crash in 50 Years as Weak Forecast Overshadows AI Chip Demand

  Top repos:
  - [Piratelord54942/Telegram-Channel-Admin-rpocket](https://github.com/Piratelord54942/Telegram-Channel-Admin-rpocket) — 16.0 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 8.82 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 6.35 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 37.91 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in Piratelord54942/Telegram-Channel-Admin-rpocket-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 5. Wallets & UX  —  confidence: Medium  (score 37.4)

- GitHub repos matching: **13**  (top velocity 29.37 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Starknet introduces wallet privacy feature for DeFi activity

  Top repos:
  - [Piratelord54942/Telegram-Channel-Admin-rpocket](https://github.com/Piratelord54942/Telegram-Channel-Admin-rpocket) — 16.0 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 8.96 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 1.62 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 13 new wallet/onboarding repos at 29.37 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 1 this period — users clearly need guardrails).

### 6. Dev Tooling & Infra  —  confidence: Medium  (score 33.2)

- GitHub repos matching: **46**  (top velocity 33.24 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [refrax-xyz/refrax-node](https://github.com/refrax-xyz/refrax-node) — 7.67 stars/day
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 7.3 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 6.35 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 46 tooling repos at 33.24 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 7. RWA & Tokenization  —  confidence: Medium  (score 33.1)

- GitHub repos matching: **6**  (top velocity 1.15 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Mirae Asset Securities issues tokenized notes on Solana
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading

  Top repos:
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.32 stars/day
  - [CompdProtocol/compd-solana](https://github.com/CompdProtocol/compd-solana) — 0.29 stars/day
  - [CompdProtocol/compd-solana-programs](https://github.com/CompdProtocol/compd-solana-programs) — 0.2 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (6 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 8. Payments & Stablecoins  —  confidence: Medium  (score 23.8)

- GitHub repos matching: **6**  (top velocity 15.84 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain

  Top repos:
  - [Signcluengine/onchain-money-trail-analyzer](https://github.com/Signcluengine/onchain-money-trail-analyzer) — 14.0 stars/day
  - [des35swim/hood-warfare](https://github.com/des35swim/hood-warfare) — 0.94 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 0.28 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.
