import unittest

from kztool import build_prompt
from textstats import stats


class ToolsTests(unittest.TestCase):
    def test_stats_counts(self):
        s = stats("Бұл бірінші сөйлем. Бұл екінші сөйлем! Үшінші?")
        self.assertEqual(s["sentences"], 3)
        self.assertEqual(s["words"], 7)
        self.assertEqual(s["top_words"][0][0], "сөйлем")

    def test_stats_empty(self):
        s = stats("")
        self.assertEqual((s["words"], s["sentences"]), (0, 0))

    def test_prompts_mention_language_and_text(self):
        p = build_prompt("translate", "Hello", "kk")
        self.assertIn("Kazakh", p)
        self.assertIn("Hello", p)
        self.assertIn("bullet", build_prompt("summarize", "x", "en"))
        self.assertIn("simple", build_prompt("simplify", "x", "ru"))


if __name__ == "__main__":
    unittest.main()
