# DayTrader ORB — 15m Opening-Range Breakout (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Adapted from day-trader-delta ORB skills (scanner/entry/exit/risk/budget). Entry on fresh close break of prior OR bar high/low; SL = OR low (long) / OR high (short); target = 1R. Separate virtual $1,000, 1% risk, max $15/trade, daily loss cap $50 / 20 trades, notional cap 3×, same fees as Donchian/Viru. **Not Viru. Not Donchian.** Runs every 15 min (at :02/:17/:32/:47 UTC) via GitHub Actions.

**Last update:** 2026-10-27 18:13 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| XRPUSD | long | 1.3042 | 1.2906 | 1.3119 | 628.867 | $4.84 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
| DOGEUSD | long | 10-27 04:45 | 10-27 15:00 | 0.07758 | 0.0769846 | stop | $-9.41 |
| ETHUSD | long | 10-27 04:45 | 10-27 12:15 | 2,317.7 | 2,300.94 | stop | $-9.59 |
| XAUTUSD | long | 10-27 05:30 | 10-27 06:45 | 4,024.19 | 4,011.07 | stop | $-9.63 |
| SOLUSD | long | 10-27 05:00 | 10-27 08:00 | 100.83 | 100.271 | stop | $-9.47 |
| BNBUSD | long | 10-27 05:30 | 10-27 07:45 | 744.77 | 741.952 | stop | $-10.35 |
| BTCUSD | long | 10-27 04:45 | 10-27 08:30 | 80,045 | 79,668.6 | stop | $-10.33 |
| XAUTUSD | short | 10-27 05:00 | 10-27 05:15 | 4,017.19 | 4,012.9 | target_1R | $1.62 |
| XAUTUSD | short | 10-27 03:45 | 10-27 04:30 | 4,022.31 | 4,019.18 | target_1R | $0.92 |
| XAUTUSD | long | 10-27 03:00 | 10-27 03:30 | 4,024.3 | 4,022.3 | stop | $-3.08 |
| SOLUSD | short | 10-27 04:30 | 10-27 04:45 | 100.281 | 100.441 | stop | $-5.63 |
| SOLUSD | long | 10-27 02:45 | 10-27 04:00 | 100.58 | 100.219 | stop | $-10.78 |
| BNBUSD | short | 10-27 04:30 | 10-27 05:15 | 739.52 | 742.799 | stop | $-12.56 |
| BNBUSD | short | 10-27 03:30 | 10-27 03:45 | 743 | 742.84 | target_1R | $-0.47 |
| DOGEUSD | long | 10-27 03:00 | 10-27 04:30 | 0.07742 | 0.0769846 | stop | $-10.10 |
| ETHUSD | long | 10-27 03:00 | 10-27 04:30 | 2,312.85 | 2,302.64 | stop | $-10.61 |
| BTCUSD | short | 10-27 03:30 | 10-27 04:30 | 79,963.5 | 79,741 | target_1R | $6.11 |
| XRPUSD | short | 10-27 04:30 | 10-27 04:45 | 1.2899 | 1.29406 | stop | $-10.19 |
| XRPUSD | long | 10-27 02:45 | 10-27 03:30 | 1.293 | 1.2975 | target_1R | $7.49 |
| XAUTUSD | long | 10-27 00:45 | 10-27 02:15 | 4,020.27 | 4,024.06 | target_1R | $1.39 |
| XAUTUSD | short | 10-26 23:00 | 10-27 00:30 | 4,026.37 | 4,017.62 | target_1R | $4.53 |
| SOLUSD | short | 10-27 01:45 | 10-27 02:30 | 100.281 | 100.531 | stop | $-8.25 |
| SOLUSD | short | 10-26 23:00 | 10-27 00:15 | 101.321 | 100.661 | target_1R | $8.00 |
| BNBUSD | short | 10-27 02:45 | 10-27 03:00 | 741.33 | 742.719 | stop | $-6.63 |
| BNBUSD | short | 10-27 02:15 | 10-27 02:30 | 740.5 | 741.828 | stop | $-6.48 |
| BNBUSD | short | 10-27 01:15 | 10-27 02:00 | 742.65 | 741.91 | target_1R | $1.55 |
| BNBUSD | short | 10-27 00:30 | 10-27 00:45 | 742.47 | 743.872 | stop | $-6.76 |
| BNBUSD | short | 10-27 00:00 | 10-27 00:15 | 743.94 | 742.68 | target_1R | $3.37 |
| DOGEUSD | short | 10-27 02:30 | 10-27 02:45 | 0.0771 | 0.0772454 | stop | $-6.78 |
| DOGEUSD | long | 10-27 00:30 | 10-27 02:00 | 0.07739 | 0.0771746 | stop | $-9.23 |
| DOGEUSD | short | 10-26 23:00 | 10-27 00:15 | 0.07759 | 0.07722 | target_1R | $8.02 |
| ETHUSD | short | 10-27 01:45 | 10-27 02:15 | 2,311.1 | 2,304.25 | target_1R | $6.68 |
| ETHUSD | short | 10-26 23:00 | 10-27 00:30 | 2,323.5 | 2,311.05 | target_1R | $7.97 |
| BTCUSD | long | 10-27 02:30 | 10-27 03:00 | 79,925.5 | 80,059.5 | target_1R | $3.28 |
| BTCUSD | short | 10-27 01:30 | 10-27 02:15 | 79,927 | 79,803.5 | target_1R | $2.94 |
| BTCUSD | short | 10-26 23:00 | 10-27 00:30 | 80,203.5 | 79,878 | target_1R | $7.63 |
| XRPUSD | short | 10-27 00:00 | 10-27 02:30 | 1.2972 | 1.2892 | target_1R | $7.85 |
| XAUTUSD | long | 10-26 02:30 | 10-26 03:30 | 4,008.39 | 4,004.06 | stop | $-4.90 |
| SOLUSD | short | 10-26 03:15 | 10-26 03:30 | 101.16 | 101.601 | stop | $-11.22 |
| BNBUSD | short | 10-26 03:15 | 10-26 03:30 | 737.62 | 740.578 | stop | $-12.94 |
| DOGEUSD | long | 10-26 04:00 | 10-26 04:45 | 0.07735 | 0.0771246 | stop | $-9.51 |
| DOGEUSD | short | 10-26 03:15 | 10-26 03:30 | 0.0768 | 0.0772654 | stop | $-10.62 |
| ETHUSD | short | 10-26 04:45 | 10-26 05:00 | 2,326.3 | 2,311.65 | target_1R | $8.24 |
| ETHUSD | long | 10-26 04:00 | 10-26 04:30 | 2,347.75 | 2,336.68 | stop | $-10.67 |
| ETHUSD | short | 10-26 03:15 | 10-26 03:30 | 2,332 | 2,343.12 | stop | $-10.92 |
| BTCUSD | long | 10-26 03:30 | 10-26 04:45 | 80,388.5 | 80,140 | stop | $-10.37 |
| XRPUSD | short | 10-26 04:30 | 10-26 04:45 | 1.2995 | 1.2967 | target_1R | $4.78 |
| XRPUSD | short | 10-26 03:15 | 10-26 03:30 | 1.2933 | 1.29976 | stop | $-10.86 |
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
| Balance (realized) | $751.90 |
| Realized P&L | $-248.10 |
| Unrealized P&L | $4.84 |
| Total P&L | $-243.26 |
| Closed trades | 65 |
| Win rate | 37% |

_State: `state/daytrader_state.json`, journal: `state/daytrader_journal.jsonl`. Paper trading only — not financial advice._
