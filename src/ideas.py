#!/usr/bin/env python3
"""Evidence-tied build-idea generation.

Ideas are derived from each narrative's observed evidence (repo velocity,
headline themes, market momentum). Templates are curated per narrative so
each idea names the signal it is riding and a concrete first deliverable.
"""
IDEAS = {
    "AI Agents on Solana": [
        "Agent-wallet runtime: a Go/Type SDK that gives every AI agent a non-custodial Solana wallet with per-action spend limits and an auditable on-chain action log (rides the 25 new agent repos at {vel}).",
        "Agent-to-agent escrow program: an Anchor program where two agents lock funds against a task hash and release on verifiable completion — targets the trust gap visible in {top_repo}-style automation repos.",
        "Agent fee rail: x402-style HTTP 402 paywall in Rust/TS that lets any API monetize per-call for AI agents paying in USDC — stablecoin rail already has {pay_vol} volume/mcap ratio on Solana.",
        "Agent incident canary: an on-chain watchdog that publishes hashes of every action an agent took, enabling post-hoc audits when an agent misbehaves (responds to security-threat headline spike: {n_hits}).",
    ],
    "Wallets & UX": [
        "One-tap embedded wallet for Telegram mini-apps on Solana, targeting the wallet-UX friction visible in {repo_count} new wallet/onboarding repos at {vel}.",
        "Session-key wallet: a SPL program that issues 24h scoped keys (spend cap, program allowlist) so dapps never touch the main key — direct answer to onboarding drop-off that wallet repos are attacking.",
        "Wallet-drain canary service: continuous simulation that alerts users when a signature request would exfiltrate tokens (security headlines: {n_hits} this period — users clearly need guardrails).",
        "Human-readable transaction renderer as an open library any wallet can embed, covering the top 20 program layouts; targets the same UX gap the {top_repo} wave is aimed at.",
    ],
    "DeFi / Trading Infra": [
        "Copy-trading guardrail bot: open-source program + bot that mirrors KOL wallets but with hard loss caps and sandwich-protection, riding the {repo_count} trading-infrastructure repos at {vel}.",
        "Perp risk dashboard: real-time liquidation-heat map over Solana perps using public RPC; headlines show perp/DeFi coverage ({n_hits} hits) while retail seeks clearer risk tooling.",
        "Intent-based DEX aggregator SDK with MEV-protection defaults — the aggregator lane is crowded but the intent/MEV-protection angle is under-served based on repo descriptions sampled.",
        "Yield-strategy vaults for stablecoin LPs with automated migration when APY decays; stablecoin pairs dominate Solana ecosystem volume ({mkt_note}).",
    ],
    "Security & Threats": [
        "Open drainer-signature registry: community-maintained feed of known malicious program IDs + a free API dapps/wallets can query before signing (drainer repos at {vel} show industrial-scale scam ops).",
        "Pre-sign simulation widget: embeddable, self-hosted tool that runs a tx against a forked state and flags token transfers to unknown owners — targets the phishing/drainer headline cluster ({n_hits} hits).",
        "Rug-pull early warning for launchpads: on-chain LP-lock + authority-change monitor with public API; pairs with the meme-launchpad narrative instead of fighting it.",
        "Wallet hygiene scanner: a read-only audit that lists every infinite-approval a wallet has granted, with one-click revoke — a consumer-facing wedge into the security narrative.",
    ],
    "Meme & Speculation": [
        "Launchpad honesty score: index every pump.fun-style launch by LP lock, mint authority, holder concentration and dev-wallet behavior; surfaces the few credible launches ({mkt_note}).",
        "Anti-sniper launch template: open-source fair-launch program (no-bundle, capped per-wallet buys) that new launchpads can adopt — a counter-position to the sniper-bot repos in the dataset.",
        "Meme-velocity dashboard: tracks {mkt_note} so traders see which launches have real retention vs. pure rotation.",
    ],
    "Dev Tooling & Infra": [
        "Local-first Solana dev container: one command that ships validator, airdropped test keypair, and explorer UI (rides the {repo_count} tooling repos at {vel}).",
        "Program-diff explorer: show what changed between two deployed program versions (upgrade authority audit trail) — infra trusts need this as more programs go live.",
        "Free hosted RPC status page with per-method latency/limits across public providers; every new dev hits rate limits on day one.",
    ],
    "Payments & Stablecoins": [
        "Invoice-or implementation: Solana Pay QR + email fallback + automatic USDC settlement for freelancers in emerging markets (stablecoin rails have {pay_vol} volume/mcap ratio).",
        "Subscription billing program: SPL streaming contract with cancel-anytime semantics for SaaS pricing on-chain.",
        "Cross-border payroll pilot: batch USDC payouts with memo-based reconciliation; targets remittance-adjacent repos and stablecoin volume signals.",
    ],
    "Consumer & Social": [
        "Creator-tipping rail: portable tipping widget (Solana Pay + SPL transfers) embeddable on any site — consumer/social repos number {repo_count} this period.",
        "On-chain achievements protocol: signed attestations for in-game/player milestones, composable across games.",
        "NFT-backed ticketing kit for IRL events with transfer rules and anti-scalp caps.",
    ],
    "RWA & Tokenization": [
        "RWA disclosure registry: standard JSON schema + on-chain hash for tokenized asset disclosures; low-current-signal ({repo_count} repos, {conf} confidence) makes this a land-grab moment.",
        "Treasury-bill yield mirror: transparent program mirroring T-bill yields to a SPL token with per-epoch attestation.",
        "Commodity tokenization starter kit (warehouse-receipt model) for regional exchanges.",
    ],
    "DePIN & Physical Infra": [
        "DePIN coverage explorer: map + API of real-world device hotspots (Helium/Render-style) with honest coverage scoring — no signal-weighted product exists yet ({repo_count} repos, {conf} confidence).",
        "Sensor-data escrow program: payments released when IoT data hashes verify, targeting DePIN trust gaps.",
        "Bandwidth marketplace starter: open implementation of a per-GB settlement rail on Solana.",
    ],
}

def ideas_for(narrative, top_n=3):
    ev = narrative["evidence"]
    ctx = {
        "vel": f"{ev['github_top_velocity']} stars/day",
        "repo_count": ev["github_repos"],
        "n_hits": ev["headline_hits"],
        "conf": narrative["confidence"],
        "top_repo": (narrative["member_repos"][0]["full_name"] if narrative["member_repos"] else "top repo"),
        "pay_vol": f"{ev.get('market_avg_7d_pct') if ev.get('market_avg_7d_pct') is not None else 'deep'}",
        "mkt_note": (f"avg 7d change {ev['market_avg_7d_pct']}%" if ev.get("market_avg_7d_pct") is not None
                     else f"top token {narrative['evidence'].get('sample_headlines', ['n/a'])[0][:40] if narrative['evidence'].get('sample_headlines') else 'meme category'}"),
    }
    pool = IDEAS.get(narrative["narrative"], [])
    out = []
    for tpl in pool[:top_n]:
        try:
            out.append(tpl.format(**ctx))
        except Exception:
            out.append(tpl)
    return out
