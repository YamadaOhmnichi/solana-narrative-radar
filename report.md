# Solana Narrative Radar — Fortnightly Report

Generated: 2026-10-10T17:21:15+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Wallets & UX  —  confidence: Medium  (score 104.0)

- GitHub repos matching: **20**  (top velocity 96.04 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Ledger Probes Potential Theft of $87M in User Funds Tied to Crypto Wallet Reseller

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 39.4 stars/day
  - [NuvexNetwork/nuvex](https://github.com/NuvexNetwork/nuvex) — 21.5 stars/day
  - [Janina21/Crypto-Checker](https://github.com/Janina21/Crypto-Checker) — 20.75 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 20 new wallet/onboarding repos at 96.04 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 1 this period — users clearly need guardrails).

### 2. DeFi / Trading Infra  —  confidence: High  (score 98.3)

- GitHub repos matching: **56**  (top velocity 74.32 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - THORChain exec accuses Tether of temporarily freezing USDT vaults
  - S&P Global brings risk assessments to growing crypto lending vault sector
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 39.4 stars/day
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 17.8 stars/day
  - [xmaxco/exlipse](https://github.com/xmaxco/exlipse) — 3.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 56 trading-infrastructure repos at 74.32 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (3 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. Meme & Speculation  —  confidence: High  (score 84.9)

- GitHub repos matching: **11**  (top velocity 69.2 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-7.87%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 39.4 stars/day
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 18.24 stars/day
  - [xmaxco/exlipse](https://github.com/xmaxco/exlipse) — 3.0 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -7.87%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -7.87% so traders see which launches have real retention vs. pure rotation.

### 4. Dev Tooling & Infra  —  confidence: Medium  (score 48.0)

- GitHub repos matching: **41**  (top velocity 47.97 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [NuvexNetwork/nuvex](https://github.com/NuvexNetwork/nuvex) — 21.5 stars/day
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 17.8 stars/day
  - [propavingk/SlotDrift](https://github.com/propavingk/SlotDrift) — 3.2 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 41 tooling repos at 47.97 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 5. AI Agents on Solana  —  confidence: High  (score 47.8)

- GitHub repos matching: **20**  (top velocity 23.81 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Capital starting to rotate back to crypto from AI: Raoul Pal
  - Here’s a Way to Predict When AI Chatbots Will Turn Bad
  - OpenAI and Anthropic Are Quietly Rehearsing for the Day After an AI Catastrophe

  Top repos:
  - [NuvexNetwork/nuvex-services](https://github.com/NuvexNetwork/nuvex-services) — 17.8 stars/day
  - [recogardtech/AutoPilotPM](https://github.com/recogardtech/AutoPilotPM) — 2.83 stars/day
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 0.73 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 23.81 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in NuvexNetwork/nuvex-services-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. Payments & Stablecoins  —  confidence: Medium  (score 18.3)

- GitHub repos matching: **8**  (top velocity 2.31 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Solana Foundation hires ex-Binance CMO and payments exec as new partnerships expand
  - French Committee Backs Stablecoin Swap Tax and Crypto Exit Tax, Then Rejects the Budget

  Top repos:
  - [2274802010922/pipicachu](https://github.com/2274802010922/pipicachu) — 1.0 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 0.67 stars/day
  - [2274802010922/picachu__](https://github.com/2274802010922/picachu__) — 0.36 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 7. RWA & Tokenization  —  confidence: Medium  (score 17.8)

- GitHub repos matching: **6**  (top velocity 1.83 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Winners and losers of the SEC’s new tokenized stocks rules
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [2274802010922/pipicachu](https://github.com/2274802010922/pipicachu) — 1.0 stars/day
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.58 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.14 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (6 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 8. Consumer & Social  —  confidence: Medium  (score 6.6)

- GitHub repos matching: **7**  (top velocity 6.59 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [xmaxco/exlipse](https://github.com/xmaxco/exlipse) — 3.0 stars/day
  - [uni-launch/solana-token-creator](https://github.com/uni-launch/solana-token-creator) — 1.82 stars/day
  - [vectorix-cross/My-web3-projects](https://github.com/vectorix-cross/My-web3-projects) — 0.58 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 7 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.
