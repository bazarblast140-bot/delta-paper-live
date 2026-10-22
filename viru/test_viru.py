import pytest
from viru import indicator as I
from viru.indicator import compute, rma, sma
from viru.strategy import step


def mk(cl, rng=1.0):
    return [{"time": 900 * i, "open": p, "high": p + rng, "low": p - rng, "close": p} for i, p in enumerate(cl)]


def test_hema_recursion_first_bars():
    c = mk([100, 102]); r = compute(c); a = g = 2 / 21
    assert r[0]["hema"] == pytest.approx(100)
    b0 = g * 100
    assert r[1]["hema"] == pytest.approx((1 - a) * (100 + b0) + a * 102)


def test_rma_seed_and_smoothing():
    x = [None, 1, 2, 3, 4]
    out = rma(x, 2)
    assert out[:2] == [None, None] and out[2] == 1.5 and out[3] == pytest.approx(0.5 * 3 + 0.5 * 1.5)
    assert sma([1, 2, 3], 2) == [None, 1.5, 2.5]


def test_uptrend_bullish_agreement_and_buy():
    c = mk([100 + 0.05 * i * i for i in range(80)])
    r = compute(c)
    assert r[-1]["hema_dir"] == 1 and r[-1]["osc_dir"] == 1 and r[-1]["agreement"] == 1
    sigs = [x for x in r if x["signal"]]
    assert sigs and sigs[0]["signal"] == 1


def test_neutral_zone_keeps_direction(monkeypatch):
    c = mk([100 + 0.05 * i * i for i in range(60)] + [277] * 1)
    r = compute(c, atrMult=1e9)  # nothing ever exceeds the zone -> direction stays 0
    assert all(x["hema_dir"] == 0 for x in r)
    r2 = compute(c)
    assert r2[-1]["hema_dir"] == 1


@pytest.fixture
def machine():
    from viru.indicator import machine
    return machine


def bar(h, l, c): return {"high": h, "low": l, "close": c}


def test_no_signal_on_setup_candle(machine):
    out = machine([1, 1], [bar(10, 9, 9.5), bar(11, 9.5, 10.5)])
    assert out[0]["signal"] == 0 and out[1]["signal"] == 1
    assert out[1]["setup_high"] == 10 and out[1]["setup_low"] == 9  # frozen at setup candle


def test_agreement_broken_has_priority(machine):
    out = machine([1, 0], [bar(10, 9, 9.5), bar(12, 9.5, 11)])
    assert out[1]["signal"] == 0 and out[1]["event"] == "cancel_agreement"


def test_wick_breach_beats_breakout(machine):
    out = machine([1, 1], [bar(10, 9, 9.5), bar(12, 8.9, 11)])
    assert out[1]["signal"] == 0 and out[1]["event"] == "cancel_wick"
    out = machine([-1, -1], [bar(10, 9, 9.5), bar(10.1, 8, 8.5)])
    assert out[1]["event"] == "cancel_wick"


def test_expiry_after_three_bars(machine):
    b = [bar(10, 9, 9.5)] + [bar(9.9, 9.1, 9.5)] * 3 + [bar(11, 9.5, 10.5)]
    out = machine([1] * 5, b)
    assert out[4]["event"] == "expired" and out[4]["signal"] == 0
    out = machine([1] * 4, b[:3] + [bar(11, 9.5, 10.5)])
    assert out[3]["signal"] == 1  # age 3 still valid


def test_sell_and_fresh_agreement_needed(machine):
    out = machine([-1, -1, -1], [bar(10, 9, 9.5), bar(9.5, 8, 8.5), bar(9, 7, 7.5)])
    assert out[1]["signal"] == -1 and out[2]["signal"] == 0  # no re-arm without fresh agreement


def test_strategy_entry_sl_reverse_and_stop():
    st = {"equity": 1000.0, "position": None}
    k = {"time": 1, "open": 10, "high": 11, "low": 9.5, "close": 10.5}
    ev = step("X", st, k, {"signal": 1, "setup_high": 10, "setup_low": 9})
    p = st["position"]; assert p["side"] == "long" and p["sl"] == 9
    assert abs(p["entry"] - p["sl"]) * p["qty"] <= 10 + 1e-9 and p["qty"] * p["entry"] <= 3000 + 1e-9
    k2 = {"time": 2, "open": 10.5, "high": 10.6, "low": 9.6, "close": 9.7}
    ev = step("X", st, k2, {"signal": -1, "setup_high": 10.6, "setup_low": 9.6})
    assert [e[0] for e in ev] == ["exit", "entry"] and ev[0][1]["reason"] == "reverse"
    assert st["position"]["side"] == "short" and st["position"]["sl"] == 10.6
    k3 = {"time": 3, "open": 10, "high": 11, "low": 9.9, "close": 10.8}
    ev = step("X", st, k3, {"signal": 1, "setup_high": 11, "setup_low": 9.9})
    assert len(ev) == 1 and ev[0][1]["reason"] == "stop" and ev[0][1]["exit"] > 10.6 and st["position"] is None
