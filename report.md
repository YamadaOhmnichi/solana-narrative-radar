# Solana Narrative Radar — Fortnightly Report

Generated: 2026-09-18T12:32:16+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Meme & Speculation  —  confidence: High  (score 101.5)

- GitHub repos matching: **17**  (top velocity 69.28 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **8.12%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - Fomo overtakes Pump.fun in daily revenue on Solana
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 51.43 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 5.51 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 5.39 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change 8.12%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change 8.12% so traders see which launches have real retention vs. pure rotation.

### 2. DeFi / Trading Infra  —  confidence: High  (score 52.6)

- GitHub repos matching: **49**  (top velocity 20.58 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Kraken brings DeFi yield to tokenized stocks and ETFs
  - Sui DeFi protocol Full Sail to wind down after Switchboard incident
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 5.51 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 5.39 stars/day
  - [tayohya/solprobe](https://github.com/tayohya/solprobe) — 2.09 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 49 trading-infrastructure repos at 20.58 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (4 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. AI Agents on Solana  —  confidence: High  (score 39.5)

- GitHub repos matching: **20**  (top velocity 7.51 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Security Experts Want the US and China to Promise Never to Let AI Control Nukes
  - Ethereum Founder Vitalik Buterin Says AI Won’t Doom Crypto Security
  - Andrew Yang Calls for AI Kill Switch as Safety Fears Mount

  Top repos:
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 1.8 stars/day
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 1.31 stars/day
  - [PillCrew/PillCrew](https://github.com/PillCrew/PillCrew) — 1.22 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 7.51 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in PillCrew/claimchain-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 4. Wallets & UX  —  confidence: Medium  (score 18.7)

- GitHub repos matching: **18**  (top velocity 18.67 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 5.51 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 5.39 stars/day
  - [ascenx/safe_wallet](https://github.com/ascenx/safe_wallet) — 3.16 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 18 new wallet/onboarding repos at 18.67 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 5. Security & Threats  —  confidence: Medium  (score 17.2)

- GitHub repos matching: **4**  (top velocity 1.23 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - More Markets lending reserve drained for $410,000: Blockaid
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [andreysuperiorgit/aegis](https://github.com/andreysuperiorgit/aegis) — 1.14 stars/day
  - [hypnogaba/solana-signal-trader](https://github.com/hypnogaba/solana-signal-trader) — 0.05 stars/day
  - [KarloAldrete/universal-proxy](https://github.com/KarloAldrete/universal-proxy) — 0.02 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 1.23 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (2 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 6. Dev Tooling & Infra  —  confidence: Medium  (score 9.8)

- GitHub repos matching: **41**  (top velocity 9.85 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nicechunk/game](https://github.com/nicechunk/game) — 5.27 stars/day
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 1.31 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 1.14 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 41 tooling repos at 9.85 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 7. RWA & Tokenization  —  confidence: Low  (score 8.1)

- GitHub repos matching: **3**  (top velocity 0.13 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **0/3**

  Sample headlines:
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [keelwright/slipway](https://github.com/keelwright/slipway) — 0.07 stars/day
  - [thesithunyein/equxi](https://github.com/thesithunyein/equxi) — 0.04 stars/day
  - [RedDuckTeam/staking](https://github.com/RedDuckTeam/staking) — 0.02 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (3 repos, Low confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 8. Consumer & Social  —  confidence: Medium  (score 6.4)

- GitHub repos matching: **7**  (top velocity 6.39 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nicechunk/game](https://github.com/nicechunk/game) — 5.27 stars/day
  - [blueshift-gg/solana-awesome](https://github.com/blueshift-gg/solana-awesome) — 0.48 stars/day
  - [accretion-xyz/awesome-solana-security](https://github.com/accretion-xyz/awesome-solana-security) — 0.22 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 7 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.
