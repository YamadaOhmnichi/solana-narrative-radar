# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-24T09:55:48+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 1273.0)

- GitHub repos matching: **43**  (top velocity 1233.0 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Perps and Swaps: How to Trade the News on Decrypt
  - Ethereum’s new DeFi security tool raises questions over censorship

  Top repos:
  - [lucast752/polymarket-trading-arbitrage-bot](https://github.com/lucast752/polymarket-trading-arbitrage-bot) — 141.0 stars/day
  - [fathommillet/raydium-meteora-sniper-bot](https://github.com/fathommillet/raydium-meteora-sniper-bot) — 135.0 stars/day
  - [Alice34742/profanity2-evm-solana-vanity-gen](https://github.com/Alice34742/profanity2-evm-solana-vanity-gen) — 132.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 43 trading-infrastructure repos at 1233.0 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Dev Tooling & Infra  —  confidence: Medium  (score 1233.0)

- GitHub repos matching: **65**  (top velocity 1233.0 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [lucast752/polymarket-trading-arbitrage-bot](https://github.com/lucast752/polymarket-trading-arbitrage-bot) — 141.0 stars/day
  - [fathommillet/raydium-meteora-sniper-bot](https://github.com/fathommillet/raydium-meteora-sniper-bot) — 135.0 stars/day
  - [Alice34742/profanity2-evm-solana-vanity-gen](https://github.com/Alice34742/profanity2-evm-solana-vanity-gen) — 132.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 65 tooling repos at 1233.0 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 3. Meme & Speculation  —  confidence: High  (score 1168.4)

- GitHub repos matching: **20**  (top velocity 1148.0 stars/day)
- Headline mentions (last fortnight): **1**
- Market 7d avg change: **-6.18%**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - GPU Jesus Has Risen: Jensen Huang’s Nvidia Comeback Gets a Meme Parade

  Top repos:
  - [fathommillet/raydium-meteora-sniper-bot](https://github.com/fathommillet/raydium-meteora-sniper-bot) — 135.0 stars/day
  - [andreahasegawa2558/solana-pump-fun-jito-bundler](https://github.com/andreahasegawa2558/solana-pump-fun-jito-bundler) — 126.0 stars/day
  - [barbara92780/solana-pump-fun-jito-bundler](https://github.com/barbara92780/solana-pump-fun-jito-bundler) — 122.0 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -6.18%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -6.18% so traders see which launches have real retention vs. pure rotation.

### 4. Wallets & UX  —  confidence: High  (score 964.1)

- GitHub repos matching: **16**  (top velocity 948.12 stars/day)
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
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 16 new wallet/onboarding repos at 948.12 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 5. DePIN & Physical Infra  —  confidence: Medium  (score 254.1)

- GitHub repos matching: **3**  (top velocity 254.12 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [lieve2338/electrum-wallet-password-recovery](https://github.com/lieve2338/electrum-wallet-password-recovery) — 123.0 stars/day
  - [luukalexiou4715/hashcat-wallet-dat-recovery-cuda](https://github.com/luukalexiou4715/hashcat-wallet-dat-recovery-cuda) — 112.0 stars/day
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 19.12 stars/day

  **Build ideas:**
  - DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet (3 repos, Medium confidence).
  - Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.
  - Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.

### 6. AI Agents on Solana  —  confidence: High  (score 60.5)

- GitHub repos matching: **10**  (top velocity 28.45 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - China's Z.ai Says Its New AI Model Can Think Like One Four Times Its Size
  - OpenAI Will Pay You Up to $8K to Preach the AI Gospel to Small Businesses
  - Why One Math Proof Has AI Experts Warning Humans Might Soon Lose Control

  Top repos:
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 19.12 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 4.46 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 3.5 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 28.45 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in farzanamustafa936-dot/solana-pump-fun-sniper-bot-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 7. Security & Threats  —  confidence: Medium  (score 24.7)

- GitHub repos matching: **4**  (top velocity 0.68 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - North Korea Moves $247 Million of Binance Hack Loot Through Bitcoin Mixers
  - Crypto hack losses equal 57 cents per $1 earned onchain: Ark’s Valente

  Top repos:
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.29 stars/day
  - [Phat1911/Tributary](https://github.com/Phat1911/Tributary) — 0.2 stars/day
  - [RedDuckTeam/redduck-solana-audit](https://github.com/RedDuckTeam/redduck-solana-audit) — 0.12 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.68 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 8. RWA & Tokenization  —  confidence: Medium  (score 16.5)

- GitHub repos matching: **3**  (top velocity 0.54 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Mirae Asset Securities issues tokenized notes on Solana
  - RWA protocol stUSDT winds down 3 years after $2.3B TVL peak

  Top repos:
  - [FoundationStoneAlgorithms/TokenWork](https://github.com/FoundationStoneAlgorithms/TokenWork) — 0.4 stars/day
  - [Hymetdotfun/hymet](https://github.com/Hymetdotfun/hymet) — 0.1 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.04 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (3 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.
