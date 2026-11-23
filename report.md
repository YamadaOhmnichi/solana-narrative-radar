# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-23T07:41:13+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 1119.7)

- GitHub repos matching: **45**  (top velocity 1079.72 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Bitcoin Breaks Below $60K as Crypto Fear Index Hits Worst Level Since February
  - Ethereum’s new DeFi security tool raises questions over censorship

  Top repos:
  - [mykarenlo-work85/polymarket-trading-arbitrage-bot](https://github.com/mykarenlo-work85/polymarket-trading-arbitrage-bot) — 138.0 stars/day
  - [v-nancythom-r84/solana-pump-fun-jito-bundler](https://github.com/v-nancythom-r84/solana-pump-fun-jito-bundler) — 137.0 stars/day
  - [kevin-techeng95w9/solana-pump-fun-jito-bundler-portable](https://github.com/kevin-techeng95w9/solana-pump-fun-jito-bundler-portable) — 136.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 45 trading-infrastructure repos at 1079.72 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Dev Tooling & Infra  —  confidence: Medium  (score 981.7)

- GitHub repos matching: **57**  (top velocity 981.72 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [mykarenlo-work85/polymarket-trading-arbitrage-bot](https://github.com/mykarenlo-work85/polymarket-trading-arbitrage-bot) — 138.0 stars/day
  - [v-nancythom-r84/solana-pump-fun-jito-bundler](https://github.com/v-nancythom-r84/solana-pump-fun-jito-bundler) — 137.0 stars/day
  - [kevin-techeng95w9/solana-pump-fun-jito-bundler-portable](https://github.com/kevin-techeng95w9/solana-pump-fun-jito-bundler-portable) — 136.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 57 tooling repos at 981.72 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 3. Meme & Speculation  —  confidence: High  (score 976.7)

- GitHub repos matching: **22**  (top velocity 965.93 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-5.4%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [v-nancythom-r84/solana-pump-fun-jito-bundler](https://github.com/v-nancythom-r84/solana-pump-fun-jito-bundler) — 137.0 stars/day
  - [kevin-techeng95w9/solana-pump-fun-jito-bundler-portable](https://github.com/kevin-techeng95w9/solana-pump-fun-jito-bundler-portable) — 136.0 stars/day
  - [nikita-berg-io2090h6/solana-pump-fun-jito-bundler-pro](https://github.com/nikita-berg-io2090h6/solana-pump-fun-jito-bundler-pro) — 135.0 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -5.4%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -5.4% so traders see which launches have real retention vs. pure rotation.

### 4. Wallets & UX  —  confidence: High  (score 639.0)

- GitHub repos matching: **23**  (top velocity 623.04 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [v-nancythom-r84/solana-pump-fun-jito-bundler](https://github.com/v-nancythom-r84/solana-pump-fun-jito-bundler) — 137.0 stars/day
  - [kevin-techeng95w9/solana-pump-fun-jito-bundler-portable](https://github.com/kevin-techeng95w9/solana-pump-fun-jito-bundler-portable) — 136.0 stars/day
  - [nikita-berg-io2090h6/solana-pump-fun-jito-bundler-pro](https://github.com/nikita-berg-io2090h6/solana-pump-fun-jito-bundler-pro) — 135.0 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 23 new wallet/onboarding repos at 623.04 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 5. AI Agents on Solana  —  confidence: High  (score 228.7)

- GitHub repos matching: **19**  (top velocity 196.69 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Signal Calls OS-Level AI an 'Existential Threat' and Blocks Screenshots to Fight It
  - Is the AI Bubble Finally Popping? Nvidia Crashes 48% as Wall Street Experts Sound the Alarm
  - Google Gives Gemini Control of Mac Apps, But Its New AI Agent Comes With Risks

  Top repos:
  - [nikitasio1997h6/gmgn-bullx-copytrade-bot-2026](https://github.com/nikitasio1997h6/gmgn-bullx-copytrade-bot-2026) — 131.0 stars/day
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 33.0 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 21.86 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 196.69 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in nikitasio1997h6/gmgn-bullx-copytrade-bot-2026-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. Security & Threats  —  confidence: High  (score 156.8)

- GitHub repos matching: **7**  (top velocity 132.85 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Wrapped Monero Token Collapses 99% After $13 Million Hack Blamed on Web Host
  - Crypto hack losses equal 57 cents per $1 earned onchain: Ark’s Valente

  Top repos:
  - [nikitasio1997h6/gmgn-bullx-copytrade-bot-2026](https://github.com/nikitasio1997h6/gmgn-bullx-copytrade-bot-2026) — 131.0 stars/day
  - [getkenning/kenning](https://github.com/getkenning/kenning) — 0.95 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.33 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 132.85 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. Consumer & Social  —  confidence: Medium  (score 45.9)

- GitHub repos matching: **4**  (top velocity 37.94 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Google's Quantum Chip Beats Classical Limits in 'Impossible' Game

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 33.0 stars/day
  - [nibblescreative-afk/darkseek](https://github.com/nibblescreative-afk/darkseek) — 4.5 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.33 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 4 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.

### 8. DePIN & Physical Infra  —  confidence: Medium  (score 21.9)

- GitHub repos matching: **1**  (top velocity 21.86 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 21.86 stars/day

  **Build ideas:**
  - DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet (1 repos, Medium confidence).
  - Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.
  - Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.
