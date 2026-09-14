# Solana Narrative Radar — Fortnightly Report

Generated: 2026-09-14T06:36:18+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Meme & Speculation  —  confidence: High  (score 217.5)

- GitHub repos matching: **16**  (top velocity 179.65 stars/day)
- Headline mentions (last fortnight): **2**
- Market 7d avg change: **-10.9%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - Fomo overtakes Pump.fun in daily revenue on Solana
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 145.5 stars/day
  - [shaleflydisconnect/solana-sniper-bot](https://github.com/shaleflydisconnect/solana-sniper-bot) — 12.0 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 6.26 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -10.9%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -10.9% so traders see which launches have real retention vs. pure rotation.

### 2. DeFi / Trading Infra  —  confidence: High  (score 78.0)

- GitHub repos matching: **48**  (top velocity 38.02 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Robinhood Crypto Trading Volume Jumps 61% in August
  - Sui DeFi protocol Full Sail to wind down after Switchboard incident
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [shaleflydisconnect/solana-sniper-bot](https://github.com/shaleflydisconnect/solana-sniper-bot) — 12.0 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 6.26 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 6.23 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 48 trading-infrastructure repos at 38.02 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. AI Agents on Solana  —  confidence: High  (score 25.6)

- GitHub repos matching: **19**  (top velocity 9.57 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI Agents Spending Money Online? New Research Says Not Really
  - OpenAI Asks Congress Whether an AI Slowdown Would Be Legal

  Top repos:
  - [PillCrew/claimchain](https://github.com/PillCrew/claimchain) — 4.18 stars/day
  - [PillCrew/PillCrew](https://github.com/PillCrew/PillCrew) — 2.22 stars/day
  - [kaiserern/Kaiser.charon](https://github.com/kaiserern/Kaiser.charon) — 1.13 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 9.57 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in PillCrew/claimchain-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 4. Security & Threats  —  confidence: Medium  (score 24.2)

- GitHub repos matching: **3**  (top velocity 0.17 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - More Markets lending reserve drained for $410,000: Blockaid
  - Term Finance loses estimated $8.5M in vault governance exploit
  - Harmony plans rollback, wiping 109,000 transactions after ONE exploit

  Top repos:
  - [hypnogaba/solana-signal-trader](https://github.com/hypnogaba/solana-signal-trader) — 0.12 stars/day
  - [KarloAldrete/universal-proxy](https://github.com/KarloAldrete/universal-proxy) — 0.03 stars/day
  - [leafwithered/clawledger](https://github.com/leafwithered/clawledger) — 0.02 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.17 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 5. Wallets & UX  —  confidence: Medium  (score 21.4)

- GitHub repos matching: **19**  (top velocity 21.36 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 6.26 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 6.23 stars/day
  - [ascenx/safe_wallet](https://github.com/ascenx/safe_wallet) — 3.49 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 19 new wallet/onboarding repos at 21.36 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 0 this period — users clearly need guardrails).

### 6. Dev Tooling & Infra  —  confidence: Medium  (score 8.6)

- GitHub repos matching: **41**  (top velocity 8.6 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nicechunk/game](https://github.com/nicechunk/game) — 5.66 stars/day
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 0.88 stars/day
  - [antonkarasbiz/solana-program-examples](https://github.com/antonkarasbiz/solana-program-examples) — 0.67 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 41 tooling repos at 8.6 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 7. Consumer & Social  —  confidence: Medium  (score 6.5)

- GitHub repos matching: **7**  (top velocity 6.48 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [nicechunk/game](https://github.com/nicechunk/game) — 5.66 stars/day
  - [accretion-xyz/awesome-solana-security](https://github.com/accretion-xyz/awesome-solana-security) — 0.24 stars/day
  - [dizcorvus/opencatz-ai](https://github.com/dizcorvus/opencatz-ai) — 0.21 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 7 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.

### 8. DePIN & Physical Infra  —  confidence: Low  (score 0.9)

- GitHub repos matching: **2**  (top velocity 0.9 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **0/3**

  Top repos:
  - [SohniSwatantra/nosana-mcp](https://github.com/SohniSwatantra/nosana-mcp) — 0.88 stars/day
  - [belumume/zeroclaw-solana](https://github.com/belumume/zeroclaw-solana) — 0.02 stars/day

  **Build ideas:**
  - DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet (2 repos, Low confidence).
  - Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.
  - Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.
