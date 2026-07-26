from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate-skills"


class ValidateSkillsTests(unittest.TestCase):
    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), "--root", str(root)],
            check=False,
            capture_output=True,
            text=True,
        )

    def add_skill(
        self,
        root: Path,
        name: str,
        description: str = "Use when focused alpha behavior needs careful handling.",
    ) -> None:
        skill_dir = root / "skills" / name
        (skill_dir / "agents").mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: {description}\n---\n\n"
            f"# {name.replace('-', ' ').title()}\n"
        )
        (skill_dir / "agents" / "openai.yaml").write_text(
            "interface:\n"
            f'  display_name: "{name.replace("-", " ").title()}"\n'
            '  short_description: "Handle focused behavior with careful checks."\n'
            f'  default_prompt: "Use ${name} to handle this request safely."\n'
        )

    def make_fixture(self) -> tempfile.TemporaryDirectory[str]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        (root / ".codex-plugin").mkdir()
        (root / "evals").mkdir()
        (root / ".codex-plugin" / "plugin.json").write_text(
            json.dumps({"name": "fixture", "version": "1.0.0", "skills": "./skills/"})
        )
        self.add_skill(root, "alpha-skill")
        (root / "README.md").write_text(
            "# Fixture\n\n## Skills\n\n- `alpha-skill`: fixture skill.\n\n## End\n"
        )
        (root / "evals" / "scenarios.json").write_text(
            json.dumps(
                {
                    "version": 1,
                    "scenarios": [
                        {
                            "id": "alpha-basic",
                            "skill": "alpha-skill",
                            "request": "Handle the alpha case.",
                            "expected": {
                                "must": ["Follow the alpha workflow."],
                                "must_not": ["Mutate unrelated state."],
                            },
                        }
                    ],
                }
            )
        )
        return temporary

    def test_current_repository_passes(self) -> None:
        result = self.run_validator(REPO_ROOT)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_metadata_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            (root / "skills" / "alpha-skill" / "agents" / "openai.yaml").unlink()
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing agents/openai.yaml", result.stderr)

    def test_broken_skill_reference_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            path = root / "skills" / "alpha-skill" / "SKILL.md"
            path.write_text(path.read_text() + "\nUse $missing-skill.\n")
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("references missing skill $missing-skill", result.stderr)

    def test_missing_readme_entry_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# Fixture\n\n## Skills\n\n## End\n")
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing skill entries: alpha-skill", result.stderr)

    def test_non_object_manifest_fails_without_traceback(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            (root / ".codex-plugin" / "plugin.json").write_text("[]")
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("plugin manifest must be a JSON object", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_invalid_eval_skill_reference_fails_without_traceback(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            scenarios_path = root / "evals" / "scenarios.json"
            scenarios = json.loads(scenarios_path.read_text())
            scenarios["scenarios"][0]["skill"] = ["alpha-skill"]
            scenarios_path.write_text(json.dumps(scenarios))
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("skill must name an existing skill", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_invalid_single_quoted_yaml_scalar_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            metadata = root / "skills" / "alpha-skill" / "agents" / "openai.yaml"
            metadata.write_text(
                metadata.read_text().replace(
                    '"Alpha Skill"', "'Owner's Tools'"
                )
            )
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "single quotes inside a YAML string must be escaped", result.stderr
        )

    def test_invalid_plain_scalar_colon_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            skill = root / "skills" / "alpha-skill" / "SKILL.md"
            skill.write_text(
                skill.read_text().replace(
                    "description: Use when focused alpha behavior needs careful handling.",
                    "description: Use when: focused alpha behavior needs careful handling.",
                )
            )
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsupported YAML plain-scalar syntax", result.stderr)

    def test_implicit_yaml_boolean_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            skill = root / "skills" / "alpha-skill" / "SKILL.md"
            skill.write_text(
                skill.read_text().replace(
                    "description: Use when focused alpha behavior needs careful handling.",
                    "description: true",
                )
            )
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ambiguous YAML non-string scalar", result.stderr)

    def test_forbidden_plain_scalar_start_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            skill = root / "skills" / "alpha-skill" / "SKILL.md"
            skill.write_text(
                skill.read_text().replace(
                    "description: Use when focused alpha behavior needs careful handling.",
                    "description: @owner tools",
                )
            )
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "use a single-line string scalar for skill metadata", result.stderr
        )

    def test_description_overlap_warns_without_failing(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            description = "Use when focused alpha behavior needs careful handling."
            self.add_skill(root, "beta-skill", description)
            readme = root / "README.md"
            readme.write_text(
                readme.read_text().replace(
                    "\n## End", "\n- `beta-skill`: fixture skill.\n\n## End"
                )
            )
            scenarios_path = root / "evals" / "scenarios.json"
            scenarios = json.loads(scenarios_path.read_text())
            scenarios["scenarios"].append(
                {
                    "id": "beta-basic",
                    "skill": "beta-skill",
                    "request": "Handle the beta case.",
                    "expected": {
                        "must": ["Follow the beta workflow."],
                        "must_not": ["Mutate unrelated state."],
                    },
                }
            )
            scenarios_path.write_text(json.dumps(scenarios))
            result = self.run_validator(root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[WARN] description overlap 1.00", result.stdout)


if __name__ == "__main__":
    unittest.main()
