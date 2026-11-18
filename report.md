# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-18T07:30:36+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Dev Tooling & Infra  —  confidence: Medium  (score 344.0)

- GitHub repos matching: **52**  (top velocity 344.04 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [s-warren725/solana-node-notes](https://github.com/s-warren725/solana-node-notes) — 100.0 stars/day
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 76.5 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 76.5 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 52 tooling repos at 344.04 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 2. DeFi / Trading Infra  —  confidence: High  (score 273.4)

- GitHub repos matching: **45**  (top velocity 225.37 stars/day)
- Headline mentions (last fortnight): **6**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Former Robinhood Engineer Pleads Guilty to Crypto Insider Trading Scheme
  - EU DeFi proposals could push users to riskier platforms, says Coinbase exec

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 76.5 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 76.5 stars/day
  - [ValidatorStack/solana-vigil](https://github.com/ValidatorStack/solana-vigil) — 32.86 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 45 trading-infrastructure repos at 225.37 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (6 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. Meme & Speculation  —  confidence: High  (score 170.9)

- GitHub repos matching: **15**  (top velocity 137.21 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-16.84%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 76.5 stars/day
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 17.44 stars/day
  - [chadandyou/jrames](https://github.com/chadandyou/jrames) — 8.64 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -16.84%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -16.84% so traders see which launches have real retention vs. pure rotation.

### 4. Wallets & UX  —  confidence: High  (score 154.1)

- GitHub repos matching: **21**  (top velocity 130.1 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - Binance Hack Wallets Move $137 Million in Ethereum After Two Weeks of Silence
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 76.5 stars/day
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 17.44 stars/day
  - [miloslavatangen/Checker-Mnemonic](https://github.com/miloslavatangen/Checker-Mnemonic) — 16.0 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 21 new wallet/onboarding repos at 130.1 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 3 this period — users clearly need guardrails).

### 5. AI Agents on Solana  —  confidence: High  (score 131.5)

- GitHub repos matching: **25**  (top velocity 107.5 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - Why Microsoft Thinks Smaller, Cheaper AI Can Beat Claude and GPT
  - Blockchain is ‘perfect solution’ for AI agent trust, VeChain CEO says

  Top repos:
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 76.5 stars/day
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 8.33 stars/day
  - [Novaograge12557/Solana-AI-resp-Agent-Multimodal](https://github.com/Novaograge12557/Solana-AI-resp-Agent-Multimodal) — 8.33 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 107.5 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in farzanamustafa936-dot/solana-pump-fun-sniper-bot-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. DePIN & Physical Infra  —  confidence: Medium  (score 86.5)

- GitHub repos matching: **3**  (top velocity 86.45 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 76.5 stars/day
  - [Novaograge12557/Solana-AI-resp-Agent-Multimodal](https://github.com/Novaograge12557/Solana-AI-resp-Agent-Multimodal) — 8.33 stars/day
  - [refrax-xyz/refrax-node](https://github.com/refrax-xyz/refrax-node) — 1.62 stars/day

  **Build ideas:**
  - DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet (3 repos, Medium confidence).
  - Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.
  - Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.

### 7. Payments & Stablecoins  —  confidence: High  (score 35.4)

- GitHub repos matching: **8**  (top velocity 19.39 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Zelle picks Solana for ZelleUSD stablecoin and international payments
  - World Bank Taps Circle and Citi to Test Stablecoins for Development Payments

  Top repos:
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 8.33 stars/day
  - [ismeh7765/FlashUSDT-v](https://github.com/ismeh7765/FlashUSDT-v) — 5.0 stars/day
  - [tommyg-dev/contingency](https://github.com/tommyg-dev/contingency) — 5.0 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. Security & Threats  —  confidence: High  (score 30.9)

- GitHub repos matching: **10**  (top velocity 6.91 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Binance Hack Wallets Move $137 Million in Ethereum After Two Weeks of Silence
  - Crypto hack losses equal 57 cents per $1 earned onchain: Ark’s Valente

  Top repos:
  - [tommyg-dev/contingency](https://github.com/tommyg-dev/contingency) — 5.0 stars/day
  - [PTK030/kenning](https://github.com/PTK030/kenning) — 0.87 stars/day
  - [Phat1911/Tributary](https://github.com/Phat1911/Tributary) — 0.24 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 6.91 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.
