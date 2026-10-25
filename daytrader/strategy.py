"""DayTrader ORB paper-fill logic. NO order placement (paper only).

Adapted from day-trader-delta ORB skills:
  - Opening range = prior `or_bars` closed candles (default 1)
  - Long on close break above OR high (fresh cross); short below OR low
  - SL = OR low (long) / OR high (short); target = 1R
  - 1% risk, notional cap 3x equity, optional max_loss_usd cap
Same fee model as Donchian/Viru paper. Completely separate state.
"""
LEV = 3.0
RISK = 0.01
MAX_LOSS_USD = 15.0
OR_BARS = 1
TARGET_R = 1.0
MAKER_FEE, TAKER_FEE, SLIPPAGE = 0.0002, 0.0005, 0.0002


def _close(pos, price, fee, t, reason, sym):
    qty = pos["qty"]
    gross = (price - pos["entry"]) * qty * (1 if pos["side"] == "long" else -1)
    fees = pos["entry_fee"] + abs(price * qty) * fee
    return {"symbol": sym, "side": pos["side"], "entry_time": pos["time"], "exit_time": t,
            "entry": pos["entry"], "exit": price, "qty": qty, "reason": reason,
            "gross": round(gross, 4), "fees": round(fees, 4), "net": round(gross - fees, 4),
            "or_high": pos.get("or_high"), "or_low": pos.get("or_low"), "target": pos.get("target")}


def _size(equity, entry, stop):
    dist = abs(entry - stop)
    if dist <= 0 or equity <= 0:
        return 0.0
    qty = min(equity * RISK / dist, equity * LEV / entry)
    if MAX_LOSS_USD and qty * dist > MAX_LOSS_USD:
        qty = MAX_LOSS_USD / dist
    return qty


def _open(st, side, px, or_high, or_low, t, sym):
    stop = or_low if side == "long" else or_high
    risk = abs(px - stop)
    if risk <= 0:
        return None
    target = px + TARGET_R * risk if side == "long" else px - TARGET_R * risk
    qty = _size(st["equity"], px, stop)
    if qty <= 0:
        return None
    st["position"] = {
        "side": side, "entry": px, "qty": qty, "time": t, "sl": stop,
        "target": target, "or_high": or_high, "or_low": or_low,
        "entry_fee": px * qty * MAKER_FEE,
    }
    return ("entry", dict(st["position"], symbol=sym))


def opening_range(c, i, or_bars=OR_BARS):
    """Prior `or_bars` closed candles before index i (excludes i)."""
    if i < or_bars:
        return None
    w = c[i - or_bars:i]
    return max(x["high"] for x in w), min(x["low"] for x in w)


def step(sym, st, c, i, or_bars=OR_BARS):
    """Process closed candle i. st: {equity, position}. Returns events list."""
    ev = []
    rng = opening_range(c, i, or_bars)
    if rng is None:
        return ev
    or_high, or_low = rng
    k = c[i]
    t = k["time"]
    pos = st.get("position")
    if pos:
        L = pos["side"] == "long"
        hit_sl = (k["low"] <= pos["sl"]) if L else (k["high"] >= pos["sl"])
        hit_tp = (k["high"] >= pos["target"]) if L else (k["low"] <= pos["target"])
        # Same-bar both: pessimistic stop
        if hit_sl and hit_tp:
            hit_tp = False
        if hit_sl:
            px = min(pos["sl"], k["open"]) if L else max(pos["sl"], k["open"])
            px *= (1 - SLIPPAGE) if L else (1 + SLIPPAGE)
            tr = _close(pos, px, TAKER_FEE, t, "stop", sym)
            st["equity"] = round(st["equity"] + tr["net"], 4)
            st["position"] = None
            ev.append(("exit", tr))
            return ev
        if hit_tp:
            tr = _close(pos, pos["target"], MAKER_FEE, t, "target_1R", sym)
            st["equity"] = round(st["equity"] + tr["net"], 4)
            st["position"] = None
            ev.append(("exit", tr))
            return ev
        return ev

    # Fresh break: previous close was inside/at the range
    prev = c[i - 1]
    side = None
    if k["close"] > or_high and prev["close"] <= or_high:
        side = "long"
    elif k["close"] < or_low and prev["close"] >= or_low:
        side = "short"
    if side:
        e = _open(st, side, k["close"], or_high, or_low, t, sym)
        if e:
            ev.append(e)
    return ev
