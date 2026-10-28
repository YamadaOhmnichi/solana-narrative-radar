# Solana Narrative Radar — Fortnightly Report

Generated: 2026-10-28T05:44:21+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 168.7)

- GitHub repos matching: **46**  (top velocity 96.67 stars/day)
- Headline mentions (last fortnight): **9**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours
  - Robinhood Taps Ripple's Stablecoin, Treasury Software and Trading Loans

  Top repos:
  - [wcoxptzhhdbo/solana-sniper-bot](https://github.com/wcoxptzhhdbo/solana-sniper-bot) — 52.5 stars/day
  - [cxmza/windle](https://github.com/cxmza/windle) — 10.81 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 10.14 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 46 trading-infrastructure repos at 96.67 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (9 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Meme & Speculation  —  confidence: Medium  (score 100.8)

- GitHub repos matching: **13**  (top velocity 95.78 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-2.53%**
- Cross-source confirmation: **1/3**

  Top repos:
  - [wcoxptzhhdbo/solana-sniper-bot](https://github.com/wcoxptzhhdbo/solana-sniper-bot) — 52.5 stars/day
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 11.96 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 10.14 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -2.53%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -2.53% so traders see which launches have real retention vs. pure rotation.

### 3. AI Agents on Solana  —  confidence: High  (score 52.0)

- GitHub repos matching: **22**  (top velocity 19.99 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - Capital starting to rotate back to crypto from AI: Raoul Pal
  - China's Stock Market Has Lost $2.4 Trillion as Investors Doubt Its AI Boom Will Ever Pay Off

  Top repos:
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 7.18 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 7.14 stars/day
  - [recogardtech/AutoPilotPM](https://github.com/recogardtech/AutoPilotPM) — 2.59 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 19.99 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in SpaceDataRig/space-data-rig-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 4. Dev Tooling & Infra  —  confidence: Medium  (score 34.4)

- GitHub repos matching: **43**  (top velocity 34.35 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [lalalune/daosfun-source](https://github.com/lalalune/daosfun-source) — 10.67 stars/day
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 8.47 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 7.18 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 43 tooling repos at 34.35 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 5. Payments & Stablecoins  —  confidence: Medium  (score 34.1)

- GitHub repos matching: **5**  (top velocity 2.15 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Robinhood Taps Ripple's Stablecoin, Treasury Software and Trading Loans
  - Anchorage Positions Itself as Custody Backbone of US-Mexico Stablecoin Corridor

  Top repos:
  - [des35swim/hood-warfare](https://github.com/des35swim/hood-warfare) — 1.13 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 0.31 stars/day
  - [nirholas/papertrade-x402](https://github.com/nirholas/papertrade-x402) — 0.29 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 6. RWA & Tokenization  —  confidence: Medium  (score 33.8)

- GitHub repos matching: **6**  (top velocity 1.75 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours

  Top repos:
  - [CompdProtocol/compd-solana-programs](https://github.com/CompdProtocol/compd-solana-programs) — 0.5 stars/day
  - [CompdProtocol/compd-solana](https://github.com/CompdProtocol/compd-solana) — 0.5 stars/day
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.34 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (6 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 7. Wallets & UX  —  confidence: High  (score 31.2)

- GitHub repos matching: **10**  (top velocity 15.2 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Bitcoin Wallet Maker Keystone Pulls Devices as Stolen Key Opens Door to Fakes
  - Starknet introduces wallet privacy feature for DeFi activity

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 10.14 stars/day
  - [aaronjmars/walletscan](https://github.com/aaronjmars/walletscan) — 2.0 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 1.72 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 10 new wallet/onboarding repos at 15.2 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 8. Security & Threats  —  confidence: Low  (score 8.2)

- GitHub repos matching: **2**  (top velocity 0.15 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **0/3**

  Sample headlines:
  - Drift exploiter sends $61M ETH to Tornado Cash, holds $194M

  Top repos:
  - [TodorBonchev/rust-auditor](https://github.com/TodorBonchev/rust-auditor) — 0.08 stars/day
  - [Portaudit/referee](https://github.com/Portaudit/referee) — 0.07 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.15 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (1 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.
