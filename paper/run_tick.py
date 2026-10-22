"""Stateless hourly PAPER tick. Uses only the PUBLIC candles endpoint. No auth, no orders."""
import json, os, sys, time, urllib.request, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paper.strategy import step

BASE = os.getenv("DELTA_PUBLIC_URL", "https://api.india.delta.exchange").rstrip("/")
SYMS = os.getenv("PAPER_SYMBOLS", "XRPUSD,BTCUSD,ETHUSD,DOGEUSD,BNBUSD,SOLUSD,XAUTUSD").split(",")
START = 1000.0  # USD, one shared virtual account
STATE = os.getenv("PAPER_STATE", "state/paper_state.json")
JOURNAL = os.getenv("PAPER_JOURNAL", "state/trade_journal.jsonl")
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))


def candles(sym, n=100):
    now = int(time.time())
    url = f"{BASE}/v2/history/candles?resolution=1h&symbol={sym}&start={now-3600*(n+2)}&end={now}"
    req = urllib.request.Request(url, headers={"User-Agent": "paper-bot"})
    r = json.load(urllib.request.urlopen(req, timeout=20))["result"]
    c = sorted((x for x in r if x["time"] + 3600 <= now), key=lambda x: x["time"])  # closed only
    return c[-n:]


def main():
    st = json.load(open(STATE)) if os.path.exists(STATE) else {"symbols": {}}
    os.makedirs(os.path.dirname(STATE) or ".", exist_ok=True)
    jf = open(JOURNAL, "a")
    st.setdefault("balance", START)
    for s in SYMS:
        ss = st["symbols"].setdefault(s, {"position": None, "last_ts": 0})
        try:
            c = candles(s)
        except Exception as e:
            print(f"{s}: fetch failed {e}"); continue
        for i, k in enumerate(c):
            if k["time"] <= ss["last_ts"]:
                continue
            if ss["last_ts"] == 0 and i < len(c) - 1:
                continue  # first run: start live from latest closed candle only
            ss["equity"] = st["balance"]
            evs = step(s, ss, c, i)
            st["balance"] = ss.pop("equity")
            for kind, d in evs:
                print(f"{s} {kind.upper()} {json.dumps(d)}")
                jf.write(json.dumps({"event": kind, **d}) + "\n")
            ss["last_ts"] = k["time"]
        if c:
            ss["price"] = c[-1]["close"]
        p = ss["position"]
        last = c[-1] if c else {}
        print(f"{s}: last closed {dt.datetime.fromtimestamp(last.get('time',0), IST):%Y-%m-%d %H:%M} IST "
              f"close={last.get('close')} balance=${st['balance']:.2f} position="
              + (f"{p['side']} @{p['entry']} SL {p['sl']:.6g}" if p else "flat"))
    st["updated"] = dt.datetime.now(IST).isoformat()
    json.dump(st, open(STATE, "w"), indent=1)
    jf.close()
    from paper.dashboard import write_readme
    write_readme(st, JOURNAL, START, os.getenv("README_PATH", "README.md"))


if __name__ == "__main__":
    main()
