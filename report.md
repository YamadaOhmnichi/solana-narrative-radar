# Solana Narrative Radar — Fortnightly Report

Generated: 2026-10-25T16:22:34+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 105.1)

- GitHub repos matching: **45**  (top velocity 41.11 stars/day)
- Headline mentions (last fortnight): **8**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours
  - The UK needs a workable route to regulated DeFi access

  Top repos:
  - [cxmza/windle](https://github.com/cxmza/windle) — 13.38 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 11.15 stars/day
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 9.2 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 45 trading-infrastructure repos at 41.11 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (8 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Dev Tooling & Infra  —  confidence: Medium  (score 51.0)

- GitHub repos matching: **43**  (top velocity 51.03 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [lalalune/daosfun-source](https://github.com/lalalune/daosfun-source) — 29.0 stars/day
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 9.2 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 7.6 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 43 tooling repos at 51.03 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 3. RWA & Tokenization  —  confidence: Medium  (score 41.2)

- GitHub repos matching: **5**  (top velocity 1.25 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours

  Top repos:
  - [CompdProtocol/compd-solana](https://github.com/CompdProtocol/compd-solana) — 0.5 stars/day
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.37 stars/day
  - [CompdProtocol/CompdProtocol](https://github.com/CompdProtocol/CompdProtocol) — 0.18 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (5 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 4. Meme & Speculation  —  confidence: Medium  (score 41.2)

- GitHub repos matching: **11**  (top velocity 37.46 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **1.85%**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 12.48 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 11.15 stars/day
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 9.2 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change 1.85%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change 1.85% so traders see which launches have real retention vs. pure rotation.

### 5. AI Agents on Solana  —  confidence: High  (score 37.8)

- GitHub repos matching: **23**  (top velocity 13.79 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Capital starting to rotate back to crypto from AI: Raoul Pal
  - SEC Flags AI 'Super Intelligence' and Tokenization as Systemic Market Risks
  - Bitcoin Core Rewrites Its Security Policy for a World Where AI Finds Bugs in One Prompt

  Top repos:
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 7.6 stars/day
  - [recogardtech/AutoPilotPM](https://github.com/recogardtech/AutoPilotPM) — 2.52 stars/day
  - [GuiBibeau/solos](https://github.com/GuiBibeau/solos) — 0.77 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 13.79 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in SpaceDataRig/space-data-rig-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. Payments & Stablecoins  —  confidence: Medium  (score 34.6)

- GitHub repos matching: **6**  (top velocity 2.62 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Solana Foundation hires ex-Binance CMO and payments exec as new partnerships expand
  - Hong Kong’s Biggest Bank Puts a Stablecoin in 3 Million Wallets

  Top repos:
  - [des35swim/hood-warfare](https://github.com/des35swim/hood-warfare) — 1.42 stars/day
  - [nirholas/papertrade-x402](https://github.com/nirholas/papertrade-x402) — 0.36 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 0.33 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 7. Wallets & UX  —  confidence: High  (score 30.5)

- GitHub repos matching: **10**  (top velocity 14.52 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Hong Kong’s Biggest Bank Puts a Stablecoin in 3 Million Wallets
  - Starknet introduces wallet privacy feature for DeFi activity

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 11.15 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 1.8 stars/day
  - [DigitalShieldOfficial/DigitalShield-Hardware-Airgap-Sdk](https://github.com/DigitalShieldOfficial/DigitalShield-Hardware-Airgap-Sdk) — 0.57 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 10 new wallet/onboarding repos at 14.52 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 8. Consumer & Social  —  confidence: Low  (score 10.6)

- GitHub repos matching: **6**  (top velocity 2.6 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **0/3**

  Sample headlines:
  - Game Publishers Have Pushed to Cut Discs Since 2007, Infinity Ward Veteran Says

  Top repos:
  - [des35swim/hood-warfare](https://github.com/des35swim/hood-warfare) — 1.42 stars/day
  - [vectorix-cross/My-web3-projects](https://github.com/vectorix-cross/My-web3-projects) — 0.34 stars/day
  - [livid/exe-hub](https://github.com/livid/exe-hub) — 0.29 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 6 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.
