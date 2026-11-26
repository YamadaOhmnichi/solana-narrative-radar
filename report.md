# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-26T08:20:27+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 331.9)

- GitHub repos matching: **46**  (top velocity 291.86 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - The 1Password Breach Didn’t Touch Your Vault. The Phishing Emails Might
  - UK regulator plans tighter DeFi rules, citing $6.3B Binance hack: Report

  Top repos:
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 63.0 stars/day
  - [Norao01/solana-pump-fun-jito-bundler-sniper](https://github.com/Norao01/solana-pump-fun-jito-bundler-sniper) — 59.0 stars/day
  - [dianenelson33/kalshi-polymarket-cross-exchange-arb-bot](https://github.com/dianenelson33/kalshi-polymarket-cross-exchange-arb-bot) — 40.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 46 trading-infrastructure repos at 291.86 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Dev Tooling & Infra  —  confidence: Medium  (score 232.2)

- GitHub repos matching: **58**  (top velocity 232.15 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 63.0 stars/day
  - [Norao01/solana-pump-fun-jito-bundler-sniper](https://github.com/Norao01/solana-pump-fun-jito-bundler-sniper) — 59.0 stars/day
  - [dianenelson33/gmgn-bullx-photon-copytrade-bot-2026](https://github.com/dianenelson33/gmgn-bullx-photon-copytrade-bot-2026) — 23.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 58 tooling repos at 232.15 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 3. Meme & Speculation  —  confidence: High  (score 213.6)

- GitHub repos matching: **19**  (top velocity 201.29 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-6.16%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 63.0 stars/day
  - [Norao01/solana-pump-fun-jito-bundler-sniper](https://github.com/Norao01/solana-pump-fun-jito-bundler-sniper) — 59.0 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 15.3 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -6.16%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -6.16% so traders see which launches have real retention vs. pure rotation.

### 4. AI Agents on Solana  —  confidence: High  (score 122.2)

- GitHub repos matching: **20**  (top velocity 82.2 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - China's Google Just Released Its Fast New AI Model for Free
  - What Is Artex? The AI Hacking Tool Linked to the US Spy Agency Breach
  - Elon Musk’s SpaceX Gets FCC Approval to Launch AI Data Centers in Space

  Top repos:
  - [bettysuzuki/okx-agent-trade-kit-mcp-grid-dca-bot](https://github.com/bettysuzuki/okx-agent-trade-kit-mcp-grid-dca-bot) — 40.0 stars/day
  - [farzanamustafa936-dot/solana-pump-fun-sniper-bot](https://github.com/farzanamustafa936-dot/solana-pump-fun-sniper-bot) — 15.3 stars/day
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 14.86 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 82.2 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in bettysuzuki/okx-agent-trade-kit-mcp-grid-dca-bot-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 5. Wallets & UX  —  confidence: High  (score 77.5)

- GitHub repos matching: **20**  (top velocity 61.51 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [bryanwalter710-debug/solana-defi-security](https://github.com/bryanwalter710-debug/solana-defi-security) — 15.3 stars/day
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 14.86 stars/day
  - [arnabbhowmik07/Ghost](https://github.com/arnabbhowmik07/Ghost) — 8.83 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 20 new wallet/onboarding repos at 61.51 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 6. Security & Threats  —  confidence: High  (score 43.7)

- GitHub repos matching: **8**  (top velocity 3.73 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - The 1Password Breach Didn’t Touch Your Vault. The Phishing Emails Might
  - What Is Artex? The AI Hacking Tool Linked to the US Spy Agency Breach

  Top repos:
  - [GuiBibeau/artex-program](https://github.com/GuiBibeau/artex-program) — 2.0 stars/day
  - [getkenning/kenning](https://github.com/getkenning/kenning) — 0.93 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.22 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 3.73 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (5 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. Payments & Stablecoins  —  confidence: High  (score 25.9)

- GitHub repos matching: **6**  (top velocity 9.94 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Japan’s SBI, SMFG launch Solana venture for stablecoins, tokenization
  - Zelle picks Solana for ZelleUSD stablecoin and international payments

  Top repos:
  - [arnabbhowmik07/Ghost](https://github.com/arnabbhowmik07/Ghost) — 8.83 stars/day
  - [makedotfun/prize-escrow](https://github.com/makedotfun/prize-escrow) — 0.32 stars/day
  - [orrery-node/orrery](https://github.com/orrery-node/orrery) — 0.3 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. Consumer & Social  —  confidence: Medium  (score 17.0)

- GitHub repos matching: **4**  (top velocity 16.97 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 14.86 stars/day
  - [nibblescreative-afk/darkseek](https://github.com/nibblescreative-afk/darkseek) — 1.8 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.22 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 4 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.
