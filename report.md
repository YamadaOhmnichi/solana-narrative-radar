# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-15T18:52:25+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 492.6)

- GitHub repos matching: **49**  (top velocity 452.56 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - EU DeFi proposals could push users to riskier platforms, says Coinbase exec
  - The UK needs a workable route to regulated DeFi access

  Top repos:
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 50.0 stars/day
  - [NikubfrostPixel62446/Solana-Token-rpocket-Swap-Tutorial](https://github.com/NikubfrostPixel62446/Solana-Token-rpocket-Swap-Tutorial) — 50.0 stars/day
  - [ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket](https://github.com/ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket) — 50.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 49 trading-infrastructure repos at 452.56 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. AI Agents on Solana  —  confidence: High  (score 362.0)

- GitHub repos matching: **28**  (top velocity 313.96 stars/day)
- Headline mentions (last fortnight): **6**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - OpenAI, Anthropic, Google and Other AI Giants Face Lawsuit Demanding Development Freeze
  - OpenAI Launches ChatGPT Wallet to Let AI Agents Shop—Without Crypto

  Top repos:
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 50.0 stars/day
  - [Novaograge12557/Solana-AI-resp-Agent-Multimodal](https://github.com/Novaograge12557/Solana-AI-resp-Agent-Multimodal) — 50.0 stars/day
  - [ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket](https://github.com/ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket) — 50.0 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 313.96 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in Savageworks/solana-resp-trader-client-go-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 3. Dev Tooling & Infra  —  confidence: Medium  (score 339.8)

- GitHub repos matching: **52**  (top velocity 339.75 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 50.0 stars/day
  - [NikubfrostPixel62446/Solana-Token-rpocket-Swap-Tutorial](https://github.com/NikubfrostPixel62446/Solana-Token-rpocket-Swap-Tutorial) — 50.0 stars/day
  - [ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket](https://github.com/ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket) — 50.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 52 tooling repos at 339.75 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 4. Wallets & UX  —  confidence: High  (score 246.7)

- GitHub repos matching: **20**  (top velocity 214.74 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - OpenAI Launches ChatGPT Wallet to Let AI Agents Shop—Without Crypto
  - Dormant Bitcoin Wallets Wake Up After 16 Years, Moving $6.9 Million

  Top repos:
  - [Novaograge12557/Solana-AI-resp-Agent-Multimodal](https://github.com/Novaograge12557/Solana-AI-resp-Agent-Multimodal) — 50.0 stars/day
  - [AethForgeice25459/rugcheck-respocket-ai](https://github.com/AethForgeice25459/rugcheck-respocket-ai) — 50.0 stars/day
  - [CryAceocean/solgov-rpocket-team](https://github.com/CryAceocean/solgov-rpocket-team) — 50.0 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 20 new wallet/onboarding repos at 214.74 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 4 this period — users clearly need guardrails).

### 5. Meme & Speculation  —  confidence: High  (score 198.8)

- GitHub repos matching: **15**  (top velocity 164.44 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-17.2%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket](https://github.com/ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket) — 50.0 stars/day
  - [WolfUntilangel/sentry-bot-resp](https://github.com/WolfUntilangel/sentry-bot-resp) — 50.0 stars/day
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 26.33 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -17.2%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -17.2% so traders see which launches have real retention vs. pure rotation.

### 6. Security & Threats  —  confidence: High  (score 167.3)

- GitHub repos matching: **11**  (top velocity 151.35 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Crypto hack losses equal 57 cents per $1 earned onchain: Ark’s Valente

  Top repos:
  - [ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket](https://github.com/ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket) — 50.0 stars/day
  - [AethForgeice25459/rugcheck-respocket-ai](https://github.com/AethForgeice25459/rugcheck-respocket-ai) — 50.0 stars/day
  - [CryAceocean/solgov-rpocket-team](https://github.com/CryAceocean/solgov-rpocket-team) — 50.0 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 151.35 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (2 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. Payments & Stablecoins  —  confidence: Medium  (score 115.7)

- GitHub repos matching: **9**  (top velocity 107.7 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain

  Top repos:
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 50.0 stars/day
  - [FireDrakridge/vli.su.rpocket](https://github.com/FireDrakridge/vli.su.rpocket) — 50.0 stars/day
  - [ismeh7765/FlashUSDT-v](https://github.com/ismeh7765/FlashUSDT-v) — 6.56 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. DePIN & Physical Infra  —  confidence: Medium  (score 101.8)

- GitHub repos matching: **3**  (top velocity 101.79 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [Novaograge12557/Solana-AI-resp-Agent-Multimodal](https://github.com/Novaograge12557/Solana-AI-resp-Agent-Multimodal) — 50.0 stars/day
  - [CryAceocean/solgov-rpocket-team](https://github.com/CryAceocean/solgov-rpocket-team) — 50.0 stars/day
  - [refrax-xyz/refrax-node](https://github.com/refrax-xyz/refrax-node) — 1.79 stars/day

  **Build ideas:**
  - DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet (3 repos, Medium confidence).
  - Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.
  - Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.
