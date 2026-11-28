# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-28T07:51:14+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 791.6)

- GitHub repos matching: **49**  (top velocity 735.6 stars/day)
- Headline mentions (last fortnight): **7**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Bluefin to shut down perps, refocus on spot trading and tokenized RWAs
  - BNB Chain details new layer-1 for trading, private finance and AI

  Top repos:
  - [Alessio87221/solana-sniper-bot](https://github.com/Alessio87221/solana-sniper-bot) — 169.0 stars/day
  - [samrasmail681-sys/solana-pump-fun-sniper-bot](https://github.com/samrasmail681-sys/solana-pump-fun-sniper-bot) — 142.0 stars/day
  - [ademgokce1/solana-token-swap-tutorial](https://github.com/ademgokce1/solana-token-swap-tutorial) — 141.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 49 trading-infrastructure repos at 735.6 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (7 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Dev Tooling & Infra  —  confidence: Medium  (score 639.3)

- GitHub repos matching: **55**  (top velocity 639.31 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [martins3793/trojan-on-solana-cli-suite](https://github.com/martins3793/trojan-on-solana-cli-suite) — 186.0 stars/day
  - [samrasmail681-sys/solana-pump-fun-sniper-bot](https://github.com/samrasmail681-sys/solana-pump-fun-sniper-bot) — 142.0 stars/day
  - [ademgokce1/solana-token-swap-tutorial](https://github.com/ademgokce1/solana-token-swap-tutorial) — 141.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 55 tooling repos at 639.31 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 3. Meme & Speculation  —  confidence: High  (score 488.2)

- GitHub repos matching: **18**  (top velocity 471.62 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **8.31%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [Alessio87221/solana-sniper-bot](https://github.com/Alessio87221/solana-sniper-bot) — 169.0 stars/day
  - [samrasmail681-sys/solana-pump-fun-sniper-bot](https://github.com/samrasmail681-sys/solana-pump-fun-sniper-bot) — 142.0 stars/day
  - [mudhinpc-droid/solana-memecoin-pump-fun-volume-booster-befalen](https://github.com/mudhinpc-droid/solana-memecoin-pump-fun-volume-booster-befalen) — 118.0 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change 8.31%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change 8.31% so traders see which launches have real retention vs. pure rotation.

### 4. AI Agents on Solana  —  confidence: High  (score 191.0)

- GitHub repos matching: **19**  (top velocity 167.02 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Could AI Break Bitcoin? Not Yet, Research Firm K33 Says
  - AI-Powered GTA 6 PC Ports Now Have Multiplayer as Modders Unlock 30 and 60 FPS
  - BNB Chain details new layer-1 for trading, private finance and AI

  Top repos:
  - [samrasmail681-sys/solana-pump-fun-sniper-bot](https://github.com/samrasmail681-sys/solana-pump-fun-sniper-bot) — 142.0 stars/day
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 13.38 stars/day
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 4.18 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 167.02 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in samrasmail681-sys/solana-pump-fun-sniper-bot-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 5. Security & Threats  —  confidence: High  (score 185.7)

- GitHub repos matching: **9**  (top velocity 145.66 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Hackers Hit US Air Force Cloud System Running Air-Defense and Munitions Data
  - Binance Fully Lifts Withdrawal Suspension Four Weeks After $6.4B Hack

  Top repos:
  - [samrasmail681-sys/solana-pump-fun-sniper-bot](https://github.com/samrasmail681-sys/solana-pump-fun-sniper-bot) — 142.0 stars/day
  - [GuiBibeau/artex-program](https://github.com/GuiBibeau/artex-program) — 2.0 stars/day
  - [getkenning/kenning](https://github.com/getkenning/kenning) — 0.94 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 145.66 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (5 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 6. Wallets & UX  —  confidence: Medium  (score 47.8)

- GitHub repos matching: **19**  (top velocity 39.83 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 13.38 stars/day
  - [arnabbhowmik07/Ghost](https://github.com/arnabbhowmik07/Ghost) — 7.38 stars/day
  - [miloslavatangen/Checker-Mnemonic](https://github.com/miloslavatangen/Checker-Mnemonic) — 6.06 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 19 new wallet/onboarding repos at 39.83 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 1 this period — users clearly need guardrails).

### 7. Payments & Stablecoins  —  confidence: High  (score 24.5)

- GitHub repos matching: **7**  (top velocity 8.47 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Japan’s SBI, SMFG launch Solana venture for stablecoins, tokenization
  - Zelle picks Solana for ZelleUSD stablecoin and international payments

  Top repos:
  - [arnabbhowmik07/Ghost](https://github.com/arnabbhowmik07/Ghost) — 7.38 stars/day
  - [makedotfun/prize-escrow](https://github.com/makedotfun/prize-escrow) — 0.33 stars/day
  - [orrery-node/orrery](https://github.com/orrery-node/orrery) — 0.27 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. RWA & Tokenization  —  confidence: Medium  (score 24.4)

- GitHub repos matching: **4**  (top velocity 0.38 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Japan’s SBI, SMFG launch Solana venture for stablecoins, tokenization
  - Bluefin to shut down perps, refocus on spot trading and tokenized RWAs
  - RWA protocol stUSDT winds down 3 years after $2.3B TVL peak

  Top repos:
  - [FoundationStoneAlgorithms/TokenWork](https://github.com/FoundationStoneAlgorithms/TokenWork) — 0.22 stars/day
  - [Hymetdotfun/hymet](https://github.com/Hymetdotfun/hymet) — 0.08 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.04 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (4 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.
