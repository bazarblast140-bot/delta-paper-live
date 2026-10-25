# DayTrader ORB — 15m Opening-Range Breakout (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Adapted from day-trader-delta ORB skills (scanner/entry/exit/risk/budget). Entry on fresh close break of prior OR bar high/low; SL = OR low (long) / OR high (short); target = 1R. Separate virtual $1,000, 1% risk, max $15/trade, daily loss cap $50 / 20 trades, notional cap 3×, same fees as Donchian/Viru. **Not Viru. Not Donchian.** Runs every 15 min (at :02/:17/:32/:47 UTC) via GitHub Actions.

**Last update:** 2026-10-25 22:31 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| XRPUSD | long | 1.3084 | 1.2981 | 1.3084 | 936.803 | $0.00 |
| BTCUSD | long | 80,660 | 80,361.5 | 80,770.5 | 0.0322033 | $3.56 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
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
| Balance (realized) | $949.72 |
| Realized P&L | $-50.28 |
| Unrealized P&L | $3.56 |
| Total P&L | $-46.72 |
| Closed trades | 6 |
| Win rate | 17% |

_State: `state/daytrader_state.json`, journal: `state/daytrader_journal.jsonl`. Paper trading only — not financial advice._
