# Solana Narrative Radar — Fortnightly Report

Generated: 2026-10-06T18:34:16+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 112.9)

- GitHub repos matching: **55**  (top velocity 72.93 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Flash Loan Attacks Drained $1.2B From DeFi Between 2020 and 2024: Study
  - Don Davis Bill Would Fine Candidates $10K for Trading on Their Own Elections
  - DeFi Development Corp Adds $3 Million in Solana as SOL Buys Slow

  Top repos:
  - [TINGLISE/auto-trading-bot-pumpfun-solana-V2](https://github.com/TINGLISE/auto-trading-bot-pumpfun-solana-V2) — 28.0 stars/day
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 26.83 stars/day
  - [recogardtech/AutoPilotPM](https://github.com/recogardtech/AutoPilotPM) — 3.88 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 55 trading-infrastructure repos at 72.93 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Wallets & UX  —  confidence: Medium  (score 94.6)

- GitHub repos matching: **19**  (top velocity 94.64 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [NuvexNetwork/nuvex](https://github.com/NuvexNetwork/nuvex) — 38.0 stars/day
  - [TINGLISE/auto-trading-bot-pumpfun-solana-V2](https://github.com/TINGLISE/auto-trading-bot-pumpfun-solana-V2) — 28.0 stars/day
  - [thaorivera/crypto-wallet-generator-cracker](https://github.com/thaorivera/crypto-wallet-generator-cracker) — 16.0 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 19 new wallet/onboarding repos at 94.64 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 3. Dev Tooling & Infra  —  confidence: Medium  (score 77.9)

- GitHub repos matching: **41**  (top velocity 77.87 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [NuvexNetwork/nuvex](https://github.com/NuvexNetwork/nuvex) — 38.0 stars/day
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 26.83 stars/day
  - [propavingk/SlotDrift](https://github.com/propavingk/SlotDrift) — 4.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 41 tooling repos at 77.87 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 4. Meme & Speculation  —  confidence: High  (score 74.9)

- GitHub repos matching: **11**  (top velocity 55.95 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **1.47%**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Mistral AI Drops 'Le Chonk': A Massive AI Model Named After a Cat Meme
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [TINGLISE/auto-trading-bot-pumpfun-solana-V2](https://github.com/TINGLISE/auto-trading-bot-pumpfun-solana-V2) — 28.0 stars/day
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 19.56 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 2.67 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change 1.47%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change 1.47% so traders see which launches have real retention vs. pure rotation.

### 5. AI Agents on Solana  —  confidence: High  (score 49.9)

- GitHub repos matching: **19**  (top velocity 33.91 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Capital starting to rotate back to crypto from AI: Raoul Pal
  - Mistral AI Drops 'Le Chonk': A Massive AI Model Named After a Cat Meme

  Top repos:
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 26.83 stars/day
  - [recogardtech/AutoPilotPM](https://github.com/recogardtech/AutoPilotPM) — 3.88 stars/day
  - [Parad0x-Labs/vool](https://github.com/Parad0x-Labs/vool) — 0.88 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 33.91 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in NuvexNetwork/nuvex-services-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. Security & Threats  —  confidence: Medium  (score 36.0)

- GitHub repos matching: **1**  (top velocity 28.0 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Flash Loan Attacks Drained $1.2B From DeFi Between 2020 and 2024: Study

  Top repos:
  - [TINGLISE/auto-trading-bot-pumpfun-solana-V2](https://github.com/TINGLISE/auto-trading-bot-pumpfun-solana-V2) — 28.0 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 28.0 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (1 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. RWA & Tokenization  —  confidence: Medium  (score 17.1)

- GitHub repos matching: **6**  (top velocity 1.14 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Winners and losers of the SEC’s new tokenized stocks rules
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.65 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.33 stars/day
  - [thesithunyein/owed](https://github.com/thesithunyein/owed) — 0.07 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (6 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 8. Payments & Stablecoins  —  confidence: Medium  (score 13.0)

- GitHub repos matching: **9**  (top velocity 5.0 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Solana Foundation hires ex-Binance CMO and payments exec as new partnerships expand

  Top repos:
  - [2274802010922/pipicachu](https://github.com/2274802010922/pipicachu) — 3.0 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 1.2 stars/day
  - [2274802010922/picachu__](https://github.com/2274802010922/picachu__) — 0.5 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.
