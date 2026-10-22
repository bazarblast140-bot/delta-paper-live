"""Viru Trend paper-fill logic. NO order placement anywhere (paper only).
Entry at close on BUY/SELL; SL = frozen setup low (long) / high (short); exit on SL or opposite signal (reverse)."""
from paper.strategy import LEV, RISK, MAKER_FEE, TAKER_FEE, SLIPPAGE, _close


def _open(st, side, px, slv, t, sym):
    dist = abs(px - slv)
    qty = min(st["equity"] * RISK / dist if dist > 0 else 0, st["equity"] * LEV / px)
    st["position"] = {"side": side, "entry": px, "qty": qty, "time": t, "sl": slv, "entry_fee": px * qty * MAKER_FEE}
    return ("entry", dict(st["position"], symbol=sym))


def step(sym, st, k, ind):
    """k: closed candle, ind: indicator row for k. st: {equity, position}."""
    ev = []; t = k["time"]; pos = st.get("position")
    if pos:
        L = pos["side"] == "long"
        if (k["low"] <= pos["sl"]) if L else (k["high"] >= pos["sl"]):
            px = min(pos["sl"], k["open"]) if L else max(pos["sl"], k["open"])
            px *= (1 - SLIPPAGE) if L else (1 + SLIPPAGE)
            tr = _close(pos, px, TAKER_FEE, t, "stop", sym)
            st["equity"] = round(st["equity"] + tr["net"], 4); st["position"] = None
            ev.append(("exit", tr)); return ev  # no same-candle re-entry after stop
        if ind["signal"] == (-1 if L else 1):
            tr = _close(pos, k["close"], MAKER_FEE, t, "reverse", sym)
            st["equity"] = round(st["equity"] + tr["net"], 4); st["position"] = None
            ev.append(("exit", tr))
        else:
            return ev
    if ind["signal"] == 1:
        ev.append(_open(st, "long", k["close"], ind["setup_low"], t, sym))
    elif ind["signal"] == -1:
        ev.append(_open(st, "short", k["close"], ind["setup_high"], t, sym))
    return ev
