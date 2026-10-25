# DayTrader ORB — 15m Opening-Range Breakout (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Adapted from day-trader-delta ORB skills (scanner/entry/exit/risk/budget). Entry on fresh close break of prior OR bar high/low; SL = OR low (long) / OR high (short); target = 1R. Separate virtual $1,000, 1% risk, max $15/trade, daily loss cap $50 / 20 trades, notional cap 3×, same fees as Donchian/Viru. **Not Viru. Not Donchian.** Runs every 15 min (at :02/:17/:32/:47 UTC) via GitHub Actions.

**Last update:** 2026-10-26 03:35 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| XRPUSD | short | 1.2933 | 1.2995 | 1.2933 | 1,473.99 | $-0.00 |
| ETHUSD | short | 2,332 | 2,342.65 | 2,332 | 0.855894 | $-0.00 |
| DOGEUSD | short | 0.0768 | 0.07725 | 0.0768 | 20,440.3 | $-0.00 |
| BNBUSD | short | 737.62 | 740.03 | 737.62 | 3.72232 | $-0.00 |
| SOLUSD | short | 101.16 | 101.581 | 101.16 | 21.9012 | $-0.00 |
| XAUTUSD | long | 4,008.39 | 4,004.86 | 4,007.71 | 0.686965 | $-0.47 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
| XAUTUSD | short | 10-25 22:45 | 10-26 02:15 | 4,003.12 | 4,006.33 | stop | $-4.17 |
| SOLUSD | short | 10-25 23:30 | 10-26 02:45 | 101.771 | 101.48 | target_1R | $6.82 |
| BNBUSD | long | 10-26 02:00 | 10-26 02:15 | 741.26 | 740.062 | stop | $-6.40 |
| BNBUSD | short | 10-26 01:15 | 10-26 01:30 | 742.006 | 741.223 | target_1R | $1.81 |
| DOGEUSD | short | 10-25 23:30 | 10-26 02:45 | 0.0773 | 0.07704 | target_1R | $8.28 |
| ETHUSD | short | 10-26 02:00 | 10-26 02:45 | 2,345.75 | 2,339.75 | target_1R | $5.86 |
| BTCUSD | short | 10-26 03:00 | 10-26 03:15 | 80,350 | 80,207 | target_1R | $3.73 |
| BTCUSD | long | 10-25 20:30 | 10-26 02:45 | 80,660 | 80,345.4 | stop | $-11.94 |
| XRPUSD | long | 10-25 22:15 | 10-26 02:45 | 1.3084 | 1.29784 | stop | $-10.75 |
| BNBUSD | short | 10-25 23:45 | 10-26 00:45 | 740.99 | 742.929 | stop | $-9.29 |
| BNBUSD | long | 10-25 23:15 | 10-25 23:30 | 742.65 | 741.542 | stop | $-6.18 |
| ETHUSD | long | 10-25 22:45 | 10-26 00:30 | 2,358.1 | 2,351.78 | stop | $-9.63 |
| ETHUSD | long | 10-25 18:15 | 10-25 18:45 | 2,333.95 | 2,326.23 | stop | $-11.55 |
| BTCUSD | long | 10-25 20:00 | 10-25 20:15 | 80,385 | 80,512 | target_1R | $3.39 |
| BTCUSD | long | 10-25 18:15 | 10-25 18:45 | 80,423.5 | 80,284.4 | stop | $-7.03 |
| XRPUSD | short | 10-25 20:45 | 10-25 21:00 | 1.2972 | 1.30266 | stop | $-11.97 |
| XRPUSD | short | 10-25 19:45 | 10-25 20:15 | 1.2936 | 1.29786 | stop | $-11.85 |
| XRPUSD | short | 10-25 18:45 | 10-25 19:00 | 1.2953 | 1.29926 | stop | $-11.28 |

## Summary

| Metric | Value |
|---|---|
| Starting balance | $1,000.00 |
| Balance (realized) | $917.87 |
| Realized P&L | $-82.13 |
| Unrealized P&L | $-0.47 |
| Total P&L | $-82.59 |
| Closed trades | 18 |
| Win rate | 33% |

_State: `state/daytrader_state.json`, journal: `state/daytrader_journal.jsonl`. Paper trading only — not financial advice._
