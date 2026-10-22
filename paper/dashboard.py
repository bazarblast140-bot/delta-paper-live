"""Regenerates README.md with a live paper-trading dashboard."""
import json, os, datetime as dt
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
f = lambda x: f"{x:,.6g}"

def write_readme(st, journal, start, path="README.md", title=None, desc=None, files=None):
    ex = [json.loads(l) for l in open(journal)] if os.path.exists(journal) else []
    ex = [e for e in ex if e["event"] == "exit"]
    bal = st.get("balance", start)
    L = [title or "# Delta Paper Live — 1H Donchian(20) breakout (PAPER ONLY)", "",
         desc or "Public Delta Exchange India candles only. **No API keys, no orders.** Long on close above 20-bar high, short below 20-bar low; "
         "SL = 2×ATR(14); exit on close back through mid-channel. Virtual $1,000 start, 1% risk per trade, notional capped at 3× balance. "
         "Fees: 0.02% maker entry/mid-exit, 0.05% taker + 0.02% slippage on stops. Runs hourly at :03 UTC via GitHub Actions. "
         "Second strategy: **[Viru Trend](VIRU_TREND.md)**.", "",
         f"**Last update:** {dt.datetime.now(IST):%Y-%m-%d %H:%M} IST", "", "## Open positions", ""]
    upnl_tot = 0.0; rows = []
    for s, v in st["symbols"].items():
        p = v.get("position")
        if not p: continue
        px = v.get("price", p["entry"]); u = (px - p["entry"]) * p["qty"] * (1 if p["side"] == "long" else -1)
        upnl_tot += u
        rows.append(f"| {s} | {p['side']} | {f(p['entry'])} | {f(p['sl'])} | {f(px)} | {f(p['qty'])} | ${u:,.2f} |")
    L += (["| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |", "|---|---|---|---|---|---|---|"] + rows) if rows else ["_None (all flat)._"]
    L += ["", "## Closed trades", ""]
    if ex:
        L += ["| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |", "|---|---|---|---|---|---|---|---|"]
        for e in reversed(ex):
            t = lambda x: dt.datetime.fromtimestamp(x, IST).strftime("%m-%d %H:%M")
            L.append(f"| {e['symbol']} | {e['side']} | {t(e['entry_time'])} | {t(e['exit_time'])} | {f(e['entry'])} | {f(e['exit'])} | {e['reason']} | ${e['net']:,.2f} |")
    else:
        L.append("_No closed trades yet._")
    real = sum(e["net"] for e in ex); wins = sum(e["net"] > 0 for e in ex)
    L += ["", "## Summary", "", "| Metric | Value |", "|---|---|",
          f"| Starting balance | ${start:,.2f} |", f"| Balance (realized) | ${bal:,.2f} |",
          f"| Realized P&L | ${real:,.2f} |", f"| Unrealized P&L | ${upnl_tot:,.2f} |",
          f"| Total P&L | ${real + upnl_tot:,.2f} |", f"| Closed trades | {len(ex)} |",
          f"| Win rate | {f'{100*wins/len(ex):.0f}%' if ex else 'n/a'} |", "",
          f"_State: {files or '`state/paper_state.json`, journal: `state/trade_journal.jsonl`'}. Paper trading only — not financial advice._", ""]
    open(path, "w").write("\n".join(L))
