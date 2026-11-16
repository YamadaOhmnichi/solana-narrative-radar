# Solana Narrative Radar — Fortnightly Report

Generated: 2026-11-16T22:03:56+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Dev Tooling & Infra  —  confidence: Medium  (score 175.6)

- GitHub repos matching: **54**  (top velocity 175.61 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [binaryprovostsnatch/solana-node-notes](https://github.com/binaryprovostsnatch/solana-node-notes) — 96.0 stars/day
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 22.57 stars/day
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 10.5 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 54 tooling repos at 175.61 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 2. DeFi / Trading Infra  —  confidence: High  (score 158.0)

- GitHub repos matching: **48**  (top velocity 117.98 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Formation Securities plans Solana stock trading venue under SEC exemption
  - EU DeFi proposals could push users to riskier platforms, says Coinbase exec
  - The UK needs a workable route to regulated DeFi access

  Top repos:
  - [ValidatorStack/solana-vigil](https://github.com/ValidatorStack/solana-vigil) — 38.33 stars/day
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 10.5 stars/day
  - [NikubfrostPixel62446/Solana-Token-rpocket-Swap-Tutorial](https://github.com/NikubfrostPixel62446/Solana-Token-rpocket-Swap-Tutorial) — 10.5 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 48 trading-infrastructure repos at 117.98 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (5 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 3. Meme & Speculation  —  confidence: High  (score 105.8)

- GitHub repos matching: **16**  (top velocity 70.5 stars/day)
- Headline mentions (last fortnight): **0**
- Market 7d avg change: **-17.64%**
- Cross-source confirmation: **2/3**

  Top repos:
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 22.57 stars/day
  - [ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket](https://github.com/ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket) — 10.5 stars/day
  - [chadandyou/jrames](https://github.com/chadandyou/jrames) — 9.31 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change -17.64%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change -17.64% so traders see which launches have real retention vs. pure rotation.

### 4. AI Agents on Solana  —  confidence: High  (score 98.4)

- GitHub repos matching: **28**  (top velocity 66.44 stars/day)
- Headline mentions (last fortnight): **4**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - AI agents help rescue ETH’s Glamsterdam fork, ‘Steal My Bitcoin’ site: Hodler’s Digest
  - Hackers Redirected Bitcoin Miner Rewards via AI Attack, Luxor CEO Says
  - Fed Is Modeling AI 'Super Intelligence' Scenarios, Including Job Losses and a Stock Market Slump

  Top repos:
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 10.5 stars/day
  - [Novaograge12557/Solana-AI-resp-Agent-Multimodal](https://github.com/Novaograge12557/Solana-AI-resp-Agent-Multimodal) — 10.5 stars/day
  - [ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket](https://github.com/ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket) — 10.5 stars/day

  **Build ideas:**
  - Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at 66.44 stars/day).
  - Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in Savageworks/solana-resp-trader-client-go-style automation repos.
  - Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has deep volume/mcap ratio on Solana.

### 5. Wallets & UX  —  confidence: High  (score 96.5)

- GitHub repos matching: **22**  (top velocity 80.49 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - DTCC Plans Solana Expansion as Wallet Rules Limit Access
  - Suiet wallet to shut down in latest exit from Sui ecosystem

  Top repos:
  - [floatdotxyz/float](https://github.com/floatdotxyz/float) — 22.57 stars/day
  - [miloslavatangen/Checker-Mnemonic](https://github.com/miloslavatangen/Checker-Mnemonic) — 19.2 stars/day
  - [Novaograge12557/Solana-AI-resp-Agent-Multimodal](https://github.com/Novaograge12557/Solana-AI-resp-Agent-Multimodal) — 10.5 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 22 new wallet/onboarding repos at 80.49 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 2 this period — users clearly need guardrails).

### 6. Security & Threats  —  confidence: High  (score 59.0)

- GitHub repos matching: **13**  (top velocity 34.98 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Crypto investigators flag suspected $106M theft, $786K Solana bot drain
  - Hackers Redirected Bitcoin Miner Rewards via AI Attack, Luxor CEO Says
  - Crypto hack losses equal 57 cents per $1 earned onchain: Ark’s Valente

  Top repos:
  - [ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket](https://github.com/ColdBetweenVirgo/solana-pumpfun-sniper-bot-rpocket) — 10.5 stars/day
  - [AethForgeice25459/rugcheck-respocket-ai](https://github.com/AethForgeice25459/rugcheck-respocket-ai) — 10.5 stars/day
  - [CryAceocean/solgov-rpocket-team](https://github.com/CryAceocean/solgov-rpocket-team) — 10.5 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 34.98 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.

### 7. RWA & Tokenization  —  confidence: Medium  (score 40.2)

- GitHub repos matching: **3**  (top velocity 0.25 stars/day)
- Headline mentions (last fortnight): **5**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Mirae Asset Securities issues tokenized notes on Solana
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain
  - 'Tokenization Is Not the Finish Line': Jupiter to Let Users Borrow Against Bullish Shares

  Top repos:
  - [Hymetdotfun/hymet](https://github.com/Hymetdotfun/hymet) — 0.15 stars/day
  - [Zyxel89/owncurve](https://github.com/Zyxel89/owncurve) — 0.05 stars/day
  - [truenorth-lj/sofinance-public](https://github.com/truenorth-lj/sofinance-public) — 0.05 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (3 repos, Medium confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 8. Payments & Stablecoins  —  confidence: High  (score 33.6)

- GitHub repos matching: **8**  (top velocity 17.57 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Zelle picks Solana for ZelleUSD stablecoin and international payments
  - Tx launches USTX stablecoin to pull RWA liquidity onto its chain

  Top repos:
  - [Savageworks/solana-resp-trader-client-go](https://github.com/Savageworks/solana-resp-trader-client-go) — 10.5 stars/day
  - [ismeh7765/FlashUSDT-v](https://github.com/ismeh7765/FlashUSDT-v) — 6.0 stars/day
  - [orrery-node/orrery](https://github.com/orrery-node/orrery) — 0.4 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.
