# Delta Paper Live — 1H Donchian(20) breakout (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Long on close above 20-bar high, short below 20-bar low; initial SL = 2×ATR(14), then trailing SL = 2×ATR(14) from each closed bar (only tightens, never widens); exit on close back through mid-channel. Virtual $1,000 start, 1% risk per trade, notional capped at 3× balance. Fees: 0.02% maker entry/mid-exit, 0.05% taker + 0.02% slippage on stops. Runs hourly at :03 UTC via GitHub Actions. Second strategy: **[Viru Trend](VIRU_TREND.md)**.

**Last update:** 2026-10-29 07:40 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| XRPUSD | short | 1.2989 | 1.32131 | 1.2989 | 382.033 | $-0.00 |
| BTCUSD | short | 79,972.5 | 80,974.1 | 79,972.5 | 0.00854957 | $-0.00 |
| ETHUSD | short | 2,312.9 | 2,353.95 | 2,312.9 | 0.208599 | $-0.00 |
| DOGEUSD | short | 0.07812 | 0.07958 | 0.07812 | 5,865.07 | $-0.00 |
| SOLUSD | short | 99.86 | 101.908 | 99.86 | 4.18077 | $-0.00 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
| XAUTUSD | long | 10-29 00:30 | 10-29 03:30 | 4,074.1 | 4,052.25 | mid_exit | $-6.90 |
| SOLUSD | long | 10-28 13:30 | 10-28 17:30 | 102.682 | 101.808 | stop | $-7.05 |
| BNBUSD | long | 10-28 15:30 | 10-28 17:30 | 759.83 | 753.81 | stop | $-8.46 |
| DOGEUSD | long | 10-27 20:30 | 10-28 17:30 | 0.0782 | 0.0795995 | stop | $10.19 |
| ETHUSD | long | 10-27 20:30 | 10-28 17:30 | 2,346.15 | 2,348.05 | stop | $0.07 |
| BTCUSD | long | 10-27 20:30 | 10-28 17:30 | 80,530 | 80,897.7 | stop | $3.31 |
| XRPUSD | long | 10-27 17:30 | 10-28 16:30 | 1.315 | 1.3257 | mid_exit | $4.08 |
| XAUTUSD | long | 10-27 19:30 | 10-28 07:30 | 4,056.53 | 4,045.49 | stop | $-4.41 |
| BNBUSD | long | 10-27 20:30 | 10-28 05:30 | 749.93 | 743.261 | stop | $-8.27 |
| SOLUSD | short | 10-27 11:30 | 10-27 17:30 | 99.59 | 100.882 | stop | $-9.55 |
| BNBUSD | short | 10-27 11:30 | 10-27 15:30 | 734.75 | 740.475 | stop | $-9.98 |
| XRPUSD | long | 10-27 04:30 | 10-27 14:30 | 1.3105 | 1.2974 | mid_exit | $-5.28 |
| BNBUSD | long | 10-26 19:30 | 10-27 08:30 | 745.54 | 738.39 | mid_exit | $-6.67 |
| DOGEUSD | long | 10-26 19:30 | 10-27 11:30 | 0.07797 | 0.07725 | mid_exit | $-4.97 |
| SOLUSD | long | 10-26 19:30 | 10-26 21:30 | 102.131 | 101.32 | mid_exit | $-3.93 |
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
| Balance (realized) | $849.40 |
| Realized P&L | $-150.60 |
| Unrealized P&L | $0.00 |
| Total P&L | $-150.60 |
| Closed trades | 39 |
| Win rate | 28% |

_State: `state/paper_state.json`, journal: `state/trade_journal.jsonl`. Paper trading only — not financial advice._
