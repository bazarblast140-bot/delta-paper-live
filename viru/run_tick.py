"""Stateless 15-minute Viru Trend PAPER tick. PUBLIC Delta candles only. No auth, no orders."""
import json, os, sys, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paper.run_tick import candles, SYMS, IST
from viru.indicator import compute
from viru.strategy import step

START = 1000.0
STATE = os.getenv("VIRU_STATE", "state/viru_state.json")
JOURNAL = os.getenv("VIRU_JOURNAL", "state/viru_journal.jsonl")
HIST = 500  # closed 15m bars of warm-up for HEMA/RMA recursion


def main():
    st = json.load(open(STATE)) if os.path.exists(STATE) else {"symbols": {}}
    st.setdefault("balance", START); jf = open(JOURNAL, "a")
    for s in SYMS:
        ss = st["symbols"].setdefault(s, {"position": None, "last_ts": 0})
        try:
            c = candles(s, HIST, "15m", 900)
        except Exception as e:
            print(f"{s}: fetch failed {e}"); continue
        if not c: continue
        ind = compute(c)
        for i, k in enumerate(c):
            if k["time"] <= ss["last_ts"]: continue
            if ss["last_ts"] == 0 and i < len(c) - 1: continue  # first run: go live from latest closed bar
            ss["equity"] = st["balance"]
            for kind, d in step(s, ss, k, ind[i]):
                print(f"{s} {kind.upper()} {json.dumps(d)}"); jf.write(json.dumps({"event": kind, **d}) + "\n")
            st["balance"] = ss.pop("equity"); ss["last_ts"] = k["time"]
        r = ind[-1]; ss["price"] = c[-1]["close"]
        ss["indicator"] = {k: r[k] for k in ("hema_dir", "osc_dir", "agreement", "pend_dir", "pend_high", "pend_low", "event")}
        p = ss["position"]
        print(f"{s}: last closed {dt.datetime.fromtimestamp(c[-1]['time'], IST):%Y-%m-%d %H:%M} IST close={c[-1]['close']} "
              f"trend={r['hema_dir']} mom={r['osc_dir']} agree={r['agreement']} pending={r['pend_dir']} event={r['event']} "
              f"balance=${st['balance']:.2f} position=" + (f"{p['side']} @{p['entry']} SL {p['sl']:.6g}" if p else "flat"))
    st["updated"] = dt.datetime.now(IST).isoformat()
    json.dump(st, open(STATE, "w"), indent=1); jf.close()
    from paper.dashboard import write_readme
    write_readme(st, JOURNAL, START, "VIRU_TREND.md",
                 title="# Viru Trend — 15m Viru Trend Confirmation (PAPER ONLY)",
                 desc="Public Delta Exchange India candles only. **No API keys, no orders.** Port of `viru_trend_confirmation.pine`. "
                      "Entry at close on BUY/SELL confirmation; SL = setup low/high; exit on SL or opposite signal (reverse). "
                      "Separate virtual $1,000, 1% risk, notional cap 3×, same fees as Donchian. Runs every 15 min (at :01/:16/:31/:46) via GitHub Actions.",
                 files="`state/viru_state.json`, journal: `state/viru_journal.jsonl`")


if __name__ == "__main__":
    main()
