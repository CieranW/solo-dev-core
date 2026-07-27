import tomllib
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class AutomationTests(unittest.TestCase):
    def test_only_compact_weekly_digest_is_scheduled(self) -> None:
        definitions = sorted((REPO_ROOT / "automations").glob("*/automation.toml"))
        self.assertEqual(
            definitions,
            [
                REPO_ROOT
                / "automations"
                / "weekly-engineering-director-digest"
                / "automation.toml"
            ],
        )

        with definitions[0].open("rb") as handle:
            automation = tomllib.load(handle)

        self.assertEqual(automation["id"], "weekly-engineering-director-digest")
        self.assertEqual(automation["status"], "ACTIVE")
        self.assertEqual(automation["model"], "gpt-5.6-sol")
        self.assertEqual(automation["reasoning_effort"], "medium")
        self.assertIn("Deep-inspect no more than five repositories", automation["prompt"])
        self.assertIn("Stop once five actionable findings", automation["prompt"])
        self.assertIn("Output no more than 300 words", automation["prompt"])


if __name__ == "__main__":
    unittest.main()
