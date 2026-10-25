# Viru Trend — 15m Viru Trend Confirmation (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Port of `viru_trend_confirmation.pine`. Entry at close on BUY/SELL confirmation; SL = setup low/high; exit on SL or opposite signal (reverse). Separate virtual $1,000, 1% risk, notional cap 3×, same fees as Donchian. Runs every 15 min (at :01/:16/:31/:46) via GitHub Actions.

**Last update:** 2026-10-25 12:23 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| XRPUSD | short | 1.3208 | 1.3273 | 1.299 | 1,463.7 | $31.91 |
| BTCUSD | short | 80,550 | 80,869 | 80,482 | 0.031924 | $2.17 |
| ETHUSD | short | 2,364.55 | 2,373.1 | 2,343.5 | 1.05262 | $22.16 |
| DOGEUSD | short | 0.07763 | 0.07799 | 0.07683 | 28,500.6 | $22.80 |
| BNBUSD | short | 743.19 | 745.5 | 743.19 | 4.29628 | $-0.00 |
| SOLUSD | short | 101.93 | 102.622 | 101.57 | 15.5943 | $5.61 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
| SOLUSD | long | 10-24 23:45 | 10-25 11:00 | 101.041 | 101.93 | reverse | $14.81 |
| BNBUSD | long | 10-25 00:15 | 10-25 12:00 | 729.02 | 743.19 | reverse | $38.29 |
| DOGEUSD | long | 10-25 00:15 | 10-25 10:45 | 0.07717 | 0.07763 | reverse | $7.65 |
| BNBUSD | short | 10-24 13:30 | 10-25 00:15 | 734.75 | 729.02 | reverse | $19.98 |
| DOGEUSD | short | 10-24 12:45 | 10-25 00:15 | 0.0782 | 0.07717 | reverse | $29.00 |
| BTCUSD | short | 10-24 20:30 | 10-25 00:15 | 79,673.5 | 80,463.6 | stop | $-9.81 |
| SOLUSD | short | 10-24 00:00 | 10-24 23:45 | 104.21 | 101.041 | reverse | $82.08 |
| XAUTUSD | long | 10-24 07:45 | 10-24 15:00 | 3,999.65 | 3,998.25 | stop | $-2.87 |
| DOGEUSD | long | 10-24 07:45 | 10-24 09:15 | 0.07911 | 0.0788242 | stop | $-11.51 |
| SOLUSD | long | 10-23 21:15 | 10-23 23:30 | 104.794 | 104.293 | stop | $-11.03 |
| ETHUSD | long | 10-23 21:15 | 10-23 21:45 | 2,406.9 | 2,398.57 | stop | $-11.66 |
| XAUTUSD | long | 10-23 14:30 | 10-23 15:00 | 4,035.37 | 4,029.9 | stop | $-5.79 |
| DOGEUSD | short | 10-23 16:30 | 10-23 16:45 | 0.0799 | 0.0802761 | stop | $-11.42 |
| ETHUSD | long | 10-23 12:15 | 10-23 13:15 | 2,408.8 | 2,398.82 | stop | $-11.82 |
| SOLUSD | long | 10-23 06:00 | 10-23 06:45 | 103.931 | 103.56 | stop | $-12.36 |
| XRPUSD | short | 10-22 23:15 | 10-23 07:15 | 1.3103 | 1.31676 | stop | $-11.91 |
| BTCUSD | short | 10-22 23:30 | 10-23 00:15 | 81,068 | 81,376.3 | stop | $-12.51 |

## Summary

| Metric | Value |
|---|---|
| Starting balance | $1,000.00 |
| Balance (realized) | $1,079.13 |
| Realized P&L | $79.13 |
| Unrealized P&L | $84.65 |
| Total P&L | $163.78 |
| Closed trades | 17 |
| Win rate | 35% |

_State: `state/viru_state.json`, journal: `state/viru_journal.jsonl`. Paper trading only — not financial advice._
