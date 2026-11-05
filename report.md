# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-05T19:58:16+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. AI Agents on Solana  —  confidence: High  (score 240.4)

- GitHub repos matching: **26**  (top velocity 216.42 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - Bitcoin Erases Election Rally as AI Stocks Plunge, $428 Million in Crypto Longs Get Wiped Out
  - Blockchain is ‘perfect solution’ for AI agent trust, VeChain CEO says

  Top repos:
  - [relayworkslab/relayworks](https://github.com/relayworkslab/relayworks) — 107.0 stars/day
  - [relayworkslab/relayworks-recovery](https://github.com/relayworkslab/relayworks-recovery) — 83.0 stars/day
  - [askglyph/glyph](https://github.com/askglyph/glyph) — 10.33 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 216.42 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in relayworkslab/relayworks-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 2. Meme & Speculation  —  confidence: High  (score 141.3)

- GitHub repos matching: **12**  (top velocity 109.02 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-16.13%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [chadandyou/jrames](https://github.com/chadandyou/jrames) — 63.5 stars/day
  - [tapoooooty/hypergrad](https://github.com/tapoooooty/hypergrad) — 10.83 stars/day
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 10.04 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -16.13%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -16.13% so traders see which launches have real retention vs. pure rotation.

### 3. Wallets & UX  —  confidence: High  (score 140.8)

- GitHub repos matching: **17**  (top velocity 124.78 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Stablecoins Go Mainstream as Samsung Wallet Adds USDC on Solana
  - Starknet introduces wallet privacy feature for DeFi activity

  Top repos:
  - [relayworkslab/relayworks](https://github.com/relayworkslab/relayworks) — 107.0 stars/day
  - [anica2020/Seed-Wallet-Checker](https://github.com/anica2020/Seed-Wallet-Checker) — 7.33 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 7.29 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 17 new wallet/onboarding repos at 124.78 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 4. Payments & Stablecoins  —  confidence: High  (score 133.9)

- GitHub repos matching: **6**  (top velocity 117.94 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Stablecoins Go Mainstream as Samsung Wallet Adds USDC on Solana

  Top repos:
  - [relayworkslab/relayworks-recovery](https://github.com/relayworkslab/relayworks-recovery) — 83.0 stars/day
  - [Signcluengine/onchain-money-trail-analyzer](https://github.com/Signcluengine/onchain-money-trail-analyzer) — 34.2 stars/day
  - [blueshift-gg/solana-pull-program](https://github.com/blueshift-gg/solana-pull-program) — 0.23 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 5. DeFi / Trading Infra  —  confidence: High  (score 108.4)

- GitHub repos matching: **39**  (top velocity 36.38 stars/day)
- Headline mentions (last fortnight): **9**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading
  - Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours
  - Solana Labs’ Leap Launches Mobile App for Trading Tokenized Stocks and Crypto

  Top repos:
  - [tapoooooty/hypergrad](https://github.com/tapoooooty/hypergrad) — 10.83 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 7.32 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 7.29 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 39 trading-infrastructure repos at 36.38 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (9 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 6. Dev Tooling & Infra  —  confidence: Medium  (score 49.3)

- GitHub repos matching: **49**  (top velocity 49.3 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [mAphrica/solana-foundation-kora](https://github.com/mAphrica/solana-foundation-kora) — 11.38 stars/day
  - [Nexq-Pro/program](https://github.com/Nexq-Pro/program) — 6.74 stars/day
  - [Nexq-Pro/explorer](https://github.com/Nexq-Pro/explorer) — 6.71 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 49 tooling repos at 49.3 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 7. RWA & Tokenization  —  confidence: Medium  (score 40.4)

- GitHub repos matching: **3**  (top velocity 0.41 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Mirae Asset Securities issues tokenized notes on Solana
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading

  Top repos:
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.28 stars/day
  - [truenorth-lj/sofinance-public](https://github.com/truenorth-lj/sofinance-public) — 0.07 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.06 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (3 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 8. Security & Threats  —  confidence: Medium  (score 24.6)

- GitHub repos matching: **4**  (top velocity 0.62 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - OpenAI Found 948 Linux Security Flaws—And Figured Out How to Exploit Them
  - Drift exploiter sends $61M ETH to Tornado Cash, holds $194M

  Top repos:
  - [BadmonLano/meme-sniper](https://github.com/BadmonLano/meme-sniper) — 0.38 stars/day
  - [RedDuckTeam/redduck-solana-audit](https://github.com/RedDuckTeam/redduck-solana-audit) — 0.14 stars/day
  - [Portaudit/referee](https://github.com/Portaudit/referee) — 0.05 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.62 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.
