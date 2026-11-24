# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-24T22:28:05+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 1121.0)

- GitHub repos matching: **49**  (top velocity 1097.0 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Ethereum’s new DeFi security tool raises questions over censorship
  - EU DeFi proposals could push users to riskier platforms, says Coinbase exec

  Top repos:
  - [ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot](https://github.com/ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot) — 114.0 stars/day
  - [Truong81752/trust-wallet-metamask-seed-recovery-v3](https://github.com/Truong81752/trust-wallet-metamask-seed-recovery-v3) — 112.0 stars/day
  - [haechandeluca864/gmgn-bullx-photon-copytrade-bot-v3](https://github.com/haechandeluca864/gmgn-bullx-photon-copytrade-bot-v3) — 110.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 49 trading-infrastructure repos at 1097.0 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (3 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Meme & Speculation  —  confidence: High  (score 1114.1)

- GitHub repos matching: **22**  (top velocity 1080.0 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **-9.07%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - What Is Pons? The Robinhood Chain Meme Coin Launchpad Explained
  - Ansem Meme Coin Crashes After $2.57 Million Wallet Drain, Bullpen Confirms Security Breach

  Top repos:
  - [ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot](https://github.com/ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot) — 114.0 stars/day
  - [GerhardKlein0995/module-on-solana-sniper-bot](https://github.com/GerhardKlein0995/module-on-solana-sniper-bot) — 109.0 stars/day
  - [dmitry-k-code19w1/raydium-meteora-sniper-bot-x64](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64) — 109.0 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -9.07%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -9.07% so traders see which launches have real retention vs. pure rotation.

### 3. Dev Tooling & Infra  —  confidence: Medium  (score 1088.0)

- GitHub repos matching: **67**  (top velocity 1088.0 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [Truong81752/trust-wallet-metamask-seed-recovery-v3](https://github.com/Truong81752/trust-wallet-metamask-seed-recovery-v3) — 112.0 stars/day
  - [haechandeluca864/gmgn-bullx-photon-copytrade-bot-v3](https://github.com/haechandeluca864/gmgn-bullx-photon-copytrade-bot-v3) — 110.0 stars/day
  - [GerhardKlein0995/module-on-solana-sniper-bot](https://github.com/GerhardKlein0995/module-on-solana-sniper-bot) — 109.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 67 tooling repos at 1088.0 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 4. Wallets & UX  —  confidence: High  (score 597.6)

- GitHub repos matching: **13**  (top velocity 573.57 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - Ansem Meme Coin Crashes After $2.57 Million Wallet Drain, Bullpen Confirms Security Breach
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [Truong81752/trust-wallet-metamask-seed-recovery-v3](https://github.com/Truong81752/trust-wallet-metamask-seed-recovery-v3) — 112.0 stars/day
  - [Eces381/seed-phrase-balance-checker-multichain](https://github.com/Eces381/seed-phrase-balance-checker-multichain) — 109.0 stars/day
  - [misasimmons/solana-pump-fun-jito-bundler-bot](https://github.com/misasimmons/solana-pump-fun-jito-bundler-bot) — 107.0 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 13 new wallet/onboarding repos at 573.57 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 3 this period — users clearly need guardrails).

### 5. AI Agents on Solana  —  confidence: High  (score 378.9)

- GitHub repos matching: **13**  (top velocity 354.89 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Anthropic’s Claude Ship Lets AI Write, Review and Approve Its Own Code
  - Ethereum Foundation Says AI Is a More Urgent Threat Than Quantum Computing
  - Blockchain is ‘perfect solution’ for AI agent trust, VeChain CEO says

  Top repos:
  - [ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot](https://github.com/ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot) — 114.0 stars/day
  - [janalvarez166/freqtrade-2026-ai-ml-strategies](https://github.com/janalvarez166/freqtrade-2026-ai-ml-strategies) — 108.0 stars/day
  - [JohanRonto570/ave-ai-defined-fi-memecoin-sniper](https://github.com/JohanRonto570/ave-ai-defined-fi-memecoin-sniper) — 107.0 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 354.89 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. Security & Threats  —  confidence: Medium  (score 40.7)

- GitHub repos matching: **4**  (top velocity 0.67 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Coldcard Bitcoin Exploit, Revisited: How a Hidden Flaw Survived Years of Audits
  - Ansem Meme Coin Crashes After $2.57 Million Wallet Drain, Bullpen Confirms Security Breach

  Top repos:
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.29 stars/day
  - [Phat1911/Tributary](https://github.com/Phat1911/Tributary) — 0.2 stars/day
  - [RedDuckTeam/redduck-solana-audit](https://github.com/RedDuckTeam/redduck-solana-audit) — 0.12 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.67 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (5 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. Payments & Stablecoins  —  confidence: Medium  (score 17.2)

- GitHub repos matching: **5**  (top velocity 1.17 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Zelle picks Solana for ZelleUSD stablecoin and international payments
  - Justice Department Moves to Forfeit $1.1B in USDC From North Korea's Binance Hack

  Top repos:
  - [orrery-node/orrery](https://github.com/orrery-node/orrery) — 0.33 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.29 stars/day
  - [makedotfun/prize-escrow](https://github.com/makedotfun/prize-escrow) — 0.26 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. DePIN & Physical Infra  —  confidence: Medium  (score 17.0)

- GitHub repos matching: **1**  (top velocity 17.0 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 17.0 stars/day

  **Build ideas:**
  - DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet (1 repos, Medium confidence).
  - Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.
  - Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.
