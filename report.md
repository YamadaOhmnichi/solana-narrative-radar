# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-25T21:43:21+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 1055.0)

- GitHub repos matching: **49**  (top velocity 1023.0 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - The 1Password Breach Didn’t Touch Your Vault. The Phishing Emails Might
  - Ethereum’s new DeFi security tool raises questions over censorship

  Top repos:
  - [Norao01/solana-pump-fun-jito-bundler-sniper](https://github.com/Norao01/solana-pump-fun-jito-bundler-sniper) — 178.0 stars/day
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 167.0 stars/day
  - [rajmyers29/jupiter-v6-atomic-arbitrage-bot](https://github.com/rajmyers29/jupiter-v6-atomic-arbitrage-bot) — 163.0 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 49 trading-infrastructure repos at 1023.0 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (4 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Dev Tooling & Infra  —  confidence: Medium  (score 587.0)

- GitHub repos matching: **64**  (top velocity 587.0 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [Norao01/solana-pump-fun-jito-bundler-sniper](https://github.com/Norao01/solana-pump-fun-jito-bundler-sniper) — 178.0 stars/day
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 167.0 stars/day
  - [Truong81752/trust-wallet-metamask-seed-recovery-v3](https://github.com/Truong81752/trust-wallet-metamask-seed-recovery-v3) — 32.0 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 64 tooling repos at 587.0 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 3. Meme & Speculation  —  confidence: High  (score 572.9)

- GitHub repos matching: **22**  (top velocity 560.0 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-6.46%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [Norao01/solana-pump-fun-jito-bundler-sniper](https://github.com/Norao01/solana-pump-fun-jito-bundler-sniper) — 178.0 stars/day
  - [pinargomez/raydium-meteora-grpc-sniper-bot](https://github.com/pinargomez/raydium-meteora-grpc-sniper-bot) — 167.0 stars/day
  - [JohanRonto570/ave-ai-defined-fi-memecoin-sniper](https://github.com/JohanRonto570/ave-ai-defined-fi-memecoin-sniper) — 28.0 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -6.46%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -6.46% so traders see which launches have real retention vs. pure rotation.

### 4. AI Agents on Solana  —  confidence: High  (score 273.4)

- GitHub repos matching: **15**  (top velocity 225.39 stars/day)
- Headline mentions (last fortnight): **6**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - What Is Artex? The AI Hacking Tool Linked to the US Spy Agency Breach
  - Elon Musk’s SpaceX Gets FCC Approval to Launch AI Data Centers in Space
  - Bitcoin Falls Further as Inflation, Trump Tariffs and AI Selloff Rattle Markets

  Top repos:
  - [bettysuzuki/okx-agent-trade-kit-mcp-grid-dca-bot](https://github.com/bettysuzuki/okx-agent-trade-kit-mcp-grid-dca-bot) — 128.0 stars/day
  - [JohanRonto570/ave-ai-defined-fi-memecoin-sniper](https://github.com/JohanRonto570/ave-ai-defined-fi-memecoin-sniper) — 28.0 stars/day
  - [ursulagarcia861/gmgn-ai-bullx-solana-copytrade-bot](https://github.com/ursulagarcia861/gmgn-ai-bullx-solana-copytrade-bot) — 27.0 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 225.39 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in bettysuzuki/okx-agent-trade-kit-mcp-grid-dca-bot-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 5. Wallets & UX  —  confidence: High  (score 199.3)

- GitHub repos matching: **14**  (top velocity 175.34 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - French Senate Rejects Plan to Make Crypto Holders Declare Self-Custody Wallets
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [Truong81752/trust-wallet-metamask-seed-recovery-v3](https://github.com/Truong81752/trust-wallet-metamask-seed-recovery-v3) — 32.0 stars/day
  - [sidorov4181/trust-wallet-metamask-seed-recovery-pc](https://github.com/sidorov4181/trust-wallet-metamask-seed-recovery-pc) — 32.0 stars/day
  - [FolunuSayu33/trust-wallet-metamask-seed-recovery-win11](https://github.com/FolunuSayu33/trust-wallet-metamask-seed-recovery-win11) — 30.0 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 14 new wallet/onboarding repos at 175.34 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 3 this period — users clearly need guardrails).

### 6. Security & Threats  —  confidence: Medium  (score 41.5)

- GitHub repos matching: **5**  (top velocity 1.54 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - The 1Password Breach Didn’t Touch Your Vault. The Phishing Emails Might
  - What Is Artex? The AI Hacking Tool Linked to the US Spy Agency Breach

  Top repos:
  - [getkenning/kenning](https://github.com/getkenning/kenning) — 0.93 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.25 stars/day
  - [Phat1911/Tributary](https://github.com/Phat1911/Tributary) — 0.19 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 1.54 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (5 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. Consumer & Social  —  confidence: Medium  (score 19.5)

- GitHub repos matching: **4**  (top velocity 19.47 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [setyamickala/airdrop-agent](https://github.com/setyamickala/airdrop-agent) — 17.33 stars/day
  - [nibblescreative-afk/darkseek](https://github.com/nibblescreative-afk/darkseek) — 1.8 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.25 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 4 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.

### 8. Payments & Stablecoins  —  confidence: Medium  (score 17.1)

- GitHub repos matching: **5**  (top velocity 1.14 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Japan’s SBI, SMFG launch Solana venture for stablecoins, tokenization
  - Zelle picks Solana for ZelleUSD stablecoin and international payments

  Top repos:
  - [orrery-node/orrery](https://github.com/orrery-node/orrery) — 0.32 stars/day
  - [makedotfun/prize-escrow](https://github.com/makedotfun/prize-escrow) — 0.29 stars/day
  - [startgameauthor/contingency](https://github.com/startgameauthor/contingency) — 0.25 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.
