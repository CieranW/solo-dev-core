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
        (skill_dir / "agents").mkdir(parents=True, exist_ok=True)
        (skill_dir / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: {description}\n---\n\n"
            f"# {name.replace('-', ' ').title()}\n\n"
            "## Boundaries\n\nUse for the named fixture behavior.\n\n"
            "## Workflow\n\n1. Inspect the fixture.\n\n"
            "## Evidence\n\nReport the inspected fixture.\n\n"
            "## Output Contract\n\nReturn the fixture result.\n\n"
            "## Stop Conditions\n\nStop after the result.\n\n"
            "## Composition\n\nDo not invoke unrelated fixture skills.\n"
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
        (root / "global").mkdir()
        (root / ".codex-plugin" / "plugin.json").write_text(
            json.dumps({"name": "fixture", "version": "1.0.0", "skills": "./skills/"})
        )
        director_contract = "Codex is always the Engineering Director.\n"
        (root / "AGENTS.md").write_text(director_contract)
        (root / "global" / "AGENTS.md").write_text(director_contract)
        self.add_skill(root, "alpha-skill")
        self.add_skill(
            root,
            "beta-skill",
            "Use when bounded beta release evidence must be selected.",
        )
        (root / "README.md").write_text(
            "# Fixture\n\n## Skills\n\n"
            "- `alpha-skill`: fixture skill.\n"
            "- `beta-skill`: second fixture skill.\n\n"
            "## End\n"
        )
        (root / "evals" / "scenarios.json").write_text(
            json.dumps(
                {
                    "version": 2,
                    "scenarios": [
                        {
                            "id": "alpha-basic",
                            "request": "Handle the alpha case.",
                            "expected": {
                                "skills": ["alpha-skill"],
                                "must_not_select": ["beta-skill"],
                                "mutation": "read-only",
                                "output": ["Follow the alpha workflow."],
                                "failure_indicators": ["Mutate unrelated state."],
                            },
                        },
                        {
                            "id": "beta-basic",
                            "request": "Handle the beta case.",
                            "expected": {
                                "skills": ["beta-skill"],
                                "must_not_select": ["alpha-skill"],
                                "mutation": "read-only",
                                "output": ["Follow the beta workflow."],
                                "failure_indicators": ["Mutate unrelated state."],
                            },
                        },
                    ],
                }
            )
        )
        return temporary

    def test_current_repository_passes(self) -> None:
        result = self.run_validator(REPO_ROOT)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_engineering_director_identity_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            (root / "global" / "AGENTS.md").write_text("Generic instructions.\n")
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must state 'Codex is always the Engineering Director'", result.stderr)

    def test_leadership_skill_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            self.add_skill(root, "lead-engineer")
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "leadership is an always-active root identity, not a skill: lead-engineer",
            result.stderr,
        )

    def test_engineering_director_scenario_may_select_no_skill(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            scenarios_path = root / "evals" / "scenarios.json"
            scenarios = json.loads(scenarios_path.read_text())
            scenarios["scenarios"].append(
                {
                    "id": "engineering-director-root-only",
                    "request": "Decide whether this tiny task needs delegation.",
                    "expected": {
                        "skills": [],
                        "must_not_select": ["alpha-skill", "beta-skill"],
                        "mutation": "read-only",
                        "output": ["Work directly without selecting a procedure."],
                        "failure_indicators": ["Selects a skill unnecessarily."],
                    },
                }
            )
            scenarios_path.write_text(json.dumps(scenarios))
            result = self.run_validator(root)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_empty_skills_requires_engineering_director_scenario(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            scenarios_path = root / "evals" / "scenarios.json"
            scenarios = json.loads(scenarios_path.read_text())
            scenarios["scenarios"][0]["expected"]["skills"] = []
            scenarios_path.write_text(json.dumps(scenarios))
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "expected.skills may be empty only for an engineering-director-",
            result.stderr,
        )

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
            scenarios["scenarios"][0]["expected"]["skills"] = ["missing-skill"]
            scenarios_path.write_text(json.dumps(scenarios))
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("expected.skills names unknown skills", result.stderr)
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
            result = self.run_validator(root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[WARN] description overlap 1.00", result.stdout)

    def test_missing_required_skill_section_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            skill = root / "skills" / "alpha-skill" / "SKILL.md"
            skill.write_text(skill.read_text().replace("## Evidence", "## Proof"))
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required sections: ## Evidence", result.stderr)

    def test_empty_required_skill_section_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            skill = root / "skills" / "alpha-skill" / "SKILL.md"
            skill.write_text(
                skill.read_text().replace(
                    "## Evidence\n\nReport the inspected fixture.",
                    "## Evidence\n",
                )
            )
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("empty required section: ## Evidence", result.stderr)

    def test_duplicate_required_skill_section_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            skill = root / "skills" / "alpha-skill" / "SKILL.md"
            skill.write_text(
                skill.read_text() + "\n## Evidence\n\nDuplicate evidence contract.\n"
            )
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate required section: ## Evidence", result.stderr)

    def test_readme_ignores_backticked_boundary_terms(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            readme = root / "README.md"
            readme.write_text(
                readme.read_text().replace(
                    "- `alpha-skill`: fixture skill.",
                    "- `alpha-skill`: fixture skill with a `read-only` boundary.",
                )
            )
            result = self.run_validator(root)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_unresolved_skill_placeholder_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            skill = root / "skills" / "alpha-skill" / "SKILL.md"
            skill.write_text(skill.read_text() + "\n[TODO: replace this]\n")
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("contains an unresolved TODO placeholder", result.stderr)

    def test_invalid_eval_mutation_policy_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            scenarios_path = root / "evals" / "scenarios.json"
            scenarios = json.loads(scenarios_path.read_text())
            scenarios["scenarios"][0]["expected"]["mutation"] = "sometimes"
            scenarios_path.write_text(json.dumps(scenarios))
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("expected.mutation must be one of", result.stderr)

    def test_selected_and_forbidden_skill_fails(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            scenarios_path = root / "evals" / "scenarios.json"
            scenarios = json.loads(scenarios_path.read_text())
            scenarios["scenarios"][0]["expected"]["must_not_select"] = [
                "alpha-skill"
            ]
            scenarios_path.write_text(json.dumps(scenarios))
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("skills cannot be both selected and forbidden", result.stderr)

    def test_unknown_eval_fields_fail(self) -> None:
        with self.make_fixture() as directory:
            root = Path(directory)
            scenarios_path = root / "evals" / "scenarios.json"
            scenarios = json.loads(scenarios_path.read_text())
            scenarios["legacy"] = True
            scenarios["scenarios"][0]["skill"] = "alpha-skill"
            scenarios["scenarios"][0]["expected"]["must"] = ["legacy wording"]
            scenarios_path.write_text(json.dumps(scenarios))
            result = self.run_validator(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown top-level fields: legacy", result.stderr)
        self.assertIn("unknown scenario fields: skill", result.stderr)
        self.assertIn("unknown expected fields: must", result.stderr)


if __name__ == "__main__":
    unittest.main()
