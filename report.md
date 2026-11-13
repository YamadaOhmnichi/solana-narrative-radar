# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-13T06:48:15+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. DeFi / Trading Infra  —  confidence: High  (score 221.2)

- GitHub repos matching: **44**  (top velocity 157.16 stars/day)
- Headline mentions (last fortnight): **8**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - Strategy Made $19.5 Billion in Profit. So Why Is MSCI Removing It From Stock Indexes?
  - Illinois Crypto Tax Draws Unlikely Alliance of DOJ, Banks and DeFi

  Top repos:
  - [ValidatorStack/solana-vigil](https://github.com/ValidatorStack/solana-vigil) — 120.5 stars/day
  - [ismeh7765/FlashUSDT-v](https://github.com/ismeh7765/FlashUSDT-v) — 8.5 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 6.08 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 44 trading-infrastructure repos at 157.16 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (8 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 2. Wallets & UX  —  confidence: High  (score 116.3)

- GitHub repos matching: **19**  (top velocity 92.31 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - Why the Path to Quantum Resistance Runs Uphill for Bitcoin Wallet Makers
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [PatchBuilderAmplify/stolen-crypto-tracer](https://github.com/PatchBuilderAmplify/stolen-crypto-tracer) — 43.56 stars/day
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 40.5 stars/day
  - [h100envy/gem-search](https://github.com/h100envy/gem-search) — 6.08 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 19 new wallet/onboarding repos at 92.31 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 3 this period — users clearly need guardrails).

### 3. Dev Tooling & Infra  —  confidence: Medium  (score 109.4)

- GitHub repos matching: **51**  (top velocity 109.4 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [PatchBuilderAmplify/stolen-crypto-tracer](https://github.com/PatchBuilderAmplify/stolen-crypto-tracer) — 43.56 stars/day
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 40.5 stars/day
  - [mAphrica/solana-foundation-kora](https://github.com/mAphrica/solana-foundation-kora) — 5.62 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 51 tooling repos at 109.4 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 4. Meme & Speculation  —  confidence: High  (score 107.8)

- GitHub repos matching: **16**  (top velocity 87.56 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-10.1%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 40.5 stars/day
  - [chadandyou/jrames](https://github.com/chadandyou/jrames) — 13.44 stars/day
  - [QuantumOrb/QuantOrb](https://github.com/QuantumOrb/QuantOrb) — 6.1 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -10.1%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -10.1% so traders see which launches have real retention vs. pure rotation.

### 5. Payments & Stablecoins  —  confidence: High  (score 82.5)

- GitHub repos matching: **9**  (top velocity 66.54 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - Anchorage Digital’s Stablecoins Can Now Settle Payments on Visa’s Network

  Top repos:
  - [PatchBuilderAmplify/stolen-crypto-tracer](https://github.com/PatchBuilderAmplify/stolen-crypto-tracer) — 43.56 stars/day
  - [Signcluengine/onchain-money-trail-analyzer](https://github.com/Signcluengine/onchain-money-trail-analyzer) — 12.85 stars/day
  - [ismeh7765/FlashUSDT-v](https://github.com/ismeh7765/FlashUSDT-v) — 8.5 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 6. AI Agents on Solana  —  confidence: High  (score 58.2)

- GitHub repos matching: **23**  (top velocity 18.24 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - Republican Senator Wants to Freeze AI Data Center Boom as Congress Pushes to Expand It
  - Nvidia, AMD, Broadcom: The AI Stock Winners and Losers After Jensen Huang’s Ousting

  Top repos:
  - [teraus111/web3-agent-kit-solana-trading](https://github.com/teraus111/web3-agent-kit-solana-trading) — 5.9 stars/day
  - [SpaceDataRig/space-data-rig](https://github.com/SpaceDataRig/space-data-rig) — 4.55 stars/day
  - [askglyph/glyph](https://github.com/askglyph/glyph) — 3.1 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 18.24 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in teraus111/web3-agent-kit-solana-trading-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 7. Security & Threats  —  confidence: High  (score 21.4)

- GitHub repos matching: **10**  (top velocity 5.42 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Crypto hack losses equal 57 cents per $1 earned onchain: Ark’s Valente

  Top repos:
  - [outgoingyang/solana-sniping-bot](https://github.com/outgoingyang/solana-sniping-bot) — 2.2 stars/day
  - [degeneracyy/defidegeneracy](https://github.com/degeneracyy/defidegeneracy) — 1.0 stars/day
  - [PTK030/kenning](https://github.com/PTK030/kenning) — 0.88 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 5.42 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (2 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 8. RWA & Tokenization  —  confidence: Medium  (score 16.3)

- GitHub repos matching: **3**  (top velocity 0.32 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Mirae Asset Securities issues tokenized notes on Solana
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain

  Top repos:
  - [Hymetdotfun/hymet](https://github.com/Hymetdotfun/hymet) — 0.22 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.05 stars/day
  - [truenorth-lj/sofinance-public](https://github.com/truenorth-lj/sofinance-public) — 0.05 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (3 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.
