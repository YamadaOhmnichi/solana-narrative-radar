#!/usr/bin/env python3
"""On-chain activity collector via public Solana RPC (no key needed).

Uses getRecentPerformanceSamples for real network throughput history —
a genuine on-chain usage signal (transactions/sec over recent epochs)
that contextualizes narrative momentum: accelerating usage supports
"accelerating narrative" claims, contracting usage weakens them.
"""
import json, urllib.request

RPC = "https://api.mainnet-beta.solana.com"

def rpc(method, params):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    req = urllib.request.Request(RPC, data=body, headers={
        "Content-Type": "application/json", "User-Agent": "solana-narrative-radar/0.1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def collect():
    out = {}
    try:
        samples = rpc("getRecentPerformanceSamples", [30])["result"]
        out["perf_samples"] = [{
            "slot": s["slot"],
            "num_transactions": s["numTransactions"],
            "num_non_vote": s.get("numNonVoteTransactions"),
            "num_slots": s["numSlots"],
            "sample_period_secs": s["samplePeriodSecs"],
            "tps": round(s["numTransactions"] / s["samplePeriodSecs"], 1),
        } for s in samples]
        tps_series = [x["tps"] for x in out["perf_samples"]][::-1]  # oldest→newest
        half = max(len(tps_series)//2, 1)
        first, second = tps_series[:half], tps_series[half:]
        out["tps_trend_pct"] = round(100 * (sum(second)/len(second) - sum(first)/len(first)) / max(sum(first)/len(first), 1), 2)
        out["tps_avg"] = round(sum(tps_series)/len(tps_series), 1)
        out["version"] = rpc("getVersion", [])["result"].get("solana-core")
    except Exception as e:
        print("onchain failed:", e)
    return out

if __name__ == "__main__":
    out = collect()
    json.dump(out, open("data/onchain.json", "w"), indent=1)
    print("TPS avg:", out.get("tps_avg"), "| trend:", out.get("tps_trend_pct"), "% | core:", out.get("version"))
