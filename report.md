# Solana Narrative Radar — Fortnightly Report

Generated: 2026-09-10T10:57:09+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 65.2)

- GitHub repos matching: **47**  (top velocity 33.21 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Sui DeFi protocol Full Sail to wind down after Switchboard incident
  - Term Finance loses estimated $8.5M in vault governance exploit
  - MiCA is coming for DeFi vaults, but regulation will be difficult

  Top repos:
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 7.19 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 7.15 stars/day
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 6.57 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 47 trading-infrastructure repos at 33.21 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (4 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Meme & Speculation  —  confidence: High  (score 63.0)

- GitHub repos matching: **15**  (top velocity 29.64 stars/day)
- Headline mentions (last fortnight): **4**
- Market 7d avg change: **0.67%**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Fomo overtakes Pump.fun in daily revenue on Solana
  - What Is LAPTOP? Hunter Biden's Meme Coin Targeting TRUMP Holders
  - Hunter Biden's LAPTOP Meme Coin Crashes 99% on Debut

  Top repos:
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 7.19 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 7.15 stars/day
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 6.57 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change 0.67%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change 0.67% so traders see which launches have real retention vs. pure rotation.

### 3. Wallets & UX  —  confidence: High  (score 41.1)

- GitHub repos matching: **17**  (top velocity 25.09 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Bitcoin Wallet Maker Trezor Says Hackers Breached Its Email Provider
  - Mexican Musician and Family Killed Over Bitcoin Cold Wallet Believed to Hold Millions

  Top repos:
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 7.19 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 7.15 stars/day
  - [ascenx/safe_wallet](https://github.com/ascenx/safe_wallet) — 3.89 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 17 new wallet/onboarding repos at 25.09 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 4. Security & Threats  —  confidence: Medium  (score 40.3)

- GitHub repos matching: **5**  (top velocity 0.28 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Bitcoin Wallet Maker Trezor Says Hackers Breached Its Email Provider
  - Secret Service Freezes $52.8 Million in Crypto Tied to Telegram Bazaar Behind Global Scams
  - More Markets lending reserve drained for $410,000: Blockaid

  Top repos:
  - [hypnogaba/solana-signal-trader](https://github.com/hypnogaba/solana-signal-trader) — 0.14 stars/day
  - [daemon-blockint-tech/4R3S](https://github.com/daemon-blockint-tech/4R3S) — 0.05 stars/day
  - [KarloAldrete/universal-proxy](https://github.com/KarloAldrete/universal-proxy) — 0.03 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.28 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (5 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 5. AI Agents on Solana  —  confidence: High  (score 28.9)

- GitHub repos matching: **24**  (top velocity 12.86 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI Is Solving Math's Best Problems Faster Than They Can Be Replaced, Terence Tao Warns
  - Apple Unveils Redesigned Siri AI and A20 Pro Chip as CEO John Ternus Makes Debut

  Top repos:
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 6.57 stars/day
  - [PillCrew/PillCrew](https://github.com/PillCrew/PillCrew) — 2.68 stars/day
  - [kaiserern/Kaiser.charon](https://github.com/kaiserern/Kaiser.charon) — 1.18 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 12.86 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in PillCrew/claimchain-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. Dev Tooling & Infra  —  confidence: Medium  (score 8.2)

- GitHub repos matching: **43**  (top velocity 8.16 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nicechunk/game](https://github.com/nicechunk/game) — 6.08 stars/day
  - [dinsoul09/Ortaq](https://github.com/dinsoul09/Ortaq) — 0.5 stars/day
  - [fluxrpc/solana-go](https://github.com/fluxrpc/solana-go) — 0.32 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 43 tooling repos at 8.16 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 7. Consumer & Social  —  confidence: Medium  (score 6.9)

- GitHub repos matching: **5**  (top velocity 6.9 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nicechunk/game](https://github.com/nicechunk/game) — 6.08 stars/day
  - [subhdotsol/solana-programs](https://github.com/subhdotsol/solana-programs) — 0.3 stars/day
  - [accretion-xyz/awesome-solana-security](https://github.com/accretion-xyz/awesome-solana-security) — 0.26 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 5 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.

### 8. Payments & Stablecoins  —  confidence: Low  (score 0.4)

- GitHub repos matching: **5**  (top velocity 0.37 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **0/3**

  Top repos:
  - [nirholas/onchain-agent-wallets](https://github.com/nirholas/onchain-agent-wallets) — 0.19 stars/day
  - [grokloop/grokchain-programs](https://github.com/grokloop/grokchain-programs) — 0.08 stars/day
  - [nemorixgroup/Solana-Knowledge-Base](https://github.com/nemorixgroup/Solana-Knowledge-Base) — 0.06 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.
