# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-23T23:54:55+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 1358.0)

- GitHub repos matching: **41**  (top velocity 1318.0 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Perps and Swaps: How to Trade the News on Decrypt
  - Ethereum’s new DeFi security tool raises questions over censorship

  Top repos:
  - [lucast752/polymarket-trading-arbitrage-bot](https://github.com/lucast752/polymarket-trading-arbitrage-bot) — 139.0 stars/day
  - [VasitoTa77/birdeye-solana-whale-tracker-bot](https://github.com/VasitoTa77/birdeye-solana-whale-tracker-bot) — 136.0 stars/day
  - [aukhoney/hyperliquid-perp-market-maker-bot](https://github.com/aukhoney/hyperliquid-perp-market-maker-bot) — 136.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 41 trading-infrastructure repos at 1318.0 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Dev Tooling & Infra  —  confidence: Medium  (score 1318.0)

- GitHub repos matching: **63**  (top velocity 1318.0 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [lucast752/polymarket-trading-arbitrage-bot](https://github.com/lucast752/polymarket-trading-arbitrage-bot) — 139.0 stars/day
  - [VasitoTa77/birdeye-solana-whale-tracker-bot](https://github.com/VasitoTa77/birdeye-solana-whale-tracker-bot) — 136.0 stars/day
  - [aukhoney/hyperliquid-perp-market-maker-bot](https://github.com/aukhoney/hyperliquid-perp-market-maker-bot) — 136.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 63 tooling repos at 1318.0 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 3. Meme & Speculation  —  confidence: High  (score 1291.8)

- GitHub repos matching: **19**  (top velocity 1272.0 stars/day)
- Headline mentions (last fortnight): **1**
- Market 7d avg change: **-5.92%**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - GPU Jesus Has Risen: Jensen Huang’s Nvidia Comeback Gets a Meme Parade

  Top repos:
  - [VasitoTa77/birdeye-solana-whale-tracker-bot](https://github.com/VasitoTa77/birdeye-solana-whale-tracker-bot) — 136.0 stars/day
  - [fathommillet/raydium-meteora-sniper-bot](https://github.com/fathommillet/raydium-meteora-sniper-bot) — 135.0 stars/day
  - [MariviPa23/ave-ai-defined-fi-memecoin-sniper](https://github.com/MariviPa23/ave-ai-defined-fi-memecoin-sniper) — 130.0 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -5.92%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -5.92% so traders see which launches have real retention vs. pure rotation.

### 4. DePIN & Physical Infra  —  confidence: Medium  (score 515.1)

- GitHub repos matching: **5**  (top velocity 515.12 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [GuqaveVe86/btcrecover-multigpu-seed-scanner](https://github.com/GuqaveVe86/btcrecover-multigpu-seed-scanner) — 131.0 stars/day
  - [lieve2338/electrum-wallet-password-recovery](https://github.com/lieve2338/electrum-wallet-password-recovery) — 123.0 stars/day
  - [alessiokwon72/grass-dawn-gradient-depin-farm-bot](https://github.com/alessiokwon72/grass-dawn-gradient-depin-farm-bot) — 121.0 stars/day

  **Build ideas:**
  - DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet (5 repos, Medium confidence).
  - Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.
  - Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.

### 5. Wallets & UX  —  confidence: High  (score 424.7)

- GitHub repos matching: **11**  (top velocity 408.67 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [andreahasegawa2558/solana-pump-fun-jito-bundler](https://github.com/andreahasegawa2558/solana-pump-fun-jito-bundler) — 126.0 stars/day
  - [lieve2338/electrum-wallet-password-recovery](https://github.com/lieve2338/electrum-wallet-password-recovery) — 123.0 stars/day
  - [barbara92780/solana-pump-fun-jito-bundler](https://github.com/barbara92780/solana-pump-fun-jito-bundler) — 122.0 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 11 new wallet/onboarding repos at 408.67 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 6. Payments & Stablecoins  —  confidence: Medium  (score 251.2)

- GitHub repos matching: **7**  (top velocity 243.24 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Zelle picks Solana for ZelleUSD stablecoin and international payments

  Top repos:
  - [alessiokwon72/grass-dawn-gradient-depin-farm-bot](https://github.com/alessiokwon72/grass-dawn-gradient-depin-farm-bot) — 121.0 stars/day
  - [GuqaveVe86/grass-dawn-gradient-depin-farm-bot](https://github.com/GuqaveVe86/grass-dawn-gradient-depin-farm-bot) — 121.0 stars/day
  - [orrery-node/orrery](https://github.com/orrery-node/orrery) — 0.35 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 7. AI Agents on Solana  —  confidence: High  (score 190.4)

- GitHub repos matching: **11**  (top velocity 158.37 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - China's Z.ai Says Its New AI Model Can Think Like One Four Times Its Size
  - OpenAI Will Pay You Up to $8K to Preach the AI Gospel to Small Businesses
  - Why One Math Proof Has AI Experts Warning Humans Might Soon Lose Control

  Top repos:
  - [MariviPa23/ave-ai-defined-fi-memecoin-sniper](https://github.com/MariviPa23/ave-ai-defined-fi-memecoin-sniper) — 130.0 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 19.12 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 4.46 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 158.37 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in MariviPa23/ave-ai-defined-fi-memecoin-sniper-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 8. Security & Threats  —  confidence: High  (score 154.7)

- GitHub repos matching: **5**  (top velocity 130.72 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - North Korea Moves $247 Million of Binance Hack Loot Through Bitcoin Mixers
  - Crypto hack losses equal 57 cents per $1 earned onchain: Ark’s Valente

  Top repos:
  - [MariviPa23/ave-ai-defined-fi-memecoin-sniper](https://github.com/MariviPa23/ave-ai-defined-fi-memecoin-sniper) — 130.0 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.33 stars/day
  - [Phat1911/Tributary](https://github.com/Phat1911/Tributary) — 0.2 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 130.72 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.
