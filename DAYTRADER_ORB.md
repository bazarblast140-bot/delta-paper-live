# DayTrader ORB — 15m Opening-Range Breakout (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Adapted from day-trader-delta ORB skills (scanner/entry/exit/risk/budget). Entry on fresh close break of prior OR bar high/low; SL = OR low (long) / OR high (short); target = 1R. Separate virtual $1,000, 1% risk, max $15/trade, daily loss cap $50 / 20 trades, notional cap 3×, same fees as Donchian/Viru. **Not Viru. Not Donchian.** Runs every 15 min (at :02/:17/:32/:47 UTC) via GitHub Actions.

**Last update:** 2026-10-26 01:02 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| XRPUSD | long | 1.3084 | 1.2981 | 1.3009 | 936.803 | $-7.03 |
| BTCUSD | long | 80,660 | 80,361.5 | 80,510.5 | 0.0322033 | $-4.81 |
| DOGEUSD | short | 0.0773 | 0.07756 | 0.07724 | 36,157.4 | $2.17 |
| SOLUSD | short | 101.771 | 102.062 | 101.671 | 27.2558 | $2.73 |
| XAUTUSD | short | 4,003.12 | 4,005.53 | 4,003.03 | 0.692923 | $0.06 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
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
| Balance (realized) | $924.62 |
| Realized P&L | $-75.38 |
| Unrealized P&L | $-6.88 |
| Total P&L | $-82.27 |
| Closed trades | 9 |
| Win rate | 11% |

_State: `state/daytrader_state.json`, journal: `state/daytrader_journal.jsonl`. Paper trading only — not financial advice._
