import unittest
from paper.strategy import step, bands

def mk(prices, rng=1.0):
    return [{"time": 3600*i, "open": p, "high": p+rng, "low": p-rng, "close": p} for i, p in enumerate(prices)]

class T(unittest.TestCase):
    def run_all(self, c):
        st = {"equity": 1000.0, "position": None}; ev = []
        for i in range(len(c)): ev += step("X", st, c, i)
        return st, ev
    def test_no_signal_flat(self):
        st, ev = self.run_all(mk([100]*40)); self.assertEqual(ev, [])
    def test_long_breakout_then_mid_exit(self):
        p = [100]*25 + [105, 106, 107] + [95]
        st, ev = self.run_all(mk(p))
        self.assertEqual(ev[0][0], "entry"); self.assertEqual(ev[0][1]["side"], "long")
        self.assertEqual(ev[0][1]["entry"], 105)
        self.assertEqual(ev[-1][0], "exit")
        self.assertIn(ev[-1][1]["reason"], ("mid_exit", "stop"))
    def test_short_breakout(self):
        st, ev = self.run_all(mk([100]*25 + [95]))
        self.assertEqual(ev[0][1]["side"], "short"); self.assertGreater(st["position"]["sl"], 95)
    def test_stop_uses_taker_and_slippage(self):
        c = mk([100]*25 + [105]); st, ev = self.run_all(c)
        sl = st["position"]["sl"]
        c.append({"time": 3600*26, "open": 104, "high": 104, "low": sl-5, "close": 104})
        ev = step("X", st, c, 26)
        tr = ev[0][1]; self.assertEqual(tr["reason"], "stop"); self.assertLess(tr["exit"], sl)
        self.assertLess(tr["net"], 0); self.assertIsNone(st["position"])
    def test_fees_charged(self):
        st, ev = self.run_all(mk([100]*25 + [105, 105, 104.9, 90]))
        tr = [e for k, e in ev if k == "exit"][0]; self.assertGreater(tr["fees"], 0)
        self.assertAlmostEqual(tr["net"], tr["gross"] - tr["fees"], 3)
    def test_one_percent_risk(self):
        st, ev = self.run_all(mk([100]*25 + [105])); p = st["position"]
        risk = abs(p["entry"] - p["sl"]) * p["qty"]
        self.assertLessEqual(risk, 10.0 + 1e-9)
        self.assertLessEqual(p["qty"] * p["entry"], 3000 + 1e-9)
    def test_trailing_long_moves_up_never_down(self):
        c = mk([100]*25 + [105]); st, _ = self.run_all(c); sl0 = st["position"]["sl"]
        c.append({"time": 3600*26, "open": 108, "high": 109, "low": 107, "close": 108}); step("X", st, c, 26)
        sl1 = st["position"]["sl"]; self.assertGreater(sl1, sl0)
        c.append({"time": 3600*27, "open": 106, "high": 107, "low": 105.5, "close": 106}); step("X", st, c, 27)
        self.assertIsNotNone(st["position"]); self.assertGreaterEqual(st["position"]["sl"], sl1)
    def test_trailing_short_moves_down_never_up(self):
        c = mk([100]*25 + [95]); st, _ = self.run_all(c); sl0 = st["position"]["sl"]
        c.append({"time": 3600*26, "open": 92, "high": 93, "low": 91, "close": 92}); step("X", st, c, 26)
        sl1 = st["position"]["sl"]; self.assertLess(sl1, sl0)
        c.append({"time": 3600*27, "open": 94, "high": 94.5, "low": 93, "close": 94}); step("X", st, c, 27)
        self.assertIsNotNone(st["position"]); self.assertLessEqual(st["position"]["sl"], sl1)
    def test_trailed_stop_exit_reason(self):
        c = mk([100]*25 + [105]); st, _ = self.run_all(c)
        c.append({"time": 3600*26, "open": 120, "high": 121, "low": 119, "close": 120}); step("X", st, c, 26)
        sl = st["position"]["sl"]; self.assertGreater(sl, st["position"]["entry"])
        c.append({"time": 3600*27, "open": 119, "high": 119, "low": sl-1, "close": 118}); ev = step("X", st, c, 27)
        self.assertEqual(ev[0][1]["reason"], "stop"); self.assertGreater(ev[0][1]["net"], 0)
    def test_bands_exclude_current(self):
        c = mk([100]*20 + [200]); up, lo, mid = bands(c, 20); self.assertEqual(up, 101)

if __name__ == "__main__": unittest.main()
