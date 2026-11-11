# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-11T06:24:34+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Payments & Stablecoins  —  confidence: High  (score 100.3)

- GitHub repos matching: **8**  (top velocity 84.29 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Goldman, Citi and Global Banks Commit $270 Million to Challenge Crypto’s Stablecoin Giants

  Top repos:
  - [PatchBuilderAmplify/stolen-crypto-tracer](https://github.com/PatchBuilderAmplify/stolen-crypto-tracer) — 56.0 stars/day
  - [Signcluengine/onchain-money-trail-analyzer](https://github.com/Signcluengine/onchain-money-trail-analyzer) — 15.18 stars/day
  - [ismeh7765/FlashUSDT-v](https://github.com/ismeh7765/FlashUSDT-v) — 11.25 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 2. DeFi / Trading Infra  —  confidence: High  (score 96.9)

- GitHub repos matching: **42**  (top velocity 40.89 stars/day)
- Headline mentions (last fortnight): **7**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Solana's Jupiter Expands Beyond Trading With Token Baskets, Yield Vaults and New Portfolio

  Top repos:
  - [ismeh7765/FlashUSDT-v](https://github.com/ismeh7765/FlashUSDT-v) — 11.25 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 6.36 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 6.25 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 42 trading-infrastructure repos at 40.89 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (7 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. Dev Tooling & Infra  —  confidence: Medium  (score 84.0)

- GitHub repos matching: **50**  (top velocity 83.96 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [PatchBuilderAmplify/stolen-crypto-tracer](https://github.com/PatchBuilderAmplify/stolen-crypto-tracer) — 56.0 stars/day
  - [mAphrica/solana-foundation-kora](https://github.com/mAphrica/solana-foundation-kora) — 6.43 stars/day
  - [h100envy/crawl-hive](https://github.com/h100envy/crawl-hive) — 4.9 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 50 tooling repos at 83.96 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 4. Meme & Speculation  —  confidence: High  (score 70.5)

- GitHub repos matching: **15**  (top velocity 52.9 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-8.82%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [chadandyou/jrames](https://github.com/chadandyou/jrames) — 17.29 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 6.36 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 6.25 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -8.82%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -8.82% so traders see which launches have real retention vs. pure rotation.

### 5. Wallets & UX  —  confidence: Medium  (score 64.6)

- GitHub repos matching: **19**  (top velocity 64.61 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [PatchBuilderAmplify/stolen-crypto-tracer](https://github.com/PatchBuilderAmplify/stolen-crypto-tracer) — 56.0 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 6.36 stars/day
  - [PTK030/kenning](https://github.com/PTK030/kenning) — 0.81 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 19 new wallet/onboarding repos at 64.61 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 6. AI Agents on Solana  —  confidence: High  (score 52.7)

- GitHub repos matching: **23**  (top velocity 20.68 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - Bitcoin Miner HIVE Eyes $45 Million in Annual Revenue From AI Deal
  - Near AI Breach Exposes User Details and Data From 18 AI Agents

  Top repos:
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 6.25 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 4.84 stars/day
  - [askglyph/glyph](https://github.com/askglyph/glyph) — 3.88 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 20.68 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in teraus111/web3-agent-kit-solana-trading-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 7. Security & Threats  —  confidence: High  (score 29.4)

- GitHub repos matching: **8**  (top velocity 5.37 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Near AI Breach Exposes User Details and Data From 18 AI Agents
  - Drift exploiter sends $61M ETH to Tornado Cash, holds $194M

  Top repos:
  - [outgoingyang/solana-sniping-bot](https://github.com/outgoingyang/solana-sniping-bot) — 2.75 stars/day
  - [Quincy-Labs/solana-sec-bench](https://github.com/Quincy-Labs/solana-sec-bench) — 1.0 stars/day
  - [PTK030/kenning](https://github.com/PTK030/kenning) — 0.81 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 5.37 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 8. RWA & Tokenization  —  confidence: Medium  (score 24.7)

- GitHub repos matching: **4**  (top velocity 0.66 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Mirae Asset Securities issues tokenized notes on Solana
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading

  Top repos:
  - [Hymetdotfun/hymet](https://github.com/Hymetdotfun/hymet) — 0.29 stars/day
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.26 stars/day
  - [truenorth-lj/sofinance-public](https://github.com/truenorth-lj/sofinance-public) — 0.06 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (4 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.
