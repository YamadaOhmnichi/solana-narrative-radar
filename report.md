# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-10T07:20:47+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Dev Tooling & Infra  —  confidence: Medium  (score 105.4)

- GitHub repos matching: **52**  (top velocity 105.39 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [PatchBuilderAmplify/stolen-crypto-tracer](https://github.com/PatchBuilderAmplify/stolen-crypto-tracer) — 65.0 stars/day
  - [mAphrica/solana-foundation-kora](https://github.com/mAphrica/solana-foundation-kora) — 7.0 stars/day
  - [Nexq-Pro/explorer](https://github.com/Nexq-Pro/explorer) — 6.26 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 52 tooling repos at 105.39 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 2. Payments & Stablecoins  —  confidence: Medium  (score 101.8)

- GitHub repos matching: **8**  (top velocity 93.85 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain

  Top repos:
  - [PatchBuilderAmplify/stolen-crypto-tracer](https://github.com/PatchBuilderAmplify/stolen-crypto-tracer) — 65.0 stars/day
  - [Signcluengine/onchain-money-trail-analyzer](https://github.com/Signcluengine/onchain-money-trail-analyzer) — 16.7 stars/day
  - [ismeh7765/FlashUSDT-v](https://github.com/ismeh7765/FlashUSDT-v) — 10.75 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 3. DeFi / Trading Infra  —  confidence: High  (score 90.5)

- GitHub repos matching: **43**  (top velocity 42.49 stars/day)
- Headline mentions (last fortnight): **6**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - The UK needs a workable route to regulated DeFi access

  Top repos:
  - [ismeh7765/FlashUSDT-v](https://github.com/ismeh7765/FlashUSDT-v) — 10.75 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 6.51 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 6.44 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 43 trading-infrastructure repos at 42.49 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (6 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 4. Meme & Speculation  —  confidence: High  (score 83.2)

- GitHub repos matching: **16**  (top velocity 63.28 stars/day)
- Headline mentions (last fortnight): **1**
- Market 7d avg change: **-5.96%**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Binance Hack Launderers Mint Elon Musk and Animal Meme Coins to Move Stolen Crypto

  Top repos:
  - [chadandyou/jrames](https://github.com/chadandyou/jrames) — 20.17 stars/day
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 9.44 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 6.51 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -5.96%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -5.96% so traders see which launches have real retention vs. pure rotation.

### 5. Wallets & UX  —  confidence: Medium  (score 73.8)

- GitHub repos matching: **18**  (top velocity 73.78 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [PatchBuilderAmplify/stolen-crypto-tracer](https://github.com/PatchBuilderAmplify/stolen-crypto-tracer) — 65.0 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 6.51 stars/day
  - [PTK030/kenning](https://github.com/PTK030/kenning) — 0.77 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 18 new wallet/onboarding repos at 73.78 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 6. AI Agents on Solana  —  confidence: High  (score 60.7)

- GitHub repos matching: **25**  (top velocity 20.72 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - AI Data Centers Are Buying Used Jet Engines as New Power Turbines Take Six Years
  - Google Takes Aim at Nvidia With New AI Chips Built for Privacy and Massive Memory

  Top repos:
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 6.44 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 4.9 stars/day
  - [askglyph/glyph](https://github.com/askglyph/glyph) — 4.43 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 20.72 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in teraus111/web3-agent-kit-solana-trading-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 7. RWA & Tokenization  —  confidence: Medium  (score 40.7)

- GitHub repos matching: **4**  (top velocity 0.7 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Mirae Asset Securities issues tokenized notes on Solana
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading

  Top repos:
  - [Hymetdotfun/hymet](https://github.com/Hymetdotfun/hymet) — 0.33 stars/day
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.26 stars/day
  - [truenorth-lj/sofinance-public](https://github.com/truenorth-lj/sofinance-public) — 0.06 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (4 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 8. Security & Threats  —  confidence: High  (score 28.4)

- GitHub repos matching: **6**  (top velocity 4.45 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Binance Hack Launderers Mint Elon Musk and Animal Meme Coins to Move Stolen Crypto
  - Drift exploiter sends $61M ETH to Tornado Cash, holds $194M

  Top repos:
  - [outgoingyang/solana-sniping-bot](https://github.com/outgoingyang/solana-sniping-bot) — 3.14 stars/day
  - [PTK030/kenning](https://github.com/PTK030/kenning) — 0.77 stars/day
  - [BadmonLano/meme-sniper](https://github.com/BadmonLano/meme-sniper) — 0.29 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 4.45 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.
