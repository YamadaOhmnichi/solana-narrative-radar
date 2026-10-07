# Solana Narrative Radar — Fortnightly Report

Generated: 2026-10-07T18:36:17+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Meme & Speculation  —  confidence: High  (score 151.9)

- GitHub repos matching: **12**  (top velocity 122.62 stars/day)
- Headline mentions (last fortnight): **1**
- Market 7d avg change: **-10.63%**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 86.5 stars/day
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 18.96 stars/day
  - [xmaxco/exlipse](https://github.com/xmaxco/exlipse) — 9.0 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -10.63%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -10.63% so traders see which launches have real retention vs. pure rotation.

### 2. DeFi / Trading Infra  —  confidence: High  (score 151.5)

- GitHub repos matching: **56**  (top velocity 135.47 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - S&P Global brings risk assessments to growing crypto lending vault sector
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 86.5 stars/day
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 24.14 stars/day
  - [xmaxco/exlipse](https://github.com/xmaxco/exlipse) — 9.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 56 trading-infrastructure repos at 135.47 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (2 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. Wallets & UX  —  confidence: Medium  (score 146.9)

- GitHub repos matching: **19**  (top velocity 138.92 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Europol Warns Crypto Wallets Are 'Primary Risk' for Quantum Attacks

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 86.5 stars/day
  - [NuvexNetwork/nuvex](https://github.com/NuvexNetwork/nuvex) — 32.2 stars/day
  - [thaorivera/crypto-wallet-generator-cracker](https://github.com/thaorivera/crypto-wallet-generator-cracker) — 8.0 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 19 new wallet/onboarding repos at 138.92 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 1 this period — users clearly need guardrails).

### 4. Dev Tooling & Infra  —  confidence: Medium  (score 67.8)

- GitHub repos matching: **42**  (top velocity 67.84 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [NuvexNetwork/nuvex](https://github.com/NuvexNetwork/nuvex) — 32.2 stars/day
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 24.14 stars/day
  - [propavingk/SlotDrift](https://github.com/propavingk/SlotDrift) — 3.76 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 42 tooling repos at 67.84 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 5. AI Agents on Solana  —  confidence: Medium  (score 38.9)

- GitHub repos matching: **20**  (top velocity 30.94 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Capital starting to rotate back to crypto from AI: Raoul Pal

  Top repos:
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 24.14 stars/day
  - [recogardtech/AutoPilotPM](https://github.com/recogardtech/AutoPilotPM) — 3.56 stars/day
  - [Parad0x-Labs/vool](https://github.com/Parad0x-Labs/vool) — 0.83 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 30.94 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in NuvexNetwork/nuvex-services-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. Consumer & Social  —  confidence: Medium  (score 20.6)

- GitHub repos matching: **6**  (top velocity 12.55 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Google Lets You Build a Video Game by Typing a Description

  Top repos:
  - [xmaxco/exlipse](https://github.com/xmaxco/exlipse) — 9.0 stars/day
  - [uni-launch/solana-token-creator](https://github.com/uni-launch/solana-token-creator) — 2.21 stars/day
  - [vectorix-cross/My-web3-projects](https://github.com/vectorix-cross/My-web3-projects) — 0.62 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 6 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.

### 7. Payments & Stablecoins  —  confidence: High  (score 19.7)

- GitHub repos matching: **9**  (top velocity 3.73 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Solana Foundation hires ex-Binance CMO and payments exec as new partnerships expand
  - Circle Welcomes DJ Khaled to 'Team USDC' and Crypto Twitter Is Furious

  Top repos:
  - [2274802010922/pipicachu](https://github.com/2274802010922/pipicachu) — 2.0 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 1.0 stars/day
  - [2274802010922/picachu__](https://github.com/2274802010922/picachu__) — 0.45 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. RWA & Tokenization  —  confidence: Medium  (score 17.0)

- GitHub repos matching: **6**  (top velocity 1.02 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Winners and losers of the SEC’s new tokenized stocks rules
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.62 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.25 stars/day
  - [thesithunyein/owed](https://github.com/thesithunyein/owed) — 0.06 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (6 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.
