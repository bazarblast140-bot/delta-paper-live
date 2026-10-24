# Viru Trend — 15m Viru Trend Confirmation (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Port of `viru_trend_confirmation.pine`. Entry at close on BUY/SELL confirmation; SL = setup low/high; exit on SL or opposite signal (reverse). Separate virtual $1,000, 1% risk, notional cap 3×, same fees as Donchian. Runs every 15 min (at :01/:16/:31/:46) via GitHub Actions.

**Last update:** 2026-10-24 21:45 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| XRPUSD | short | 1.3208 | 1.3273 | 1.2734 | 1,463.7 | $69.38 |
| BTCUSD | short | 79,673.5 | 80,447.5 | 79,804.5 | 0.0115907 | $-1.52 |
| ETHUSD | short | 2,364.55 | 2,373.1 | 2,307.6 | 1.05262 | $59.95 |
| DOGEUSD | short | 0.0782 | 0.07851 | 0.0761 | 29,032.1 | $60.97 |
| BNBUSD | short | 734.75 | 736.78 | 721.57 | 3.67469 | $48.43 |
| SOLUSD | short | 104.21 | 104.456 | 100.12 | 26.2405 | $107.32 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
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
| Balance (realized) | $897.12 |
| Realized P&L | $-102.88 |
| Unrealized P&L | $344.53 |
| Total P&L | $241.65 |
| Closed trades | 10 |
| Win rate | 0% |

_State: `state/viru_state.json`, journal: `state/viru_journal.jsonl`. Paper trading only — not financial advice._
