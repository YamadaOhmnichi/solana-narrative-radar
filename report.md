# Solana Narrative Radar — Fortnightly Report

Generated: 2026-09-12T18:28:08+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Meme & Speculation  —  confidence: High  (score 265.7)

- GitHub repos matching: **16**  (top velocity 222.51 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **-13.6%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - Fomo overtakes Pump.fun in daily revenue on Solana
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 197.0 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 6.47 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 6.43 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -13.6%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -13.6% so traders see which launches have real retention vs. pure rotation.

### 2. DeFi / Trading Infra  —  confidence: High  (score 69.1)

- GitHub repos matching: **50**  (top velocity 29.11 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Robinhood Crypto Trading Volume Jumps 61% in August
  - Sui DeFi protocol Full Sail to wind down after Switchboard incident
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 6.47 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 6.43 stars/day
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 5.11 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 50 trading-infrastructure repos at 29.11 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. Security & Threats  —  confidence: Medium  (score 32.2)

- GitHub repos matching: **4**  (top velocity 0.22 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Blockstream Refuses Ransom for Return of $47M in Bitcoin from Liquid Hack: 'It Is Theft'
  - More Markets lending reserve drained for $410,000: Blockaid
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [hypnogaba/solana-signal-trader](https://github.com/hypnogaba/solana-signal-trader) — 0.12 stars/day
  - [daemon-blockint-tech/4R3S](https://github.com/daemon-blockint-tech/4R3S) — 0.05 stars/day
  - [KarloAldrete/universal-proxy](https://github.com/KarloAldrete/universal-proxy) — 0.03 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.22 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (4 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 4. Wallets & UX  —  confidence: Medium  (score 22.2)

- GitHub repos matching: **20**  (top velocity 22.23 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 6.47 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 6.43 stars/day
  - [ascenx/safe_wallet](https://github.com/ascenx/safe_wallet) — 3.58 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 20 new wallet/onboarding repos at 22.23 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 5. AI Agents on Solana  —  confidence: Medium  (score 18.1)

- GitHub repos matching: **23**  (top velocity 10.1 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - OpenAI Asks Congress Whether an AI Slowdown Would Be Legal

  Top repos:
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 5.11 stars/day
  - [PillCrew/PillCrew](https://github.com/PillCrew/PillCrew) — 2.43 stars/day
  - [kaiserern/Kaiser.charon](https://github.com/kaiserern/Kaiser.charon) — 1.17 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 10.1 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in PillCrew/claimchain-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 6. Dev Tooling & Infra  —  confidence: Medium  (score 7.5)

- GitHub repos matching: **41**  (top velocity 7.55 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nicechunk/game](https://github.com/nicechunk/game) — 5.85 stars/day
  - [fluxrpc/solana-go](https://github.com/fluxrpc/solana-go) — 0.29 stars/day
  - [dinsoul09/Ortaq](https://github.com/dinsoul09/Ortaq) — 0.29 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 41 tooling repos at 7.55 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 7. Consumer & Social  —  confidence: Medium  (score 6.7)

- GitHub repos matching: **8**  (top velocity 6.74 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nicechunk/game](https://github.com/nicechunk/game) — 5.85 stars/day
  - [accretion-xyz/awesome-solana-security](https://github.com/accretion-xyz/awesome-solana-security) — 0.25 stars/day
  - [subhdotsol/solana-programs](https://github.com/subhdotsol/solana-programs) — 0.23 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 8 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.

### 8. Payments & Stablecoins  —  confidence: Low  (score 0.4)

- GitHub repos matching: **8**  (top velocity 0.41 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **0/3**

  Top repos:
  - [nirholas/onchain-agent-wallets](https://github.com/nirholas/onchain-agent-wallets) — 0.17 stars/day
  - [grokloop/grokchain-programs](https://github.com/grokloop/grokchain-programs) — 0.07 stars/day
  - [nemorixgroup/Solana-Knowledge-Base](https://github.com/nemorixgroup/Solana-Knowledge-Base) — 0.05 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.
