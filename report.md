# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-20T07:18:14+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Dev Tooling & Infra  —  confidence: Medium  (score 241.3)

- GitHub repos matching: **55**  (top velocity 241.32 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 82.0 stars/day
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 38.25 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 38.25 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 55 tooling repos at 241.32 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 2. Meme & Speculation  —  confidence: High  (score 191.3)

- GitHub repos matching: **18**  (top velocity 162.48 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-14.41%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 82.0 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 38.25 stars/day
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 14.09 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -14.41%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -14.41% so traders see which launches have real retention vs. pure rotation.

### 3. AI Agents on Solana  —  confidence: High  (score 183.6)

- GitHub repos matching: **24**  (top velocity 143.57 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Citi Says Customers Are Responsible When AI Banking Agents Go Rogue—Even After a Hack
  - Protesters Arrested Outside Nasdaq as Activists Oppose Anthropic IPO Over AI Bubble Risks
  - Anthropic Stock Opens 33% Above IPO Price as AI Stocks Rally

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 82.0 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 38.25 stars/day
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 5.0 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 143.57 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in setyamickala/airdrop-agent-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 4. DeFi / Trading Infra  —  confidence: High  (score 175.9)

- GitHub repos matching: **46**  (top velocity 127.9 stars/day)
- Headline mentions (last fortnight): **6**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - What Are Perpetual Futures? How Crypto's Most Popular Derivative Works
  - Ethereum’s new DeFi security tool raises questions over censorship

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 38.25 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 38.25 stars/day
  - [ValidatorStack/solana-vigil](https://github.com/ValidatorStack/solana-vigil) — 25.22 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 46 trading-infrastructure repos at 127.9 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (6 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 5. Wallets & UX  —  confidence: High  (score 174.0)

- GitHub repos matching: **21**  (top velocity 158.02 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 82.0 stars/day
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 38.25 stars/day
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 14.09 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 21 new wallet/onboarding repos at 158.02 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 6. Consumer & Social  —  confidence: Medium  (score 83.9)

- GitHub repos matching: **3**  (top velocity 83.94 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 82.0 stars/day
  - [askglyph/glyph](https://github.com/askglyph/glyph) — 1.82 stars/day
  - [Hymetdotfun/hymet](https://github.com/Hymetdotfun/hymet) — 0.12 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 3 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.

### 7. DePIN & Physical Infra  —  confidence: Medium  (score 46.0)

- GitHub repos matching: **4**  (top velocity 46.02 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 38.25 stars/day
  - [Novaograge12557/Solana-AI-resp-Agent-Multimodal](https://github.com/Novaograge12557/Solana-AI-resp-Agent-Multimodal) — 5.0 stars/day
  - [refrax-xyz/refrax-node](https://github.com/refrax-xyz/refrax-node) — 1.48 stars/day

  **Build ideas:**
  - DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet (4 repos, Medium confidence).
  - Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.
  - Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.

### 8. Security & Threats  —  confidence: Medium  (score 35.0)

- GitHub repos matching: **8**  (top velocity 3.0 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Citi Says Customers Are Responsible When AI Banking Agents Go Rogue—Even After a Hack
  - Hackers Leak Visa, Mastercard and JPMorgan Customer Data

  Top repos:
  - [outgoingyang/solana-sniping-bot](https://github.com/outgoingyang/solana-sniping-bot) — 1.29 stars/day
  - [PTK030/kenning](https://github.com/PTK030/kenning) — 0.93 stars/day
  - [Phat1911/Tributary](https://github.com/Phat1911/Tributary) — 0.22 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 3.0 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (4 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.
