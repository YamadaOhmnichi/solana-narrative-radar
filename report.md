# Solana Narrative Radar — Fortnightly Report

Generated: 2026-09-15T18:29:01+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Meme & Speculation  —  confidence: High  (score 150.6)

- GitHub repos matching: **14**  (top velocity 106.46 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **-14.08%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - Fomo overtakes Pump.fun in daily revenue on Solana
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 85.75 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 5.88 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 5.85 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -14.08%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -14.08% so traders see which launches have real retention vs. pure rotation.

### 2. DeFi / Trading Infra  —  confidence: High  (score 64.9)

- GitHub repos matching: **51**  (top velocity 24.86 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Solana Treasury Firm DeFi Dev Corp Rolls Out $300M CHAD to Buy More SOL
  - Kraken brings DeFi yield to tokenized stocks and ETFs
  - Sui DeFi protocol Full Sail to wind down after Switchboard incident

  Top repos:
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 5.88 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 5.85 stars/day
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 3.83 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 51 trading-infrastructure repos at 24.86 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. AI Agents on Solana  —  confidence: High  (score 25.6)

- GitHub repos matching: **20**  (top velocity 9.55 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Why an AI Slowdown Could Collapse Under Commercial and US-China Pressure
  - OpenAI’s Sam Altman Warns Humans Could Lose Control of AI

  Top repos:
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 3.83 stars/day
  - [PillCrew/PillCrew](https://github.com/PillCrew/PillCrew) — 2.12 stars/day
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 1.3 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 9.55 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in PillCrew/claimchain-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 4. Security & Threats  —  confidence: Medium  (score 24.2)

- GitHub repos matching: **3**  (top velocity 0.16 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - More Markets lending reserve drained for $410,000: Blockaid
  - Term Finance loses estimated $8.5M in vault governance exploit
  - Harmony plans rollback, wiping 109,000 transactions after ONE exploit

  Top repos:
  - [hypnogaba/solana-signal-trader](https://github.com/hypnogaba/solana-signal-trader) — 0.11 stars/day
  - [KarloAldrete/universal-proxy](https://github.com/KarloAldrete/universal-proxy) — 0.03 stars/day
  - [leafwithered/clawledger](https://github.com/leafwithered/clawledger) — 0.02 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.16 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 5. Wallets & UX  —  confidence: Medium  (score 20.2)

- GitHub repos matching: **20**  (top velocity 20.2 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 5.88 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 5.85 stars/day
  - [ascenx/safe_wallet](https://github.com/ascenx/safe_wallet) — 3.32 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 20 new wallet/onboarding repos at 20.2 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 6. Dev Tooling & Infra  —  confidence: Medium  (score 9.5)

- GitHub repos matching: **43**  (top velocity 9.47 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nicechunk/game](https://github.com/nicechunk/game) — 5.56 stars/day
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 1.3 stars/day
  - [Mgabal/-AMM-Automated-Market-Maker-Solana-Anchor](https://github.com/Mgabal/-AMM-Automated-Market-Maker-Solana-Anchor) — 1.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 43 tooling repos at 9.47 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 7. Payments & Stablecoins  —  confidence: Low  (score 8.5)

- GitHub repos matching: **6**  (top velocity 0.48 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **0/3**

  Sample headlines:
  - Banks Want More: Trade Groups Demand Stricter Stablecoin Limits in Clarity Act

  Top repos:
  - [nirholas/onchain-agent-wallets](https://github.com/nirholas/onchain-agent-wallets) — 0.19 stars/day
  - [neogeeks/tx402](https://github.com/neogeeks/tx402) — 0.14 stars/day
  - [grokloop/grokchain-programs](https://github.com/grokloop/grokchain-programs) — 0.06 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. RWA & Tokenization  —  confidence: Low  (score 8.1)

- GitHub repos matching: **3**  (top velocity 0.14 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **0/3**

  Sample headlines:
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [keelwright/slipway](https://github.com/keelwright/slipway) — 0.08 stars/day
  - [thesithunyein/equxi](https://github.com/thesithunyein/equxi) — 0.04 stars/day
  - [RedDuckTeam/staking](https://github.com/RedDuckTeam/staking) — 0.02 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (3 repos, Low confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.
