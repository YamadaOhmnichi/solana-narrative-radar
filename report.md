# Solana Narrative Radar — Fortnightly Report

Generated: 2026-10-22T21:37:20+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 120.7)

- GitHub repos matching: **44**  (top velocity 48.72 stars/day)
- Headline mentions (last fortnight): **9**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours
  - Trade Where You Read: Decrypt Brings Jupiter-Powered Trading to The Information Exchange

  Top repos:
  - [cxmza/windle](https://github.com/cxmza/windle) — 16.45 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 12.88 stars/day
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 11.5 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 44 trading-infrastructure repos at 48.72 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (9 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. AI Agents on Solana  —  confidence: High  (score 63.2)

- GitHub repos matching: **22**  (top velocity 15.25 stars/day)
- Headline mentions (last fortnight): **6**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Capital starting to rotate back to crypto from AI: Raoul Pal
  - a16z Drops Crypto From Its Name, Widens Bets to AI and Frontier Tech
  - Meta Creates Non-Voting Stock to Fund AI Buildout, Keeping Zuckerberg in Control

  Top repos:
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 8.58 stars/day
  - [recogardtech/AutoPilotPM](https://github.com/recogardtech/AutoPilotPM) — 2.83 stars/day
  - [GuiBibeau/solos](https://github.com/GuiBibeau/solos) — 0.83 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 15.25 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in SpaceDataRig/space-data-rig-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 3. Meme & Speculation  —  confidence: Medium  (score 50.8)

- GitHub repos matching: **11**  (top velocity 43.12 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-3.82%**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 13.22 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 12.88 stars/day
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 11.5 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -3.82%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -3.82% so traders see which launches have real retention vs. pure rotation.

### 4. RWA & Tokenization  —  confidence: Medium  (score 32.6)

- GitHub repos matching: **3**  (top velocity 0.61 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours

  Top repos:
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.38 stars/day
  - [truenorth-lj/sofinance-public](https://github.com/truenorth-lj/sofinance-public) — 0.12 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.11 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (3 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 5. Wallets & UX  —  confidence: Medium  (score 27.7)

- GitHub repos matching: **16**  (top velocity 19.66 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Starknet introduces wallet privacy feature for DeFi activity

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 12.88 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 1.98 stars/day
  - [uni-launch/solana-token-creator](https://github.com/uni-launch/solana-token-creator) — 1.07 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 16 new wallet/onboarding repos at 19.66 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 1 this period — users clearly need guardrails).

### 6. Dev Tooling & Infra  —  confidence: Medium  (score 27.2)

- GitHub repos matching: **44**  (top velocity 27.19 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 11.5 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 8.58 stars/day
  - [Positano777/idl-drift-watch](https://github.com/Positano777/idl-drift-watch) — 2.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 44 tooling repos at 27.19 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 7. Payments & Stablecoins  —  confidence: High  (score 27.1)

- GitHub repos matching: **6**  (top velocity 3.1 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Solana Foundation hires ex-Binance CMO and payments exec as new partnerships expand
  - SoFi Launches Tokenized Deposit That Earns 4.4% and Converts to a Stablecoin

  Top repos:
  - [des35swim/hood-warfare](https://github.com/des35swim/hood-warfare) — 1.7 stars/day
  - [nirholas/papertrade-x402](https://github.com/nirholas/papertrade-x402) — 0.45 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 0.38 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. Security & Threats  —  confidence: Low  (score 8.4)

- GitHub repos matching: **3**  (top velocity 0.43 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **0/3**

  Sample headlines:
  - Drift exploiter sends $61M ETH to Tornado Cash, holds $194M

  Top repos:
  - [TodorBonchev/rust-auditor](https://github.com/TodorBonchev/rust-auditor) — 0.29 stars/day
  - [Portaudit/referee](https://github.com/Portaudit/referee) — 0.12 stars/day
  - [hypnogaba/solana-signal-trader](https://github.com/hypnogaba/solana-signal-trader) — 0.02 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.43 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (1 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.
