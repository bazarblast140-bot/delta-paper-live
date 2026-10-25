import unittest
from daytrader.strategy import step, opening_range, _size, RISK, LEV, MAX_LOSS_USD, OR_BARS


def mk(prices, rng=1.0):
    return [{"time": 900 * i, "open": p, "high": p + rng, "low": p - rng, "close": p}
            for i, p in enumerate(prices)]


class T(unittest.TestCase):
    def run_from(self, c, start=0):
        st = {"equity": 1000.0, "position": None}
        ev = []
        for i in range(start, len(c)):
            ev += step("X", st, c, i)
        return st, ev

    def test_or_excludes_current(self):
        c = mk([100, 100, 110])
        hi, lo = opening_range(c, 2, 1)
        self.assertEqual(hi, 101)
        self.assertEqual(lo, 99)

    def test_long_fresh_break_then_target(self):
        # bar0 range 99-101; bar1 close 102 breaks up; bar2 hits 1R target
        c = mk([100, 102, 105], rng=1.0)
        # i=1: OR=bar0 high=101 low=99; close 102 > 101, prev 100 <= 101 → long
        st, ev = self.run_from(c, start=1)
        self.assertEqual(ev[0][0], "entry")
        self.assertEqual(ev[0][1]["side"], "long")
        self.assertEqual(ev[0][1]["sl"], 99)
        self.assertEqual(ev[0][1]["entry"], 102)
        risk = 102 - 99
        self.assertAlmostEqual(ev[0][1]["target"], 102 + risk)
        # i=2 high=106 >= target 105 → target exit
        self.assertEqual(ev[-1][0], "exit")
        self.assertEqual(ev[-1][1]["reason"], "target_1R")
        self.assertIsNone(st["position"])
        self.assertGreater(st["equity"], 1000)

    def test_short_fresh_break_then_stop(self):
        c = mk([100, 98, 102], rng=1.0)
        # i=1: OR high=101 low=99; close 98 < 99 → short; SL=101
        st = {"equity": 1000.0, "position": None}
        ev = step("X", st, c, 1)
        self.assertEqual(ev[0][1]["side"], "short")
        self.assertEqual(st["position"]["sl"], 101)
        # i=2: high 103 >= SL 101 → stop
        ev2 = step("X", st, c, 2)
        self.assertEqual(ev2[0][1]["reason"], "stop")
        self.assertIsNone(st["position"])
        self.assertLess(st["equity"], 1000)

    def test_no_reentry_same_bar_after_exit(self):
        c = mk([100, 102, 95], rng=1.0)
        st = {"equity": 1000.0, "position": None}
        step("X", st, c, 1)  # long
        # force stop on bar 2 and ensure no re-entry in same step return
        c[2] = {"time": 1800, "open": 101, "high": 101, "low": 90, "close": 95}
        ev = step("X", st, c, 2)
        self.assertEqual(len(ev), 1)
        self.assertEqual(ev[0][0], "exit")
        self.assertIsNone(st["position"])

    def test_no_signal_inside_range(self):
        c = mk([100, 100.5], rng=2.0)  # close 100.5 inside 98-102
        st, ev = self.run_from(c, start=1)
        self.assertEqual(ev, [])

    def test_not_fresh_break_no_entry(self):
        # already above OR for two bars — second bar should not re-fire without cross
        c = [
            {"time": 0, "open": 100, "high": 101, "low": 99, "close": 100},
            {"time": 900, "open": 102, "high": 103, "low": 101.5, "close": 102.5},
            {"time": 1800, "open": 103, "high": 104, "low": 102, "close": 103.5},
        ]
        st = {"equity": 1000.0, "position": None}
        step("X", st, c, 1)  # enters long
        # close that position manually then check bar 2
        st["position"] = None
        # OR for i=2 is bar1: high 103 low 101.5; close 103.5 > 103 but prev close 102.5 was already > … 
        # prev close 102.5 <= OR high 103? 102.5 <= 103 → yes would still be fresh vs bar1 OR
        # Build clearer: prev already above current OR
        c2 = [
            {"time": 0, "open": 100, "high": 101, "low": 99, "close": 100},
            {"time": 900, "open": 100, "high": 100.5, "low": 99.5, "close": 105},  # already way above
            {"time": 1800, "open": 105, "high": 106, "low": 104, "close": 105.5},
        ]
        st2 = {"equity": 1000.0, "position": None}
        # skip entering on bar1; only evaluate bar2: OR=bar1 hi=100.5 lo=99.5; prev close 105 > OR high → not fresh
        ev = step("X", st2, c2, 2)
        self.assertEqual(ev, [])

    def test_one_percent_risk_and_caps(self):
        c = mk([100, 105], rng=1.0)
        st, ev = self.run_from(c, start=1)
        p = st["position"]
        risk_usd = abs(p["entry"] - p["sl"]) * p["qty"]
        self.assertLessEqual(risk_usd, MAX_LOSS_USD + 1e-6)
        self.assertLessEqual(risk_usd, 1000 * RISK + 1e-6)
        self.assertLessEqual(p["qty"] * p["entry"], 1000 * LEV + 1e-6)

    def test_size_respects_max_loss(self):
        # wide stop: 1% of 1000 = 10 but MAX_LOSS=15 so 10 wins; tighter check with huge equity risk
        qty = _size(1000, 100, 50)  # dist 50 → 1% = 10/50=0.2; lev=30/100=30 → 0.2; maxloss 15/50=0.3 → 0.2
        self.assertAlmostEqual(qty, 0.2)
        qty2 = _size(5000, 100, 99)  # dist 1 → risk 50, lev 150, maxloss 15 → 15
        self.assertAlmostEqual(qty2, 15.0)


if __name__ == "__main__":
    unittest.main()
