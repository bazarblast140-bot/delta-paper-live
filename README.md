# Delta Paper Live — 1H Donchian(20) breakout (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Long on close above 20-bar high, short below 20-bar low; SL = 2×ATR(14); exit on close back through mid-channel. Virtual $1,000 start, 1% risk per trade, notional capped at 3× balance. Fees: 0.02% maker entry/mid-exit, 0.05% taker + 0.02% slippage on stops. Runs hourly at :03 UTC via GitHub Actions. Second strategy: **[Viru Trend](VIRU_TREND.md)**.

**Last update:** 2026-10-23 14:39 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| DOGEUSD | long | 0.07999 | 0.0788111 | 0.08053 | 8,056.1 | $4.35 |
| BNBUSD | long | 739.64 | 732.787 | 745 | 1.38584 | $7.43 |
| XAUTUSD | short | 4,048.34 | 4,083.33 | 4,031.6 | 0.285796 | $4.78 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
| BNBUSD | short | 10-22 21:30 | 10-23 06:30 | 728.33 | 734.815 | stop | $-11.04 |
| DOGEUSD | short | 10-22 21:30 | 10-23 07:30 | 0.07866 | 0.07977 | mid_exit | $-9.25 |
| ETHUSD | short | 10-22 21:30 | 10-23 07:30 | 2,379.35 | 2,413.69 | stop | $-10.64 |
| BTCUSD | short | 10-22 21:30 | 10-23 07:30 | 81,244.5 | 81,942 | mid_exit | $-8.77 |
| XRPUSD | short | 10-23 01:30 | 10-23 06:30 | 1.3015 | 1.32145 | stop | $-10.60 |

## Summary

| Metric | Value |
|---|---|
| Starting balance | $1,000.00 |
| Balance (realized) | $949.70 |
| Realized P&L | $-50.30 |
| Unrealized P&L | $16.56 |
| Total P&L | $-33.74 |
| Closed trades | 5 |
| Win rate | 0% |

_State: `state/paper_state.json`, journal: `state/trade_journal.jsonl`. Paper trading only — not financial advice._
