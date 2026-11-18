import unittest

from tools.summarize_results import ROOT, summarize


class ReportedResultsTests(unittest.TestCase):
    def test_matches_published_figures(self):
        summary, total = summarize(ROOT / "data/reported_metrics.csv")
        self.assertEqual(format(summary["9"]["map50"], ".3f"), "0.826")
        self.assertEqual(format(summary["5"]["map50"], ".3f"), "0.815")
        self.assertEqual(total, 15939)
        self.assertEqual(summary["9"]["lowest_class"], "CS")
        self.assertEqual(summary["5"]["lowest_class"], "CS")


if __name__ == "__main__":
    unittest.main()
