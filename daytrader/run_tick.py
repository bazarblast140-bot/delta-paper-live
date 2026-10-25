"""DayTrader ORB — 15m PAPER tick. PUBLIC Delta candles only. No auth, no orders.

Separate virtual equity / journal / state from Viru Trend and Donchian.
"""
import json, os, sys, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paper.run_tick import candles, SYMS, IST
from daytrader.strategy import step, OR_BARS, MAX_LOSS_USD, RISK, LEV

START = 1000.0
STATE = os.getenv("DAYTRADER_STATE", "state/daytrader_state.json")
JOURNAL = os.getenv("DAYTRADER_JOURNAL", "state/daytrader_journal.jsonl")
HIST = 80  # closed 15m bars warm-up for ORB
MAX_TRADES_DAY = 20
MAX_DAILY_LOSS = 50.0


def _day_key(ts):
    return dt.datetime.fromtimestamp(ts, IST).strftime("%Y-%m-%d")


def _risk_ok(st):
    """Daily trade / loss caps from day-trader-delta config."""
    if st.get("trades_today", 0) >= MAX_TRADES_DAY:
        return False
    if st.get("daily_pnl", 0.0) <= -MAX_DAILY_LOSS:
        return False
    return True


def main():
    st = json.load(open(STATE)) if os.path.exists(STATE) else {"symbols": {}}
    os.makedirs(os.path.dirname(STATE) or ".", exist_ok=True)
    st.setdefault("balance", START)
    st.setdefault("trades_today", 0)
    st.setdefault("daily_pnl", 0.0)
    st.setdefault("day", None)
    jf = open(JOURNAL, "a")
    for s in SYMS:
        ss = st["symbols"].setdefault(s, {"position": None, "last_ts": 0})
        try:
            c = candles(s, HIST, "15m", 900)
        except Exception as e:
            print(f"{s}: fetch failed {e}"); continue
        if not c:
            continue
        for i, k in enumerate(c):
            if k["time"] <= ss["last_ts"]:
                continue
            if ss["last_ts"] == 0 and i < len(c) - 1:
                continue  # first run: go live from latest closed bar only
            day = _day_key(k["time"])
            if st.get("day") != day:
                st["day"] = day
                st["trades_today"] = 0
                st["daily_pnl"] = 0.0
            ss["equity"] = st["balance"]
            # Block new entries if daily caps hit (still manage open exits)
            allow_entry = _risk_ok(st)
            had_pos = ss.get("position") is not None
            evs = step(s, ss, c, i)
            if not allow_entry and not had_pos:
                # discard any fresh entry this bar
                for kind, d in list(evs):
                    if kind == "entry":
                        ss["position"] = None
                        evs = [(k2, d2) for k2, d2 in evs if k2 != "entry"]
                        print(f"{s}: SKIP entry (daily risk cap)")
            for kind, d in evs:
                print(f"{s} {kind.upper()} {json.dumps(d)}")
                jf.write(json.dumps({"event": kind, **d}) + "\n")
                if kind == "entry":
                    st["trades_today"] = st.get("trades_today", 0) + 1
                if kind == "exit":
                    st["daily_pnl"] = round(st.get("daily_pnl", 0.0) + d["net"], 4)
            st["balance"] = ss.pop("equity")
            ss["last_ts"] = k["time"]
        ss["price"] = c[-1]["close"]
        p = ss["position"]
        print(
            f"{s}: last closed {dt.datetime.fromtimestamp(c[-1]['time'], IST):%Y-%m-%d %H:%M} IST "
            f"close={c[-1]['close']} balance=${st['balance']:.2f} position="
            + (f"{p['side']} @{p['entry']} SL {p['sl']:.6g} TP {p['target']:.6g}" if p else "flat")
        )
    st["updated"] = dt.datetime.now(IST).isoformat()
    st["meta"] = {
        "name": "DayTrader ORB",
        "resolution": "15m",
        "or_bars": OR_BARS,
        "risk_pct": RISK,
        "lev_cap": LEV,
        "max_loss_usd": MAX_LOSS_USD,
        "target": "1R",
        "stop": "or-low/or-high",
    }
    json.dump(st, open(STATE, "w"), indent=1)
    jf.close()
    from paper.dashboard import write_readme
    write_readme(
        st, JOURNAL, START, "DAYTRADER_ORB.md",
        title="# DayTrader ORB — 15m Opening-Range Breakout (PAPER ONLY)",
        desc=(
            "Public Delta Exchange India candles only. **No API keys, no orders.** "
            "Adapted from day-trader-delta ORB skills (scanner/entry/exit/risk/budget). "
            "Entry on fresh close break of prior OR bar high/low; SL = OR low (long) / OR high (short); "
            "target = 1R. Separate virtual $1,000, 1% risk, max $15/trade, daily loss cap $50 / 20 trades, "
            "notional cap 3×, same fees as Donchian/Viru. **Not Viru. Not Donchian.** "
            "Runs every 15 min (at :02/:17/:32/:47 UTC) via GitHub Actions."
        ),
        files="`state/daytrader_state.json`, journal: `state/daytrader_journal.jsonl`",
    )


if __name__ == "__main__":
    main()
