# Delta Paper Live — 1H Donchian(20) breakout (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Long on close above 20-bar high, short below 20-bar low; initial SL = 2×ATR(14), then trailing SL = 2×ATR(14) from each closed bar (only tightens, never widens); exit on close back through mid-channel. Virtual $1,000 start, 1% risk per trade, notional capped at 3× balance. Fees: 0.02% maker entry/mid-exit, 0.05% taker + 0.02% slippage on stops. Runs hourly at :03 UTC via GitHub Actions. Second strategy: **[Viru Trend](VIRU_TREND.md)**.

**Last update:** 2026-10-26 22:04 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| DOGEUSD | long | 0.07797 | 0.07659 | 0.07782 | 6,623.99 | $-0.99 |
| BNBUSD | long | 745.54 | 735.341 | 744.24 | 0.8963 | $-1.17 |
| SOLUSD | long | 102.131 | 100.15 | 101.91 | 4.61539 | $-1.02 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
| XAUTUSD | long | 10-26 08:30 | 10-26 18:30 | 4,014.13 | 4,004.86 | stop | $-6.88 |
| SOLUSD | short | 10-26 08:30 | 10-26 09:30 | 100.231 | 101.32 | mid_exit | $-6.69 |
| BTCUSD | short | 10-26 06:30 | 10-26 10:30 | 79,719 | 80,234.5 | mid_exit | $-7.04 |
| XRPUSD | short | 10-26 08:30 | 10-26 10:30 | 1.2779 | 1.2928 | mid_exit | $-7.25 |
| XAUTUSD | long | 10-25 21:30 | 10-26 03:30 | 4,005.59 | 4,001.52 | stop | $-4.84 |
| XAUTUSD | long | 10-25 09:30 | 10-25 10:30 | 4,002.76 | 3,996.66 | stop | $-6.34 |
| BNBUSD | long | 10-25 05:30 | 10-25 13:30 | 741.57 | 740.6 | stop | $-1.88 |
| XRPUSD | long | 10-25 04:30 | 10-25 11:30 | 1.3001 | 1.29653 | stop | $-2.13 |
| SOLUSD | short | 10-24 03:30 | 10-24 23:30 | 102.321 | 101.134 | stop | $6.11 |
| BNBUSD | short | 10-24 14:30 | 10-24 23:30 | 731.99 | 727.138 | stop | $6.07 |
| DOGEUSD | short | 10-24 03:30 | 10-24 23:30 | 0.07795 | 0.077104 | stop | $5.27 |
| ETHUSD | short | 10-24 19:30 | 10-24 23:30 | 2,341.15 | 2,334.99 | stop | $1.85 |
| BTCUSD | short | 10-24 03:30 | 10-24 23:30 | 80,791.5 | 80,420.7 | stop | $3.80 |
| XRPUSD | short | 10-24 03:30 | 10-24 23:30 | 1.2908 | 1.2862 | stop | $1.68 |
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
| Balance (realized) | $907.23 |
| Realized P&L | $-92.77 |
| Unrealized P&L | $-3.18 |
| Total P&L | $-95.95 |
| Closed trades | 24 |
| Win rate | 29% |

_State: `state/paper_state.json`, journal: `state/trade_journal.jsonl`. Paper trading only — not financial advice._
