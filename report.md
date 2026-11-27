# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-27T21:18:45+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 347.6)

- GitHub repos matching: **49**  (top velocity 291.64 stars/day)
- Headline mentions (last fortnight): **7**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Bluefin to shut down perps, refocus on spot trading and tokenized RWAs
  - BNB Chain details new layer-1 for trading, private finance and AI

  Top repos:
  - [mudhinpc-droid/solana-memecoin-pump-fun-volume-booster-befalen](https://github.com/mudhinpc-droid/solana-memecoin-pump-fun-volume-booster-befalen) — 118.0 stars/day
  - [BachMason483/solana-jito-shredstream-mev-arbitrage-bot](https://github.com/BachMason483/solana-jito-shredstream-mev-arbitrage-bot) — 59.0 stars/day
  - [AsukaFerrari/gmgn-ai-bullx-neo-fast-trench-sniper-cli](https://github.com/AsukaFerrari/gmgn-ai-bullx-neo-fast-trench-sniper-cli) — 59.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 49 trading-infrastructure repos at 291.64 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (7 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Meme & Speculation  —  confidence: High  (score 302.1)

- GitHub repos matching: **19**  (top velocity 290.4 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **5.86%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [mudhinpc-droid/solana-memecoin-pump-fun-volume-booster-befalen](https://github.com/mudhinpc-droid/solana-memecoin-pump-fun-volume-booster-befalen) — 118.0 stars/day
  - [BachMason483/solana-jito-shredstream-mev-arbitrage-bot](https://github.com/BachMason483/solana-jito-shredstream-mev-arbitrage-bot) — 59.0 stars/day
  - [AsukaFerrari/gmgn-ai-bullx-neo-fast-trench-sniper-cli](https://github.com/AsukaFerrari/gmgn-ai-bullx-neo-fast-trench-sniper-cli) — 59.0 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change 5.86%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change 5.86% so traders see which launches have real retention vs. pure rotation.

### 3. Dev Tooling & Infra  —  confidence: Medium  (score 177.6)

- GitHub repos matching: **55**  (top velocity 177.56 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [BachMason483/solana-jito-shredstream-mev-arbitrage-bot](https://github.com/BachMason483/solana-jito-shredstream-mev-arbitrage-bot) — 59.0 stars/day
  - [AsukaFerrari/gmgn-ai-bullx-neo-fast-trench-sniper-cli](https://github.com/AsukaFerrari/gmgn-ai-bullx-neo-fast-trench-sniper-cli) — 59.0 stars/day
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 13.38 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 55 tooling repos at 177.56 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 4. AI Agents on Solana  —  confidence: High  (score 121.3)

- GitHub repos matching: **21**  (top velocity 97.29 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Could AI Break Bitcoin? Not Yet, Research Firm K33 Says
  - AI-Powered GTA 6 PC Ports Now Have Multiplayer as Modders Unlock 30 and 60 FPS
  - BNB Chain details new layer-1 for trading, private finance and AI

  Top repos:
  - [AsukaFerrari/gmgn-ai-bullx-neo-fast-trench-sniper-cli](https://github.com/AsukaFerrari/gmgn-ai-bullx-neo-fast-trench-sniper-cli) — 59.0 stars/day
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 13.38 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 12.75 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 97.29 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in AsukaFerrari/gmgn-ai-bullx-neo-fast-trench-sniper-cli-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 5. Wallets & UX  —  confidence: Medium  (score 120.8)

- GitHub repos matching: **21**  (top velocity 112.77 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access

  Top repos:
  - [BachMason483/solana-jito-shredstream-mev-arbitrage-bot](https://github.com/BachMason483/solana-jito-shredstream-mev-arbitrage-bot) — 59.0 stars/day
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 13.38 stars/day
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 12.75 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 21 new wallet/onboarding repos at 112.77 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 1 this period — users clearly need guardrails).

### 6. Security & Threats  —  confidence: High  (score 43.2)

- GitHub repos matching: **8**  (top velocity 3.19 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Hackers Hit US Air Force Cloud System Running Air-Defense and Munitions Data
  - Binance Fully Lifts Withdrawal Suspension Four Weeks After $6.4B Hack

  Top repos:
  - [GuiBibeau/artex-program](https://github.com/GuiBibeau/artex-program) — 1.5 stars/day
  - [getkenning/kenning](https://github.com/getkenning/kenning) — 0.94 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.2 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 3.19 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (5 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. Payments & Stablecoins  —  confidence: High  (score 24.5)

- GitHub repos matching: **7**  (top velocity 8.51 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Japan’s SBI, SMFG launch Solana venture for stablecoins, tokenization
  - Zelle picks Solana for ZelleUSD stablecoin and international payments

  Top repos:
  - [arnabbhowmik07/Ghost](https://github.com/arnabbhowmik07/Ghost) — 7.38 stars/day
  - [makedotfun/prize-escrow](https://github.com/makedotfun/prize-escrow) — 0.33 stars/day
  - [orrery-node/orrery](https://github.com/orrery-node/orrery) — 0.29 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. RWA & Tokenization  —  confidence: Medium  (score 24.4)

- GitHub repos matching: **4**  (top velocity 0.38 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Japan’s SBI, SMFG launch Solana venture for stablecoins, tokenization
  - Bluefin to shut down perps, refocus on spot trading and tokenized RWAs
  - RWA protocol stUSDT winds down 3 years after $2.3B TVL peak

  Top repos:
  - [FoundationStoneAlgorithms/TokenWork](https://github.com/FoundationStoneAlgorithms/TokenWork) — 0.22 stars/day
  - [Hymetdotfun/hymet](https://github.com/Hymetdotfun/hymet) — 0.08 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.04 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (4 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.
