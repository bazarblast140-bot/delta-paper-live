"""Faithful Python port of 'Viru Trend Confirmation' (Pine v6, MPL-2.0; see viru_trend_confirmation.pine).
Original components: ATR HEMA (c) SeerQuant, Trend Reversal oscillator (c) AlgoAlpha; combined for
Virendra Pandey | Codeviser. Evaluated on CLOSED candles only (every bar passed in must be closed)."""
import math
NA = None
ALPHA_L = GAMMA_L = 20; ATR_MULT = 0.04; ATR_LEN = 14; OSC_PERIOD = 20; CONFIRM_BARS = 3


def sma(x, n):
    out = [NA] * len(x)
    for i in range(n - 1, len(x)):
        w = x[i - n + 1:i + 1]
        if all(v is not None for v in w): out[i] = sum(w) / n
    return out


def rma(x, n):
    """Pine ta.rma: seeded with SMA(n) once n consecutive non-na values exist, then Wilder smoothing."""
    out = [NA] * len(x); a = 1.0 / n; prev = NA
    for i in range(len(x)):
        if prev is None:
            if i >= n - 1 and all(v is not None for v in x[i - n + 1:i + 1]):
                prev = sum(x[i - n + 1:i + 1]) / n
        else:
            prev = a * x[i] + (1 - a) * prev if x[i] is not None else prev
        out[i] = prev
    return out


def compute(c, alphaL=ALPHA_L, gammaL=GAMMA_L, atrMult=ATR_MULT, atrLen=ATR_LEN, oscP=OSC_PERIOD, confirm=CONFIRM_BARS):
    """c: list of closed candles {time,open,high,low,close}. Returns per-bar dicts."""
    n = len(c); H = [k["high"] for k in c]; L = [k["low"] for k in c]; C = [k["close"] for k in c]
    hl2 = [(h + l) / 2 for h, l in zip(H, L)]
    al, ga = 2.0 / (alphaL + 1.0), 2.0 / (gammaL + 1.0)
    hema = [0.0] * n; b = [0.0] * n
    for i in range(n):
        ph = hema[i - 1] if i else 0.0
        pb = b[i - 1] if i else hl2[i]          # nz(b[1], src)
        hema[i] = (1 - al) * (ph + pb) + al * hl2[i]
        b[i] = (1 - ga) * (b[i - 1] if i else 0.0) + ga * (hema[i] - (hema[i - 1] if i else 0.0))
    tr = [H[0] - L[0]] + [max(H[i] - L[i], abs(H[i] - C[i - 1]), abs(L[i] - C[i - 1])) for i in range(1, n)]
    atr = rma(tr, atrLen)
    ao = [None if s is None or l is None else s - l for s, l in zip(sma(hl2, 5), sma(hl2, 34))]
    ch = [NA] + [None if ao[i] is None or ao[i - 1] is None else ao[i] - ao[i - 1] for i in range(1, n)]
    rise = rma([None if v is None else max(v, 0) for v in ch], oscP)
    fall = rma([None if v is None else -min(v, 0) for v in ch], oscP)
    hd = 0; ags = []; rows = []
    for i in range(n):
        hc = None if i == 0 else hema[i] - hema[i - 1]
        thr = None if atr[i] is None else atr[i] * atrMult
        if hc is not None and thr is not None and abs(hc) >= thr:
            hd = 1 if hc > 0 else -1 if hc < 0 else hd   # neutral zone: keep previous direction
        r, f = rise[i], fall[i]
        if f is not None and f == 0: rsi = 100.0 - 50
        elif r is not None and r == 0: rsi = 0.0 - 50
        elif r is None or f is None: rsi = None
        else: rsi = 100.0 - 100.0 / (1.0 + r / f) - 50
        od = 0 if rsi is None else 1 if rsi > 0 else -1 if rsi < 0 else 0
        ags.append(1 if hd == 1 and od == 1 else -1 if hd == -1 and od == -1 else 0)
        rows.append({"time": c[i]["time"], "hema": hema[i], "hema_dir": hd, "osc": rsi, "osc_dir": od, "agreement": ags[-1]})
    for row, m in zip(rows, machine(ags, c, confirm)):
        row.update(m)
    return rows


def machine(ags, bars, confirm=CONFIRM_BARS):
    """Setup state machine per closed bar: agreement broken > opposite wick breach > expiry (age>confirm)
    > close breakout (age>=1); then arm on fresh agreement with frozen high/low."""
    prevAg = 0; pending = False; sd = 0; sbar = None; sh = sl = None; out = []
    for i, (ag, k) in enumerate(zip(ags, bars)):
        H, L, C = k["high"], k["low"], k["close"]
        sig = 0; event = None; sig_hi = sig_lo = None
        if pending:
            age = i - sbar
            if ag != sd: pending = False; event = "cancel_agreement"
            elif (L < sl) if sd == 1 else (H > sh): pending = False; event = "cancel_wick"
            elif age > confirm: pending = False; event = "expired"
            elif age >= 1 and ((C > sh) if sd == 1 else (C < sl)):
                sig = sd; sig_hi, sig_lo = sh, sl; pending = False; event = "BUY" if sd == 1 else "SELL"
        if ag != 0 and ag != prevAg:
            pending = True; sd = ag; sbar = i; sh, sl = H, L
            event = (event + "+" if event else "") + ("bull_setup" if ag == 1 else "bear_setup")
        prevAg = ag
        out.append({"signal": sig, "setup_high": sig_hi, "setup_low": sig_lo, "event": event, "pending": pending,
                    "pend_dir": sd if pending else 0, "pend_high": sh if pending else None, "pend_low": sl if pending else None})
    return out
