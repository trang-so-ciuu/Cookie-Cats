"""Behavior tests for the Cookie Cats analysis."""

import unittest

from analysis import retention_summary, rounds_bucket, two_proportion_ztest


class AnalysisTest(unittest.TestCase):
    def test_rounds_buckets_cover_boundaries(self) -> None:
        self.assertEqual(rounds_bucket(0), "0")
        self.assertEqual(rounds_bucket(29), "1-29")
        self.assertEqual(rounds_bucket(30), "30-39")
        self.assertEqual(rounds_bucket(40), "40-89")
        self.assertEqual(rounds_bucket(90), "90+")

    def test_identical_proportions_are_not_significant(self) -> None:
        statistic, p_value = two_proportion_ztest(50, 100, 50, 100)
        self.assertEqual(statistic, 0)
        self.assertEqual(p_value, 1)

    def test_summary_reports_gate_40_effect(self) -> None:
        rows = [
            {"version": "gate_30", "retention_1": 1, "retention_7": 1},
            {"version": "gate_30", "retention_1": 1, "retention_7": 0},
            {"version": "gate_40", "retention_1": 0, "retention_7": 0},
            {"version": "gate_40", "retention_1": 1, "retention_7": 0},
        ]
        summary = retention_summary(rows)
        self.assertEqual(summary[0]["gate_40_minus_gate_30"], -0.5)


if __name__ == "__main__":
    unittest.main()
