# Solana Narrative Radar — Fortnightly Report

Generated: 2026-10-07T06:37:09+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 252.9)

- GitHub repos matching: **56**  (top velocity 228.89 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Flash Loan Attacks Drained $1.2B From DeFi Between 2020 and 2024: Study
  - S&P Global brings risk assessments to growing crypto lending vault sector
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 150.0 stars/day
  - [TINGLISE/auto-trading-bot-pumpfun-solana-V2](https://github.com/TINGLISE/auto-trading-bot-pumpfun-solana-V2) — 35.0 stars/day
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 27.5 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 56 trading-infrastructure repos at 228.89 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (3 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Wallets & UX  —  confidence: Medium  (score 244.9)

- GitHub repos matching: **20**  (top velocity 244.92 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 150.0 stars/day
  - [NuvexNetwork/nuvex](https://github.com/NuvexNetwork/nuvex) — 39.5 stars/day
  - [TINGLISE/auto-trading-bot-pumpfun-solana-V2](https://github.com/TINGLISE/auto-trading-bot-pumpfun-solana-V2) — 35.0 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 20 new wallet/onboarding repos at 244.92 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 3. Meme & Speculation  —  confidence: High  (score 241.6)

- GitHub repos matching: **11**  (top velocity 212.84 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **-6.39%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - Mistral AI Drops 'Le Chonk': A Massive AI Model Named After a Cat Meme
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 150.0 stars/day
  - [TINGLISE/auto-trading-bot-pumpfun-solana-V2](https://github.com/TINGLISE/auto-trading-bot-pumpfun-solana-V2) — 35.0 stars/day
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 19.72 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -6.39%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -6.39% so traders see which launches have real retention vs. pure rotation.

### 4. Dev Tooling & Infra  —  confidence: Medium  (score 79.7)

- GitHub repos matching: **41**  (top velocity 79.7 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [NuvexNetwork/nuvex](https://github.com/NuvexNetwork/nuvex) — 39.5 stars/day
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 27.5 stars/day
  - [propavingk/SlotDrift](https://github.com/propavingk/SlotDrift) — 4.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 41 tooling repos at 79.7 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 5. AI Agents on Solana  —  confidence: High  (score 50.5)

- GitHub repos matching: **19**  (top velocity 34.46 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Capital starting to rotate back to crypto from AI: Raoul Pal
  - Mistral AI Drops 'Le Chonk': A Massive AI Model Named After a Cat Meme

  Top repos:
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 27.5 stars/day
  - [recogardtech/AutoPilotPM](https://github.com/recogardtech/AutoPilotPM) — 3.88 stars/day
  - [Parad0x-Labs/vool](https://github.com/Parad0x-Labs/vool) — 0.83 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 34.46 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in NuvexNetwork/nuvex-services-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. Security & Threats  —  confidence: Medium  (score 43.0)

- GitHub repos matching: **1**  (top velocity 35.0 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Flash Loan Attacks Drained $1.2B From DeFi Between 2020 and 2024: Study

  Top repos:
  - [TINGLISE/auto-trading-bot-pumpfun-solana-V2](https://github.com/TINGLISE/auto-trading-bot-pumpfun-solana-V2) — 35.0 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 35.0 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (1 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. Payments & Stablecoins  —  confidence: High  (score 28.9)

- GitHub repos matching: **9**  (top velocity 4.93 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Solana Foundation hires ex-Binance CMO and payments exec as new partnerships expand
  - Circle Welcomes DJ Khaled to 'Team USDC' and Crypto Twitter Is Furious
  - Tether Hit With Lawsuit Over $2.76 Million Stablecoin Freeze

  Top repos:
  - [2274802010922/pipicachu](https://github.com/2274802010922/pipicachu) — 3.0 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 1.2 stars/day
  - [2274802010922/picachu__](https://github.com/2274802010922/picachu__) — 0.45 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. RWA & Tokenization  —  confidence: Medium  (score 17.1)

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
