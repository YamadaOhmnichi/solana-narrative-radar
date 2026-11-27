# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-27T08:36:27+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 149.6)

- GitHub repos matching: **47**  (top velocity 93.6 stars/day)
- Headline mentions (last fortnight): **7**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - UK Regulator Cites Binance Hack as It Plans Tougher DeFi Rules Than US and EU: Report
  - BNB Chain details new layer-1 for trading, private finance and AI

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 13.91 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 13.91 stars/day
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 13.5 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 47 trading-infrastructure repos at 93.6 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (7 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Dev Tooling & Infra  —  confidence: Medium  (score 94.8)

- GitHub repos matching: **55**  (top velocity 94.75 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 13.91 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 13.91 stars/day
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 13.5 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 55 tooling repos at 94.75 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 3. Meme & Speculation  —  confidence: Medium  (score 78.3)

- GitHub repos matching: **18**  (top velocity 77.78 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-0.28%**
- Cross-source confirmation: **1/3**

  Top repos:
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 13.91 stars/day
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 13.5 stars/day
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 13.25 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -0.28%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -0.28% so traders see which launches have real retention vs. pure rotation.

### 4. Wallets & UX  —  confidence: High  (score 72.7)

- GitHub repos matching: **20**  (top velocity 56.68 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 13.91 stars/day
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 13.25 stars/day
  - [arnabbhowmik07/Ghost](https://github.com/arnabbhowmik07/Ghost) — 8.29 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 20 new wallet/onboarding repos at 56.68 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 5. AI Agents on Solana  —  confidence: High  (score 65.4)

- GitHub repos matching: **20**  (top velocity 41.42 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Before the Sell-Off, AI Stocks Showed Dot-Com-Level Bubble Signals: Study
  - Cournot Raises $5M to Build AI-Native Oracle for Verifiable Intelligence
  - BNB Chain details new layer-1 for trading, private finance and AI

  Top repos:
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 13.91 stars/day
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 13.25 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 4.25 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 41.42 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in farzanamustafa936-dot/solana-pump-fun-sniper-bot-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. Security & Threats  —  confidence: High  (score 44.7)

- GitHub repos matching: **8**  (top velocity 4.73 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Standard Chartered's Zodia Custody Says Hackers Accessed Client Contact Details
  - UK Regulator Cites Binance Hack as It Plans Tougher DeFi Rules Than US and EU: Report

  Top repos:
  - [GuiBibeau/artex-program](https://github.com/GuiBibeau/artex-program) — 3.0 stars/day
  - [getkenning/kenning](https://github.com/getkenning/kenning) — 0.96 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.2 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 4.73 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (5 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. Payments & Stablecoins  —  confidence: High  (score 25.4)

- GitHub repos matching: **6**  (top velocity 9.39 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Japan’s SBI, SMFG launch Solana venture for stablecoins, tokenization
  - Zelle picks Solana for ZelleUSD stablecoin and international payments

  Top repos:
  - [arnabbhowmik07/Ghost](https://github.com/arnabbhowmik07/Ghost) — 8.29 stars/day
  - [makedotfun/prize-escrow](https://github.com/makedotfun/prize-escrow) — 0.34 stars/day
  - [orrery-node/orrery](https://github.com/orrery-node/orrery) — 0.29 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. Consumer & Social  —  confidence: Medium  (score 24.3)

- GitHub repos matching: **5**  (top velocity 16.33 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Vibecoded GTA 6 PC Ports Are Now Rendering In-Game Graphics Despite Take-Two Crackdown

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 13.25 stars/day
  - [nibblescreative-afk/darkseek](https://github.com/nibblescreative-afk/darkseek) — 1.5 stars/day
  - [askglyph/glyph](https://github.com/askglyph/glyph) — 1.29 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 5 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.
