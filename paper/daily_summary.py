"""Prints markdown summary of today's (IST) closed paper trades."""
import json, os, datetime as dt
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
J = os.getenv("PAPER_JOURNAL", "state/trade_journal.jsonl"); S = os.getenv("PAPER_STATE", "state/paper_state.json")
ex = [json.loads(l) for l in open(J)] if os.path.exists(J) else []
ex = [e for e in ex if e["event"] == "exit"]
today = dt.datetime.now(IST).date()
td = [e for e in ex if dt.datetime.fromtimestamp(e["exit_time"], IST).date() == today]
st = json.load(open(S)) if os.path.exists(S) else {"symbols": {}}
wr = lambda L: f"{100*sum(e['net']>0 for e in L)/len(L):.0f}%" if L else "n/a"
out = [f"## Paper journal {today} (IST)", f"Trades closed today: {len(td)} | Net P&L after fees: ${sum(e['net'] for e in td):.2f} | Win rate: {wr(td)}"]
for e in td:
    out.append(f"- {e['symbol']} {e['side']} {e['entry']:.6g}→{e['exit']:.6g} ({e['reason']}) net ${e['net']:.2f}")
out.append(f"\n**Running total**: ${sum(e['net'] for e in ex):.2f} over {len(ex)} trades, win rate {wr(ex)}")
out.append(f"Balance: ${st.get('balance', 1000):.2f}")
for s, v in st["symbols"].items():
    p = v["position"]
    out.append(f"- {s}: " + (f"open {p['side']} @{p['entry']:.6g}" if p else "flat"))
out.append("\n_Paper trading only — no real orders._")
print("\n".join(out))
