# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-25T08:37:01+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 1198.0)

- GitHub repos matching: **51**  (top velocity 1174.0 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Ethereum’s new DeFi security tool raises questions over censorship
  - EU DeFi proposals could push users to riskier platforms, says Coinbase exec

  Top repos:
  - [Norao01/solana-pump-fun-jito-bundler-sniper](https://github.com/Norao01/solana-pump-fun-jito-bundler-sniper) — 187.0 stars/day
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 176.0 stars/day
  - [rajmyers29/jupiter-v6-atomic-arbitrage-bot](https://github.com/rajmyers29/jupiter-v6-atomic-arbitrage-bot) — 172.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 51 trading-infrastructure repos at 1174.0 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (3 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Meme & Speculation  —  confidence: High  (score 679.1)

- GitHub repos matching: **22**  (top velocity 643.0 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **-10.03%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - What Is Pons? The Robinhood Chain Meme Coin Launchpad Explained
  - Ansem Meme Coin Crashes After $2.57 Million Wallet Drain, Bullpen Confirms Security Breach

  Top repos:
  - [Norao01/solana-pump-fun-jito-bundler-sniper](https://github.com/Norao01/solana-pump-fun-jito-bundler-sniper) — 187.0 stars/day
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 176.0 stars/day
  - [ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot](https://github.com/ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot) — 38.0 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -10.03%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -10.03% so traders see which launches have real retention vs. pure rotation.

### 3. Dev Tooling & Infra  —  confidence: Medium  (score 656.0)

- GitHub repos matching: **64**  (top velocity 656.0 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [Norao01/solana-pump-fun-jito-bundler-sniper](https://github.com/Norao01/solana-pump-fun-jito-bundler-sniper) — 187.0 stars/day
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 176.0 stars/day
  - [Truong81752/trust-wallet-metamask-seed-recovery-v3](https://github.com/Truong81752/trust-wallet-metamask-seed-recovery-v3) — 38.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 64 tooling repos at 656.0 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 4. AI Agents on Solana  —  confidence: High  (score 278.3)

- GitHub repos matching: **15**  (top velocity 246.31 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - OpenAI and Anthropic Insiders Fear Their Next AI Models Are Too Dangerous to Release
  - Anthropic’s Claude Ship Lets AI Write, Review and Approve Its Own Code
  - Ethereum Foundation Says AI Is a More Urgent Threat Than Quantum Computing

  Top repos:
  - [bettysuzuki/okx-agent-trade-kit-mcp-grid-dca-bot](https://github.com/bettysuzuki/okx-agent-trade-kit-mcp-grid-dca-bot) — 130.0 stars/day
  - [ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot](https://github.com/ivanmustafa/gmgn-ai-bullx-solana-copytrade-bot) — 38.0 stars/day
  - [janalvarez166/freqtrade-2026-ai-ml-strategies](https://github.com/janalvarez166/freqtrade-2026-ai-ml-strategies) — 34.0 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 246.31 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in bettysuzuki/okx-agent-trade-kit-mcp-grid-dca-bot-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 5. Wallets & UX  —  confidence: High  (score 227.1)

- GitHub repos matching: **14**  (top velocity 203.1 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - Ansem Meme Coin Crashes After $2.57 Million Wallet Drain, Bullpen Confirms Security Breach
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [Truong81752/trust-wallet-metamask-seed-recovery-v3](https://github.com/Truong81752/trust-wallet-metamask-seed-recovery-v3) — 38.0 stars/day
  - [sidorov4181/trust-wallet-metamask-seed-recovery-pc](https://github.com/sidorov4181/trust-wallet-metamask-seed-recovery-pc) — 38.0 stars/day
  - [FolunuSayu33/trust-wallet-metamask-seed-recovery-win11](https://github.com/FolunuSayu33/trust-wallet-metamask-seed-recovery-win11) — 36.0 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 14 new wallet/onboarding repos at 203.1 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 3 this period — users clearly need guardrails).

### 6. Security & Threats  —  confidence: Medium  (score 41.6)

- GitHub repos matching: **5**  (top velocity 1.58 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Coldcard Bitcoin Exploit, Revisited: How a Hidden Flaw Survived Years of Audits
  - Ansem Meme Coin Crashes After $2.57 Million Wallet Drain, Bullpen Confirms Security Breach

  Top repos:
  - [getkenning/kenning](https://github.com/getkenning/kenning) — 0.96 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.25 stars/day
  - [Phat1911/Tributary](https://github.com/Phat1911/Tributary) — 0.2 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 1.58 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (5 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. Consumer & Social  —  confidence: Medium  (score 19.9)

- GitHub repos matching: **4**  (top velocity 19.93 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 17.33 stars/day
  - [nibblescreative-afk/darkseek](https://github.com/nibblescreative-afk/darkseek) — 2.25 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.25 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 4 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.

### 8. Payments & Stablecoins  —  confidence: Medium  (score 17.1)

- GitHub repos matching: **5**  (top velocity 1.15 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Zelle picks Solana for ZelleUSD stablecoin and international payments
  - Justice Department Moves to Forfeit $1.1B in USDC From North Korea's Binance Hack

  Top repos:
  - [orrery-node/orrery](https://github.com/orrery-node/orrery) — 0.32 stars/day
  - [makedotfun/prize-escrow](https://github.com/makedotfun/prize-escrow) — 0.3 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.25 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.
