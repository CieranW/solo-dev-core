from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "project-memory"
PROJECT_MEMORY_SKILL = REPO_ROOT / "skills" / "adopt-project"
BUNDLED_VALIDATOR = PROJECT_MEMORY_SKILL / "scripts" / "project-memory"
PROJECT_TEMPLATE = PROJECT_MEMORY_SKILL / "assets" / "PROJECT.md"
ADR_TEMPLATE = PROJECT_MEMORY_SKILL / "assets" / "ADR.md"
PROJECT_SECTIONS = [
    "North Star",
    "Product Boundaries",
    "Current Milestone",
    "Success and Stop Conditions",
    "Verified Current State",
    "Active Work",
    "Next",
    "Future Ideas",
    "Deferred",
    "Decisions",
    "Risks and Unknowns",
    "Exact Next Action",
    "Last Verified",
]
PROJECT_FIELDS = {
    "North Star": ["Outcome", "Intended user"],
    "Product Boundaries": ["In scope", "Out of scope", "Detailed sources"],
    "Current Milestone": ["Name", "Outcome", "Status", "Scope"],
    "Success and Stop Conditions": ["Success", "Stop or pivot when"],
    "Verified Current State": ["Implemented", "Evidence"],
    "Active Work": ["Batch", "State", "Branch"],
    "Next": ["Candidate", "Justification"],
    "Exact Next Action": ["Action"],
    "Last Verified": [
        "At",
        "Commit",
        "Branch",
        "Working tree",
        "Validation level",
        "Evidence",
    ],
}
ADR_SECTIONS = [
    "Status",
    "Context",
    "Decision",
    "Rationale",
    "Alternatives",
    "Consequences",
    "Revisit Trigger",
]
FUTURE_FIELDS = [
    "Idea",
    "Value",
    "Dependencies",
    "Reconsider when",
    "Why deferred",
    "Related decisions or components",
    "Captured",
]


class ProjectMemoryTests(unittest.TestCase):
    def run_validator(
        self, *arguments: str
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def make_project(self) -> tempfile.TemporaryDirectory[str]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        (root / "docs").mkdir()
        shutil.copyfile(PROJECT_TEMPLATE, root / "docs" / "PROJECT.md")
        return temporary

    def write_registry(
        self, root: Path, projects: list[dict[str, str]]
    ) -> Path:
        path = root / "projects.json"
        path.write_text(
            json.dumps({"version": 1, "projects": projects}),
            encoding="utf-8",
        )
        return path

    def remove_project_field(
        self, content: str, section: str, field: str
    ) -> str:
        marker = f"## {section}\n"
        start = content.index(marker) + len(marker)
        end = content.find("\n## ", start)
        if end == -1:
            end = len(content)
        body = content[start:end]
        lines = [
            line
            for line in body.splitlines()
            if not line.startswith(f"- {field}:")
        ]
        return content[:start] + "\n".join(lines) + content[end:]

    def future_idea(self) -> str:
        return (
            "### FI-20260727-local-cache — Add a local cache\n\n"
            "- Idea: Cache repeated portfolio reads.\n"
            "- Value: Reduce repeated work.\n"
            "- Dependencies: None.\n"
            "- Reconsider when: Portfolio reads exceed five seconds.\n"
            "- Why deferred: The uncached workflow is not proven.\n"
            "- Related decisions or components: None.\n"
            "- Captured: 2026-07-27"
        )

    def test_canonical_project_and_adr_templates_pass(self) -> None:
        with self.make_project() as directory:
            root = Path(directory)
            decisions = root / "docs" / "decisions"
            decisions.mkdir()
            shutil.copyfile(
                ADR_TEMPLATE,
                decisions / "ADR-20260727-example-decision.md",
            )
            result = self.run_validator("validate-project", "--repo", str(root))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1 ADR(s)", result.stdout)

    def test_skills_only_payload_supports_project_memory(self) -> None:
        with (
            tempfile.TemporaryDirectory() as payload_directory,
            tempfile.TemporaryDirectory() as target_directory,
            tempfile.TemporaryDirectory() as registry_directory,
        ):
            payload = Path(payload_directory)
            shutil.copytree(REPO_ROOT / "skills", payload / "skills")
            (payload / ".codex-plugin").mkdir()
            shutil.copyfile(
                REPO_ROOT / ".codex-plugin" / "plugin.json",
                payload / ".codex-plugin" / "plugin.json",
            )

            installed_skill = payload / "skills" / "adopt-project"
            target = Path(target_directory)
            (target / "docs").mkdir()
            shutil.copyfile(
                installed_skill / "assets" / "PROJECT.md",
                target / "docs" / "PROJECT.md",
            )
            project_result = subprocess.run(
                [
                    sys.executable,
                    str(installed_skill / "scripts" / "project-memory"),
                    "validate-project",
                    "--repo",
                    str(target),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(project_result.returncode, 0, project_result.stderr)

            registry_root = Path(registry_directory)
            registry = self.write_registry(registry_root, [])
            paths = registry_root / "paths.local.json"
            paths.write_text(
                json.dumps({"version": 1, "paths": {}}),
                encoding="utf-8",
            )
            registry_result = subprocess.run(
                [
                    sys.executable,
                    str(installed_skill / "scripts" / "project-memory"),
                    "validate-registry",
                    "--registry",
                    str(registry),
                    "--paths",
                    str(paths),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(registry_result.returncode, 0, registry_result.stderr)

        lifecycle_contracts = "\n".join(
            (REPO_ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            for name in (
                "adopt-project",
                "project-status",
                "start-work",
                "finish-work",
                "capture-idea",
                "roadmap-review",
            )
        )
        self.assertNotIn("`templates/PROJECT.md`", lifecycle_contracts)
        self.assertNotIn("`templates/ADR.md`", lifecycle_contracts)
        self.assertNotIn("`registry/projects.json`", lifecycle_contracts)

    def test_every_required_project_section_is_enforced(self) -> None:
        for section in PROJECT_SECTIONS:
            with self.subTest(section=section), self.make_project() as directory:
                root = Path(directory)
                project = root / "docs" / "PROJECT.md"
                project.write_text(
                    project.read_text(encoding="utf-8").replace(
                        f"## {section}\n", f"### {section}\n", 1
                    ),
                    encoding="utf-8",
                )
                result = self.run_validator(
                    "validate-project", "--repo", str(root)
                )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("H2 sections must exactly match", result.stderr)

    def test_every_required_project_field_is_enforced(self) -> None:
        for section, fields in PROJECT_FIELDS.items():
            for field in fields:
                with (
                    self.subTest(section=section, field=field),
                    self.make_project() as directory,
                ):
                    root = Path(directory)
                    project = root / "docs" / "PROJECT.md"
                    project.write_text(
                        self.remove_project_field(
                            project.read_text(encoding="utf-8"),
                            section,
                            field,
                        ),
                        encoding="utf-8",
                    )
                    result = self.run_validator(
                        "validate-project", "--repo", str(root)
                    )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(
                    f"section '{section}' is missing fields", result.stderr
                )
                self.assertIn(field, result.stderr)

    def test_future_idea_without_reconsideration_trigger_fails(self) -> None:
        with self.make_project() as directory:
            root = Path(directory)
            project = root / "docs" / "PROJECT.md"
            future = self.future_idea().replace(
                "- Reconsider when: Portfolio reads exceed five seconds.\n",
                "",
            )
            project.write_text(
                project.read_text(encoding="utf-8").replace("_None._", future, 1),
                encoding="utf-8",
            )
            result = self.run_validator("validate-project", "--repo", str(root))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Reconsider when", result.stderr)

    def test_every_required_future_idea_field_is_enforced(self) -> None:
        for field in FUTURE_FIELDS:
            with self.subTest(field=field), self.make_project() as directory:
                root = Path(directory)
                project = root / "docs" / "PROJECT.md"
                future = "\n".join(
                    line
                    for line in self.future_idea().splitlines()
                    if not line.startswith(f"- {field}:")
                )
                project.write_text(
                    project.read_text(encoding="utf-8").replace(
                        "_None._", future, 1
                    ),
                    encoding="utf-8",
                )
                result = self.run_validator(
                    "validate-project", "--repo", str(root)
                )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("is missing fields", result.stderr)
            self.assertIn(field, result.stderr)

    def test_future_idea_date_must_match_identifier(self) -> None:
        with self.make_project() as directory:
            root = Path(directory)
            project = root / "docs" / "PROJECT.md"
            future = self.future_idea().replace(
                "- Captured: 2026-07-27", "- Captured: 2026-07-26"
            )
            project.write_text(
                project.read_text(encoding="utf-8").replace("_None._", future, 1),
                encoding="utf-8",
            )
            result = self.run_validator("validate-project", "--repo", str(root))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("date does not match Captured", result.stderr)

    def test_duplicate_future_idea_identifier_fails(self) -> None:
        with self.make_project() as directory:
            root = Path(directory)
            project = root / "docs" / "PROJECT.md"
            future = f"{self.future_idea()}\n\n{self.future_idea()}"
            project.write_text(
                project.read_text(encoding="utf-8").replace("_None._", future, 1),
                encoding="utf-8",
            )
            result = self.run_validator("validate-project", "--repo", str(root))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate Future Idea id", result.stderr)

    def test_invalid_adr_status_fails(self) -> None:
        with self.make_project() as directory:
            root = Path(directory)
            decisions = root / "docs" / "decisions"
            decisions.mkdir()
            adr = decisions / "ADR-20260727-example-decision.md"
            shutil.copyfile(ADR_TEMPLATE, adr)
            adr.write_text(
                adr.read_text(encoding="utf-8").replace(
                    "## Status\n\nProposed", "## Status\n\nMaybe"
                ),
                encoding="utf-8",
            )
            result = self.run_validator("validate-project", "--repo", str(root))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ADR Status must be one of", result.stderr)

    def test_every_required_adr_section_is_enforced(self) -> None:
        for section in ADR_SECTIONS:
            with self.subTest(section=section), self.make_project() as directory:
                root = Path(directory)
                decisions = root / "docs" / "decisions"
                decisions.mkdir()
                adr = decisions / "ADR-20260727-example-decision.md"
                shutil.copyfile(ADR_TEMPLATE, adr)
                adr.write_text(
                    adr.read_text(encoding="utf-8").replace(
                        f"## {section}\n", f"### {section}\n", 1
                    ),
                    encoding="utf-8",
                )
                result = self.run_validator(
                    "validate-project", "--repo", str(root)
                )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("required ADR order", result.stderr)

    def test_empty_registry_and_example_mapping_pass(self) -> None:
        result = self.run_validator(
            "validate-registry",
            "--registry",
            str(REPO_ROOT / "registry" / "projects.json"),
            "--paths",
            str(REPO_ROOT / "registry" / "paths.local.example.json"),
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("0 project(s), 0 local path(s)", result.stdout)

    def test_duplicate_project_identifier_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = self.write_registry(
                root,
                [
                    {
                        "id": "alpha",
                        "name": "Alpha",
                        "remote": "github.com/example/alpha",
                    },
                    {
                        "id": "alpha",
                        "name": "Alpha copy",
                        "remote": "github.com/example/alpha-copy",
                    },
                ],
            )
            result = self.run_validator(
                "validate-registry", "--registry", str(registry)
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate project id 'alpha'", result.stderr)

    def test_every_required_registry_field_is_enforced(self) -> None:
        complete = {
            "id": "alpha",
            "name": "Alpha",
            "remote": "github.com/example/alpha",
        }
        for field in complete:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                project = dict(complete)
                project.pop(field)
                registry = self.write_registry(root, [project])
                result = self.run_validator(
                    "validate-registry", "--registry", str(registry)
                )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(f"is missing fields: {field}", result.stderr)

    def test_unknown_local_mapping_identifier_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = self.write_registry(root, [])
            paths = root / "paths.local.json"
            paths.write_text(
                json.dumps(
                    {
                        "version": 1,
                        "paths": {"unknown-project": "/tmp/unknown-project"},
                    }
                ),
                encoding="utf-8",
            )
            result = self.run_validator(
                "validate-registry",
                "--registry",
                str(registry),
                "--paths",
                str(paths),
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown project id 'unknown-project'", result.stderr)

    def test_relative_local_mapping_path_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = self.write_registry(
                root,
                [
                    {
                        "id": "alpha",
                        "name": "Alpha",
                        "remote": "github.com/example/alpha",
                    }
                ],
            )
            paths = root / "paths.local.json"
            paths.write_text(
                json.dumps({"version": 1, "paths": {"alpha": "../alpha"}}),
                encoding="utf-8",
            )
            result = self.run_validator(
                "validate-registry",
                "--registry",
                str(registry),
                "--paths",
                str(paths),
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must be absolute", result.stderr)

    def test_duplicate_json_key_fails_without_traceback(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            registry = Path(directory) / "projects.json"
            registry.write_text(
                '{"version": 1, "version": 1, "projects": []}',
                encoding="utf-8",
            )
            result = self.run_validator(
                "validate-registry", "--registry", str(registry)
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate JSON key 'version'", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
