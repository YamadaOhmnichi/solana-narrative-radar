# Solana Narrative Radar — Fortnightly Report

Generated: 2026-10-20T11:39:27+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 116.0)

- GitHub repos matching: **48**  (top velocity 75.96 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours
  - Starknet introduces wallet privacy feature for DeFi activity

  Top repos:
  - [cxmza/windle](https://github.com/cxmza/windle) — 22.75 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 15.5 stars/day
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 14.78 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 48 trading-infrastructure repos at 75.96 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Meme & Speculation  —  confidence: High  (score 70.3)

- GitHub repos matching: **12**  (top velocity 52.48 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-8.9%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 15.5 stars/day
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 14.78 stars/day
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 14.24 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -8.9%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -8.9% so traders see which launches have real retention vs. pure rotation.

### 3. Wallets & UX  —  confidence: High  (score 57.3)

- GitHub repos matching: **19**  (top velocity 41.33 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Abandoned Bitcoin? Wallet Targeted by Noah Doe Lawsuit Moves $33 Million
  - Starknet introduces wallet privacy feature for DeFi activity

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 15.5 stars/day
  - [NuvexNetwork/nuvex](https://github.com/NuvexNetwork/nuvex) — 12.06 stars/day
  - [Janina21/Crypto-Checker](https://github.com/Janina21/Crypto-Checker) — 6.54 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 19 new wallet/onboarding repos at 41.33 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 4. Dev Tooling & Infra  —  confidence: Medium  (score 53.8)

- GitHub repos matching: **49**  (top velocity 53.8 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 14.78 stars/day
  - [NuvexNetwork/nuvex](https://github.com/NuvexNetwork/nuvex) — 12.06 stars/day
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 10.35 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 49 tooling repos at 53.8 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 5. AI Agents on Solana  —  confidence: High  (score 43.0)

- GitHub repos matching: **21**  (top velocity 26.95 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Capital starting to rotate back to crypto from AI: Raoul Pal
  - Bitcoin Tests Key Support as Oil and AI Fears Squeeze Markets

  Top repos:
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 10.35 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 9.67 stars/day
  - [recogardtech/AutoPilotPM](https://github.com/recogardtech/AutoPilotPM) — 3.24 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 26.95 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in NuvexNetwork/nuvex-services-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. RWA & Tokenization  —  confidence: Medium  (score 32.6)

- GitHub repos matching: **4**  (top velocity 0.65 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours
  - Why Some of America’s Biggest Companies Are Objecting to Tokenized Shares

  Top repos:
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.42 stars/day
  - [truenorth-lj/sofinance-public](https://github.com/truenorth-lj/sofinance-public) — 0.14 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.06 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (4 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 7. Payments & Stablecoins  —  confidence: High  (score 27.4)

- GitHub repos matching: **6**  (top velocity 3.39 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Solana Foundation hires ex-Binance CMO and payments exec as new partnerships expand
  - Mt. Gox Pushes Repayment Deadline to 2027 With $2.8B in Bitcoin Still to Distribute
  - Mastercard Brings Its Fraud-Fighting Tools to Stablecoin Payments

  Top repos:
  - [des35swim/hood-warfare](https://github.com/des35swim/hood-warfare) — 2.29 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 0.42 stars/day
  - [2274802010922/pipicachu](https://github.com/2274802010922/pipicachu) — 0.38 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. Security & Threats  —  confidence: Low  (score 9.3)

- GitHub repos matching: **4**  (top velocity 1.29 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **0/3**

  Sample headlines:
  - Hackers Are Running Apple's iOS on Android Phones for the First Time

  Top repos:
  - [TodorBonchev/rust-auditor](https://github.com/TodorBonchev/rust-auditor) — 0.6 stars/day
  - [FortuneGroot/solana-token-risk-radar](https://github.com/FortuneGroot/solana-token-risk-radar) — 0.5 stars/day
  - [Portaudit/referee](https://github.com/Portaudit/referee) — 0.17 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 1.29 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (1 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.
