# Delta Paper Live — 1H Donchian(20) breakout (PAPER ONLY)

Public Delta Exchange India candles only. **No API keys, no orders.** Long on close above 20-bar high, short below 20-bar low; initial SL = 2×ATR(14), then trailing SL = 2×ATR(14) from each closed bar (only tightens, never widens); exit on close back through mid-channel. Virtual $1,000 start, 1% risk per trade, notional capped at 3× balance. Fees: 0.02% maker entry/mid-exit, 0.05% taker + 0.02% slippage on stops. Runs hourly at :03 UTC via GitHub Actions. Second strategy: **[Viru Trend](VIRU_TREND.md)**.

**Last update:** 2026-11-06 13:13 IST

## Open positions

| Coin | Side | Entry | SL | Current | Qty | Unrealized P&L |
|---|---|---|---|---|---|---|
| XRPUSD | short | 1.2816 | 1.21687 | 1.1916 | 338.479 | $30.46 |
| BTCUSD | short | 78,272 | 76,676.2 | 75,670 | 0.00797574 | $20.75 |
| ETHUSD | short | 2,343 | 2,266.01 | 2,226.95 | 0.212989 | $24.72 |
| DOGEUSD | short | 0.07603 | 0.0731671 | 0.07171 | 7,737.82 | $33.43 |
| BNBUSD | short | 710.59 | 696.846 | 690.42 | 1.14656 | $23.13 |
| SOLUSD | short | 93.017 | 91.5276 | 89.614 | 3.97707 | $13.53 |
| XAUTUSD | short | 4,051.04 | 4,077.32 | 4,043.59 | 0.156713 | $1.17 |

## Closed trades

| Coin | Side | Entry time (IST) | Exit time (IST) | Entry | Exit | Reason | Net P&L |
|---|---|---|---|---|---|---|---|
| XAUTUSD | long | 11-04 10:30 | 11-05 19:30 | 3,994.6 | 4,091.2 | stop | $20.57 |
| SOLUSD | long | 11-04 19:30 | 11-05 17:30 | 95.238 | 95.1322 | stop | $-0.58 |
| ETHUSD | long | 11-04 13:30 | 11-05 17:30 | 2,322.75 | 2,395.13 | stop | $12.90 |
| BTCUSD | long | 11-04 13:30 | 11-05 17:30 | 78,474.5 | 79,813 | stop | $8.38 |
| BNBUSD | long | 11-04 12:30 | 11-05 09:30 | 703.56 | 713.825 | stop | $7.76 |
| DOGEUSD | long | 11-04 19:30 | 11-05 12:30 | 0.07679 | 0.07642 | mid_exit | $-1.71 |
| XRPUSD | long | 11-04 15:30 | 11-05 07:30 | 1.2924 | 1.308 | mid_exit | $4.69 |
| SOLUSD | short | 11-04 07:30 | 11-04 09:30 | 90.876 | 92.5146 | stop | $-7.84 |
| BNBUSD | short | 11-04 07:30 | 11-04 09:30 | 686.13 | 694.239 | stop | $-8.13 |
| DOGEUSD | short | 11-04 07:30 | 11-04 09:30 | 0.07316 | 0.0743606 | stop | $-8.05 |
| BTCUSD | short | 11-04 07:30 | 11-04 09:30 | 76,127.5 | 77,033.4 | stop | $-8.30 |
| SOLUSD | long | 11-03 20:30 | 11-04 05:30 | 93.767 | 92.3829 | stop | $-7.66 |
| ETHUSD | long | 11-03 17:30 | 11-04 04:30 | 2,282.35 | 2,273.85 | mid_exit | $-2.97 |
| XRPUSD | long | 11-03 17:30 | 11-04 05:30 | 1.2831 | 1.27089 | stop | $-6.91 |
| XAUTUSD | short | 11-03 13:30 | 11-03 17:30 | 3,897.24 | 3,920.96 | stop | $-9.19 |
| SOLUSD | short | 11-02 22:30 | 11-03 17:30 | 92.207 | 93.3302 | stop | $-5.08 |
| BNBUSD | short | 11-02 16:30 | 11-03 15:30 | 704.56 | 698.796 | stop | $6.44 |
| DOGEUSD | short | 11-02 22:30 | 11-03 15:30 | 0.07417 | 0.0745 | mid_exit | $-2.30 |
| BTCUSD | short | 11-02 20:30 | 11-03 17:30 | 77,482.5 | 77,396.3 | stop | $0.35 |
| XAUTUSD | long | 11-02 18:30 | 11-03 00:30 | 3,935.92 | 3,930.61 | stop | $-2.20 |
| XRPUSD | short | 11-02 22:30 | 11-03 00:30 | 1.2427 | 1.2513 | mid_exit | $-4.16 |
| XAUTUSD | long | 11-02 04:30 | 11-02 06:30 | 3,899.49 | 3,893.67 | stop | $-5.37 |
| SOLUSD | short | 11-01 17:30 | 11-02 05:30 | 94.88 | 94.8749 | stop | $-0.54 |
| ETHUSD | long | 11-02 06:30 | 11-02 11:30 | 2,288.7 | 2,283.07 | stop | $-2.56 |
| BTCUSD | long | 11-02 04:30 | 11-02 11:30 | 78,313.5 | 78,134.5 | mid_exit | $-3.82 |
| XAUTUSD | short | 11-01 18:30 | 11-02 02:30 | 3,882.12 | 3,884.3 | stop | $-3.15 |
| DOGEUSD | short | 11-01 23:30 | 11-02 04:30 | 0.07535 | 0.0756 | mid_exit | $-3.87 |
| BNBUSD | long | 11-01 13:30 | 11-01 23:30 | 714.6 | 709.878 | stop | $-8.35 |
| ETHUSD | long | 10-31 17:30 | 11-01 17:30 | 2,251.4 | 2,259.67 | stop | $3.66 |
| BTCUSD | long | 11-01 10:30 | 11-01 17:30 | 77,875.5 | 77,845.5 | stop | $-2.16 |
| XAUTUSD | short | 10-29 22:30 | 11-01 05:30 | 4,012.95 | 3,885.41 | mid_exit | $37.10 |
| DOGEUSD | short | 10-30 01:30 | 10-30 20:30 | 0.07545 | 0.07596 | mid_exit | $-2.09 |
| ETHUSD | short | 10-30 01:30 | 10-30 22:30 | 2,256.7 | 2,242.5 | mid_exit | $2.26 |
| SOLUSD | short | 10-30 01:30 | 10-30 09:30 | 96.158 | 97.4606 | stop | $-4.77 |
| BTCUSD | short | 10-30 01:30 | 10-30 10:30 | 78,808.5 | 78,606.3 | stop | $0.97 |
| XRPUSD | short | 10-30 01:30 | 10-30 09:30 | 1.239 | 1.25199 | stop | $-3.95 |
| BNBUSD | short | 10-30 01:30 | 10-30 02:30 | 696.28 | 715.063 | stop | $-8.37 |
| SOLUSD | short | 10-29 06:30 | 10-29 19:30 | 99.86 | 101.638 | stop | $-7.73 |
| BNBUSD | short | 10-29 15:30 | 10-29 20:30 | 742.21 | 751.399 | stop | $-6.94 |
| DOGEUSD | short | 10-29 06:30 | 10-29 18:30 | 0.07812 | 0.0792616 | stop | $-7.02 |
| ETHUSD | short | 10-29 06:30 | 10-29 19:30 | 2,312.9 | 2,347.55 | stop | $-7.57 |
| BTCUSD | short | 10-29 06:30 | 10-29 19:30 | 79,972.5 | 80,759.3 | stop | $-7.21 |
| XRPUSD | short | 10-29 06:30 | 10-29 19:30 | 1.2989 | 1.30889 | stop | $-4.17 |
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
| Balance (realized) | $789.79 |
| Realized P&L | $-210.21 |
| Unrealized P&L | $147.19 |
| Total P&L | $-63.02 |
| Closed trades | 82 |
| Win rate | 27% |

_State: `state/paper_state.json`, journal: `state/trade_journal.jsonl`. Paper trading only — not financial advice._
