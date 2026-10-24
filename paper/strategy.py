"""Pure signal + paper-fill logic. NO order placement anywhere (paper only)."""
DON, ATR_N, ATR_MULT = 20, 14, 2.0
LEV = 3.0          # max notional = 3x balance
RISK = 0.01        # risk 1% of balance per trade (distance to 2xATR stop)
MAKER_FEE, TAKER_FEE, SLIPPAGE = 0.0002, 0.0005, 0.0002


def atr(c, i, n=ATR_N):
    trs = []
    for k in range(i - n + 1, i + 1):
        h, l, pc = c[k]["high"], c[k]["low"], c[k - 1]["close"]
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    return sum(trs) / n


def bands(c, i, n=DON):
    w = c[i - n:i]  # previous n closed candles (excludes i)
    up, lo = max(x["high"] for x in w), min(x["low"] for x in w)
    return up, lo, (up + lo) / 2


def _close(pos, price, fee, t, reason, sym):
    qty = pos["qty"]
    gross = (price - pos["entry"]) * qty * (1 if pos["side"] == "long" else -1)
    fees = pos["entry_fee"] + abs(price * qty) * fee
    return {"symbol": sym, "side": pos["side"], "entry_time": pos["time"], "exit_time": t,
            "entry": pos["entry"], "exit": price, "qty": qty, "reason": reason,
            "gross": round(gross, 4), "fees": round(fees, 4), "net": round(gross - fees, 4)}


def step(sym, st, c, i):
    """Process closed candle i. st: {equity, position}. Returns (events list)."""
    ev = []
    if i < max(DON, ATR_N + 1):
        return ev
    k = c[i]; t = k["time"]
    up, lo, mid = bands(c, i)
    pos = st.get("position")
    if pos:
        L = pos["side"] == "long"
        hit_sl = k["low"] <= pos["sl"] if L else k["high"] >= pos["sl"]
        if hit_sl:  # stop = taker + slippage, gap-aware
            px = min(pos["sl"], k["open"]) if L else max(pos["sl"], k["open"])
            px *= (1 - SLIPPAGE) if L else (1 + SLIPPAGE)
            tr = _close(pos, px, TAKER_FEE, t, "stop", sym)
        elif (k["close"] < mid) if L else (k["close"] > mid):
            tr = _close(pos, k["close"], MAKER_FEE, t, "mid_exit", sym)
        else:
            tr = None
            # trailing stop: ratchet in favour only, using ATR(14) on this closed bar
            a = atr(c, i)
            pos["sl"] = max(pos["sl"], k["close"] - ATR_MULT * a) if L else min(pos["sl"], k["close"] + ATR_MULT * a)
        if tr:
            st["equity"] = round(st["equity"] + tr["net"], 4)
            st["position"] = None
            ev.append(("exit", tr))
            return ev  # no same-candle re-entry
    else:
        side = "long" if k["close"] > up else "short" if k["close"] < lo else None
        if side:
            a = atr(c, i)
            px = k["close"]
            qty = min(st["equity"] * RISK / (ATR_MULT * a) if a > 0 else 0, st["equity"] * LEV / px)
            st["position"] = {"side": side, "entry": px, "qty": qty, "time": t, "atr": a,
                              "sl": px - ATR_MULT * a if side == "long" else px + ATR_MULT * a,
                              "entry_fee": px * qty * MAKER_FEE}
            ev.append(("entry", dict(st["position"], symbol=sym)))
    return ev
