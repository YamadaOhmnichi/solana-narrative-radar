# Solana Narrative Radar — Fortnightly Report

Generated: 2026-09-24T12:34:25+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Wallets & UX  —  confidence: Medium  (score 127.1)

- GitHub repos matching: **20**  (top velocity 127.06 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [uni-launch/solana-token-creator](https://github.com/uni-launch/solana-token-creator) — 64.0 stars/day
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 29.38 stars/day
  - [Kylerkrausemdzyra64/Crypto-Checker](https://github.com/Kylerkrausemdzyra64/Crypto-Checker) — 14.67 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 20 new wallet/onboarding repos at 127.06 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 2. DeFi / Trading Infra  —  confidence: High  (score 94.4)

- GitHub repos matching: **47**  (top velocity 70.44 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Kraken brings DeFi yield to tokenized stocks and ETFs
  - Sui DeFi protocol Full Sail to wind down after Switchboard incident
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 29.38 stars/day
  - [Oryc11/Free-Demonstration-Guide](https://github.com/Oryc11/Free-Demonstration-Guide) — 19.0 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 6.62 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 47 trading-infrastructure repos at 70.44 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (3 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. Meme & Speculation  —  confidence: High  (score 90.1)

- GitHub repos matching: **13**  (top velocity 44.82 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **14.66%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - Fomo overtakes Pump.fun in daily revenue on Solana
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 33.62 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 3.66 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 3.6 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change 14.66%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change 14.66% so traders see which launches have real retention vs. pure rotation.

### 4. RWA & Tokenization  —  confidence: High  (score 78.1)

- GitHub repos matching: **6**  (top velocity 62.07 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Winners and losers of the SEC’s new tokenized stocks rules
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [coolbbcamp/Synthetic-Liquidity-Depth-Scanner](https://github.com/coolbbcamp/Synthetic-Liquidity-Depth-Scanner) — 32.25 stars/day
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 29.38 stars/day
  - [thesithunyein/owed](https://github.com/thesithunyein/owed) — 0.33 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (6 repos, High confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 5. Consumer & Social  —  confidence: Medium  (score 65.2)

- GitHub repos matching: **7**  (top velocity 65.21 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [uni-launch/solana-token-creator](https://github.com/uni-launch/solana-token-creator) — 64.0 stars/day
  - [blueshift-gg/solana-awesome](https://github.com/blueshift-gg/solana-awesome) — 0.42 stars/day
  - [livid/exe-hub](https://github.com/livid/exe-hub) — 0.4 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 7 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.

### 6. Dev Tooling & Infra  —  confidence: Medium  (score 57.8)

- GitHub repos matching: **43**  (top velocity 57.77 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 29.38 stars/day
  - [Oryc11/Free-Demonstration-Guide](https://github.com/Oryc11/Free-Demonstration-Guide) — 19.0 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 6.62 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 43 tooling repos at 57.77 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 7. Security & Threats  —  confidence: Medium  (score 32.1)

- GitHub repos matching: **3**  (top velocity 0.08 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Brooklyn Man Who Bragged About $16M Coinbase Scam Gets Up to 12 Years
  - An AI Agent Just Hacked a Government Website for the First Time, Australia PM Says
  - More Markets lending reserve drained for $410,000: Blockaid

  Top repos:
  - [hypnogaba/solana-signal-trader](https://github.com/hypnogaba/solana-signal-trader) — 0.04 stars/day
  - [KarloAldrete/universal-proxy](https://github.com/KarloAldrete/universal-proxy) — 0.02 stars/day
  - [leafwithered/clawledger](https://github.com/leafwithered/clawledger) — 0.02 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.08 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (4 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 8. AI Agents on Solana  —  confidence: High  (score 28.8)

- GitHub repos matching: **16**  (top velocity 4.76 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - An AI Agent Just Hacked a Government Website for the First Time, Australia PM Says
  - OpenAI Gives Ukraine Access to Daybreak AI Cyber-Defense Tool
  - Meta's Muse AI Agent Read a User's Private iMessages. Then It Lied About How

  Top repos:
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 1.29 stars/day
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 1.11 stars/day
  - [PillCrew/PillCrew](https://github.com/PillCrew/PillCrew) — 1.03 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 4.76 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in PillCrew/claimchain-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.
