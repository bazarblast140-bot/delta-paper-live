# Delta Paper Live — 1H Donchian(20) breakout (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Long on close above 20-bar high, short below 20-bar low; initial SL = 2×ATR(14), then trailing SL = 2×ATR(14) from each closed bar (only tightens, never widens); exit on close back through mid-channel. Virtual $1,000 start, 1% risk per trade, notional capped at 3× balance. Fees: 0.02% maker entry/mid-exit, 0.05% taker + 0.02% slippage on stops. Runs hourly at :03 UTC via GitHub Actions. Second strategy: **[Viru Trend](VIRU_TREND.md)**.

**Last update:** 2026-10-24 23:24 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| XRPUSD | short | 1.2908 | 1.28594 | 1.2775 | 454.65 | $6.05 |
| BTCUSD | short | 80,791.5 | 80,404.6 | 80,182 | 0.0120878 | $7.37 |
| ETHUSD | short | 2,341.15 | 2,334.52 | 2,316.9 | 0.408991 | $9.92 |
| DOGEUSD | short | 0.07795 | 0.0770886 | 0.07653 | 6,658.94 | $9.46 |
| BNBUSD | short | 731.99 | 726.993 | 724 | 1.39699 | $11.16 |
| SOLUSD | short | 102.321 | 101.113 | 100.49 | 5.47168 | $10.02 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
| BNBUSD | long | 10-23 08:30 | 10-24 03:30 | 739.64 | 733.75 | mid_exit | $-8.57 |
| ETHUSD | short | 10-24 03:30 | 10-24 04:30 | 2,365.9 | 2,386.3 | mid_exit | $-5.77 |
| DOGEUSD | long | 10-23 10:30 | 10-23 23:30 | 0.07999 | 0.07962 | mid_exit | $-3.24 |
| SOLUSD | long | 10-23 18:30 | 10-23 19:30 | 105.082 | 103.63 | stop | $-10.12 |
| XAUTUSD | short | 10-22 21:30 | 10-23 17:30 | 4,048.34 | 4,034.54 | mid_exit | $3.48 |
| BNBUSD | short | 10-22 21:30 | 10-23 06:30 | 728.33 | 734.815 | stop | $-11.04 |
| DOGEUSD | short | 10-22 21:30 | 10-23 07:30 | 0.07866 | 0.07977 | mid_exit | $-9.25 |
| ETHUSD | short | 10-22 21:30 | 10-23 07:30 | 2,379.35 | 2,413.69 | stop | $-10.64 |
| BTCUSD | short | 10-22 21:30 | 10-23 07:30 | 81,244.5 | 81,942 | mid_exit | $-8.77 |
| XRPUSD | short | 10-23 01:30 | 10-23 06:30 | 1.3015 | 1.32145 | stop | $-10.60 |

## Summary

| Metric | Value |
|---|---|
| Starting balance | $1,000.00 |
| Balance (realized) | $925.49 |
| Realized P&L | $-74.51 |
| Unrealized P&L | $53.97 |
| Total P&L | $-20.54 |
| Closed trades | 10 |
| Win rate | 10% |

_State: `state/paper_state.json`, journal: `state/trade_journal.jsonl`. Paper trading only — not financial advice._
