# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-03T14:17:27+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 186.3)

- GitHub repos matching: **42**  (top velocity 122.28 stars/day)
- Headline mentions (last fortnight): **8**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours
  - The UK needs a workable route to regulated DeFi access

  Top repos:
  - [DolphinStronghold9/stolen-crypto-tracer](https://github.com/DolphinStronghold9/stolen-crypto-tracer) — 50.33 stars/day
  - [outgoingyang/solana-sniping-bot](https://github.com/outgoingyang/solana-sniping-bot) — 22.0 stars/day
  - [tapoooooty/hypergrad](https://github.com/tapoooooty/hypergrad) — 17.75 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 42 trading-infrastructure repos at 122.28 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (8 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Meme & Speculation  —  confidence: High  (score 165.5)

- GitHub repos matching: **13**  (top velocity 147.61 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-8.93%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [chadandyou/jrames](https://github.com/chadandyou/jrames) — 71.0 stars/day
  - [outgoingyang/solana-sniping-bot](https://github.com/outgoingyang/solana-sniping-bot) — 22.0 stars/day
  - [tapoooooty/hypergrad](https://github.com/tapoooooty/hypergrad) — 17.75 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -8.93%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -8.93% so traders see which launches have real retention vs. pure rotation.

### 3. Payments & Stablecoins  —  confidence: Medium  (score 116.8)

- GitHub repos matching: **6**  (top velocity 108.79 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain

  Top repos:
  - [Signcluengine/onchain-money-trail-analyzer](https://github.com/Signcluengine/onchain-money-trail-analyzer) — 57.67 stars/day
  - [DolphinStronghold9/stolen-crypto-tracer](https://github.com/DolphinStronghold9/stolen-crypto-tracer) — 50.33 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 0.24 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 4. Dev Tooling & Infra  —  confidence: Medium  (score 110.0)

- GitHub repos matching: **49**  (top velocity 110.0 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [DolphinStronghold9/stolen-crypto-tracer](https://github.com/DolphinStronghold9/stolen-crypto-tracer) — 50.33 stars/day
  - [outgoingyang/solana-sniping-bot](https://github.com/outgoingyang/solana-sniping-bot) — 22.0 stars/day
  - [Nexq-Pro/program](https://github.com/Nexq-Pro/program) — 7.39 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 49 tooling repos at 110.0 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 5. Wallets & UX  —  confidence: High  (score 93.2)

- GitHub repos matching: **17**  (top velocity 77.23 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - North Korea Is Laundering Binance Hack Loot at One New Wallet Every 25 Seconds
  - Starknet introduces wallet privacy feature for DeFi activity

  Top repos:
  - [DolphinStronghold9/stolen-crypto-tracer](https://github.com/DolphinStronghold9/stolen-crypto-tracer) — 50.33 stars/day
  - [anica2020/Seed-Wallet-Checker](https://github.com/anica2020/Seed-Wallet-Checker) — 11.0 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 7.76 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 17 new wallet/onboarding repos at 77.23 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 6. Security & Threats  —  confidence: High  (score 86.7)

- GitHub repos matching: **5**  (top velocity 22.7 stars/day)
- Headline mentions (last fortnight): **8**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Morning Minute: Tom Lee Calls the Binance Hack Bullish for Ethereum
  - Liquid Network Restores Full Bitcoin Backing Two Months After $320M Exploit

  Top repos:
  - [outgoingyang/solana-sniping-bot](https://github.com/outgoingyang/solana-sniping-bot) — 22.0 stars/day
  - [BadmonLano/meme-sniper](https://github.com/BadmonLano/meme-sniper) — 0.4 stars/day
  - [RedDuckTeam/redduck-solana-audit](https://github.com/RedDuckTeam/redduck-solana-audit) — 0.2 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 22.7 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (8 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. AI Agents on Solana  —  confidence: High  (score 75.3)

- GitHub repos matching: **26**  (top velocity 51.31 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - Tom Lee Calls Bottom on AI Stock Selloff, Citing Tight Supply and Crypto Resilience
  - Proton Users Revolt After CEO Calls Security Caution 'Loser Thinking' Amid AI Push

  Top repos:
  - [askglyph/glyph](https://github.com/askglyph/glyph) — 27.0 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 8.65 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 5.96 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 51.31 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in askglyph/glyph-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 8. DePIN & Physical Infra  —  confidence: Medium  (score 34.2)

- GitHub repos matching: **3**  (top velocity 34.25 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [outgoingyang/solana-sniping-bot](https://github.com/outgoingyang/solana-sniping-bot) — 22.0 stars/day
  - [Nexq-Pro/program](https://github.com/Nexq-Pro/program) — 7.39 stars/day
  - [refrax-xyz/refrax-node](https://github.com/refrax-xyz/refrax-node) — 4.86 stars/day

  **Build ideas:**
  - DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet (3 repos, Medium confidence).
  - Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.
  - Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.
