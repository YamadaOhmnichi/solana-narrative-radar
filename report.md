# Solana Narrative Radar — Fortnightly Report

Generated: 2026-09-22T00:33:58+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Meme & Speculation  —  confidence: High  (score 200.5)

- GitHub repos matching: **16**  (top velocity 152.08 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **16.19%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - Fomo overtakes Pump.fun in daily revenue on Solana
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [Driftmireminisce/SOL-FOR-GIT-CLUB](https://github.com/Driftmireminisce/SOL-FOR-GIT-CLUB) — 97.0 stars/day
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 42.5 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 3.87 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change 16.19%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change 16.19% so traders see which launches have real retention vs. pure rotation.

### 2. RWA & Tokenization  —  confidence: High  (score 98.3)

- GitHub repos matching: **5**  (top velocity 82.28 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Europe’s Central Bank Prepares to Invest Own Funds in Tokenized Securities
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [coolbbcamp/Synthetic-Liquidity-Depth-Scanner](https://github.com/coolbbcamp/Synthetic-Liquidity-Depth-Scanner) — 43.0 stars/day
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 39.17 stars/day
  - [keelwright/slipway](https://github.com/keelwright/slipway) — 0.06 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (5 repos, High confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 3. DeFi / Trading Infra  —  confidence: High  (score 97.2)

- GitHub repos matching: **47**  (top velocity 65.21 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Kraken brings DeFi yield to tokenized stocks and ETFs
  - Sui DeFi protocol Full Sail to wind down after Switchboard incident
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 39.17 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 7.82 stars/day
  - [mangiapanejohn-dev/MOBIUS-Searcher](https://github.com/mangiapanejohn-dev/MOBIUS-Searcher) — 4.5 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 47 trading-infrastructure repos at 65.21 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (4 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 4. Wallets & UX  —  confidence: Medium  (score 67.6)

- GitHub repos matching: **20**  (top velocity 67.62 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 39.17 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 7.82 stars/day
  - [Kylerkrausemdzyra64/Crypto-Checker](https://github.com/Kylerkrausemdzyra64/Crypto-Checker) — 7.33 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 20 new wallet/onboarding repos at 67.62 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 5. Dev Tooling & Infra  —  confidence: Medium  (score 50.1)

- GitHub repos matching: **42**  (top velocity 50.06 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 39.17 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 7.82 stars/day
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 1.31 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 42 tooling repos at 50.06 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 6. AI Agents on Solana  —  confidence: High  (score 29.6)

- GitHub repos matching: **18**  (top velocity 5.55 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Google Admits Gemini AI Hacked Three Companies—It Stayed Silent for 7 Weeks
  - What Is VVV? The Privacy-Obsessed AI Token That’s Up 3,000% in 2026
  - xAI Launches Grok 4.7. It's Bigger, But Late to the AI Frontier Party

  Top repos:
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 1.42 stars/day
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 1.31 stars/day
  - [PillCrew/PillCrew](https://github.com/PillCrew/PillCrew) — 1.06 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 5.55 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in PillCrew/claimchain-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 7. Security & Threats  —  confidence: Medium  (score 24.9)

- GitHub repos matching: **4**  (top velocity 0.9 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Google Admits Gemini AI Hacked Three Companies—It Stayed Silent for 7 Weeks
  - More Markets lending reserve drained for $410,000: Blockaid
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [andreysuperiorgit/aegis](https://github.com/andreysuperiorgit/aegis) — 0.82 stars/day
  - [hypnogaba/solana-signal-trader](https://github.com/hypnogaba/solana-signal-trader) — 0.04 stars/day
  - [KarloAldrete/universal-proxy](https://github.com/KarloAldrete/universal-proxy) — 0.02 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.9 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 8. Consumer & Social  —  confidence: Medium  (score 17.0)

- GitHub repos matching: **6**  (top velocity 1.04 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Robinhood CEO Says Crypto Will Beat Sports at Prediction Markets' Own Game
  - Sony Says You Don't Own the Games You Bought. Crypto Says It Can Fix That

  Top repos:
  - [blueshift-gg/solana-awesome](https://github.com/blueshift-gg/solana-awesome) — 0.43 stars/day
  - [accretion-xyz/awesome-solana-security](https://github.com/accretion-xyz/awesome-solana-security) — 0.23 stars/day
  - [dizcorvus/opencatz-ai](https://github.com/dizcorvus/opencatz-ai) — 0.2 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 6 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.
