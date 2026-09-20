# Solana Narrative Radar — Fortnightly Report

Generated: 2026-09-20T12:31:17+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. RWA & Tokenization  —  confidence: High  (score 113.5)

- GitHub repos matching: **6**  (top velocity 97.54 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Morning Minute: SEC Approves ‘Innovation Exemption’ Moving Tokenized Stocks Forward
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [coolbbcamp/Synthetic-Liquidity-Depth-Scanner](https://github.com/coolbbcamp/Synthetic-Liquidity-Depth-Scanner) — 51.5 stars/day
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 45.75 stars/day
  - [vectorix-cross/CrossYield](https://github.com/vectorix-cross/CrossYield) — 0.17 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (6 repos, High confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 2. DeFi / Trading Infra  —  confidence: High  (score 110.9)

- GitHub repos matching: **49**  (top velocity 70.88 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Coinbase Files to List Single-Stock Perps on Apple, Tesla and Nvidia
  - Kraken brings DeFi yield to tokenized stocks and ETFs
  - Sui DeFi protocol Full Sail to wind down after Switchboard incident

  Top repos:
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 45.75 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 9.56 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 4.05 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 49 trading-infrastructure repos at 70.88 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. Meme & Speculation  —  confidence: High  (score 86.8)

- GitHub repos matching: **18**  (top velocity 56.42 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **7.21%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - Fomo overtakes Pump.fun in daily revenue on Solana
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 41.78 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 4.05 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 3.97 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change 7.21%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change 7.21% so traders see which launches have real retention vs. pure rotation.

### 4. Wallets & UX  —  confidence: Medium  (score 69.4)

- GitHub repos matching: **19**  (top velocity 69.41 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 45.75 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 9.56 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 4.05 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 19 new wallet/onboarding repos at 69.41 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 5. Dev Tooling & Infra  —  confidence: Medium  (score 58.8)

- GitHub repos matching: **43**  (top velocity 58.82 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 45.75 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 9.56 stars/day
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 1.33 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 43 tooling repos at 58.82 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 6. Security & Threats  —  confidence: Medium  (score 17.0)

- GitHub repos matching: **4**  (top velocity 0.97 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - More Markets lending reserve drained for $410,000: Blockaid
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [andreysuperiorgit/aegis](https://github.com/andreysuperiorgit/aegis) — 0.89 stars/day
  - [hypnogaba/solana-signal-trader](https://github.com/hypnogaba/solana-signal-trader) — 0.04 stars/day
  - [KarloAldrete/universal-proxy](https://github.com/KarloAldrete/universal-proxy) — 0.02 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.97 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (2 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. AI Agents on Solana  —  confidence: Medium  (score 15.2)

- GitHub repos matching: **20**  (top velocity 7.18 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Microsoft Staff Asked If AI Scraping Was 'Largest Theft of Labor in Human History'

  Top repos:
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 1.59 stars/day
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 1.33 stars/day
  - [PillCrew/PillCrew](https://github.com/PillCrew/PillCrew) — 1.14 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 7.18 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in PillCrew/claimchain-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 8. DePIN & Physical Infra  —  confidence: Low  (score 1.4)

- GitHub repos matching: **2**  (top velocity 1.35 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **0/3**

  Top repos:
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 1.33 stars/day
  - [belumume/zeroclaw-solana](https://github.com/belumume/zeroclaw-solana) — 0.02 stars/day

  **Build ideas:**
  - DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet (2 repos, Low confidence).
  - Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.
  - Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.
