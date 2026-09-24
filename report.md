# Solana Narrative Radar — Fortnightly Report

Generated: 2026-09-24T18:31:32+00:00  |  Methodology v0.1

## On-chain context (live, public RPC)

- Network throughput: **3495.3 TPS avg** (30 recent samples, non-vote share tracked)  
- TPS trend across samples: **3.83%**  
- Solana core: **4.2.2**

## Detected Narratives (ranked)

### 1. Wallets & UX  —  confidence: Medium  (score 140.2)

- GitHub repos matching: **20**  (top velocity 132.16 stars/day)
- Headline mentions (last fortnight): **1**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Elliptic Wants Every Cop to Read a Crypto Wallet in Seconds—With AI

  Top repos:
  - [uni-launch/solana-token-creator](https://github.com/uni-launch/solana-token-creator) — 73.0 stars/day
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 26.11 stars/day
  - [Kylerkrausemdzyra64/Crypto-Checker](https://github.com/Kylerkrausemdzyra64/Crypto-Checker) — 14.67 stars/day

  **Build ideas:**
  - One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in 20 new wallet/onboarding repos at 132.16 stars/day.
  - Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.
  - Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: 1 this period — users clearly need guardrails).

### 2. Meme & Speculation  —  confidence: High  (score 93.4)

- GitHub repos matching: **12**  (top velocity 45.49 stars/day)
- Headline mentions (last fortnight): **3**
- Market 7d avg change: **11.93%**
- Cross-source confirmation: **3/3**

  Sample headlines:
  - Fomo overtakes Pump.fun in daily revenue on Solana
  - Decrypt Media and FOMO Hour’s Thought Leader Farokh Sarmad to Take Main Stage at NEXTPredict NY Conference
  - Fomo overtakes Pump.fun in daily revenue on Solana

  Top repos:
  - [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) — 34.38 stars/day
  - [dartkomnitibe/solana-meme-tool](https://github.com/dartkomnitibe/solana-meme-tool) — 3.6 stars/day
  - [neilveriemusm/Trpjan-solana-trading-toolkit](https://github.com/neilveriemusm/Trpjan-solana-trading-toolkit) — 3.57 stars/day

  **Build ideas:**
  - Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches (avg 7d change 11.93%).
  - Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.
  - Meme-velocity dashboard: tracks avg 7d change 11.93% so traders see which launches have real retention vs. pure rotation.

### 3. DeFi / Trading Infra  —  confidence: High  (score 83.0)

- GitHub repos matching: **47**  (top velocity 59.03 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Kraken brings DeFi yield to tokenized stocks and ETFs
  - Sui DeFi protocol Full Sail to wind down after Switchboard incident
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 26.11 stars/day
  - [Oryc11/Free-Demonstration-Guide](https://github.com/Oryc11/Free-Demonstration-Guide) — 10.5 stars/day
  - [openarbmev/Openarb-Trade-SDK](https://github.com/openarbmev/Openarb-Trade-SDK) — 6.14 stars/day

  **Build ideas:**
  - Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the 47 trading-infrastructure repos at 59.03 stars/day.
  - Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage (3 hits) while retail seeks clearer risk tooling.
  - Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.

### 4. Consumer & Social  —  confidence: Medium  (score 73.8)

- GitHub repos matching: **6**  (top velocity 73.81 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [uni-launch/solana-token-creator](https://github.com/uni-launch/solana-token-creator) — 73.0 stars/day
  - [blueshift-gg/solana-awesome](https://github.com/blueshift-gg/solana-awesome) — 0.42 stars/day
  - [accretion-xyz/awesome-solana-security](https://github.com/accretion-xyz/awesome-solana-security) — 0.23 stars/day

  **Build ideas:**
  - Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number 6 this period.
  - On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.
  - NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.

### 5. RWA & Tokenization  —  confidence: High  (score 71.2)

- GitHub repos matching: **6**  (top velocity 55.22 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Winners and losers of the SEC’s new tokenized stocks rules
  - Kraken brings DeFi yield to tokenized stocks and ETFs

  Top repos:
  - [coolbbcamp/Synthetic-Liquidity-Depth-Scanner](https://github.com/coolbbcamp/Synthetic-Liquidity-Depth-Scanner) — 28.67 stars/day
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 26.11 stars/day
  - [thesithunyein/owed](https://github.com/thesithunyein/owed) — 0.33 stars/day

  **Build ideas:**
  - RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal (6 repos, High confidence) makes this a land-grab moment.
  - Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.
  - Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.

### 6. Dev Tooling & Infra  —  confidence: Medium  (score 61.4)

- GitHub repos matching: **43**  (top velocity 61.36 stars/day)
- Headline mentions (last fortnight): **0**
- Cross-source confirmation: **1/3**

  Top repos:
  - [coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot](https://github.com/coolbbcamp/StonkFun-Multi-Wallet-Volume-Bot) — 26.11 stars/day
  - [propavingk/SlotDrift](https://github.com/propavingk/SlotDrift) — 16.25 stars/day
  - [Oryc11/Free-Demonstration-Guide](https://github.com/Oryc11/Free-Demonstration-Guide) — 10.5 stars/day

  **Build ideas:**
  - Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the 43 tooling repos at 61.36 stars/day).
  - Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.
  - Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.

### 7. Payments & Stablecoins  —  confidence: High  (score 26.8)

- GitHub repos matching: **7**  (top velocity 10.8 stars/day)
- Headline mentions (last fortnight): **2**
- Cross-source confirmation: **2/3**

  Sample headlines:
  - Solana Foundation hires ex-Binance CMO and payments exec as new partnerships expand
  - US Aims to Turn Stablecoins Into a Weapon for Dollar Dominance

  Top repos:
  - [Oryc11/Free-Demonstration-Guide](https://github.com/Oryc11/Free-Demonstration-Guide) — 10.5 stars/day
  - [nirholas/onchain-agent-wallets](https://github.com/nirholas/onchain-agent-wallets) — 0.17 stars/day
  - [grokloop/grokchain-programs](https://github.com/grokloop/grokchain-programs) — 0.04 stars/day

  **Build ideas:**
  - Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have deep volume/mcap ratio).
  - Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.
  - Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.

### 8. Security & Threats  —  confidence: Medium  (score 24.0)

- GitHub repos matching: **2**  (top velocity 0.04 stars/day)
- Headline mentions (last fortnight): **3**
- Cross-source confirmation: **1/3**

  Sample headlines:
  - Brooklyn Man Who Bragged About $16M Coinbase Scam Gets Up to 12 Years
  - More Markets lending reserve drained for $410,000: Blockaid
  - Term Finance loses estimated $8.5M in vault governance exploit

  Top repos:
  - [KarloAldrete/universal-proxy](https://github.com/KarloAldrete/universal-proxy) — 0.02 stars/day
  - [leafwithered/clawledger](https://github.com/leafwithered/clawledger) — 0.02 stars/day

  **Build ideas:**
  - Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at 0.04 stars/day show industrial-scale scam ops).
  - Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster (3 hits).
  - Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.
