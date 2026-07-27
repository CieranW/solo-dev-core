from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEWER = REPO_ROOT / "skills" / "portfolio-review" / "scripts" / "portfolio-review"
PROJECT_TEMPLATE = (
    REPO_ROOT / "skills" / "adopt-project" / "assets" / "PROJECT.md"
)


class PortfolioReviewTests(unittest.TestCase):
    def run_reviewer(
        self, *arguments: str
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(REVIEWER), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def write_registry(
        self, root: Path, projects: list[dict[str, str]]
    ) -> Path:
        registry = root / "projects.json"
        registry.write_text(
            json.dumps({"version": 1, "projects": projects}),
            encoding="utf-8",
        )
        return registry

    def write_paths(self, root: Path, paths: dict[str, str]) -> Path:
        path = root / "paths.local.json"
        path.write_text(
            json.dumps({"version": 1, "paths": paths}),
            encoding="utf-8",
        )
        return path

    def project_entry(self, project_id: str) -> dict[str, str]:
        return {
            "id": project_id,
            "name": project_id.title(),
            "remote": f"github.com/example/{project_id}",
        }

    def make_project(self, root: Path) -> None:
        (root / "docs").mkdir(parents=True)
        content = PROJECT_TEMPLATE.read_text(encoding="utf-8")
        content = content.replace("- Name: Unset", "- Name: Import launch")
        content = content.replace("- Status: Uncertain", "- Status: Active")
        content = content.replace(
            "- Unknown: Project state has not been reconstructed.",
            "- Risk: Import latency remains unmeasured.",
        )
        content = content.replace(
            "- Action: Reconstruct repository state and replace the template defaults.",
            "- Action: Measure the largest representative import.",
        )
        content = content.replace("- At: Unverified", "- At: 2026-06-01")
        content = content.replace(
            "- Validation level: none", "- Validation level: focused"
        )
        content = content.replace(
            "_None._",
            (
                "### FI-20260601-streaming-import — Stream large imports\n\n"
                "- Idea: Stream large imports.\n"
                "- Value: Reduce peak memory.\n"
                "- Dependencies: Baseline import measurements.\n"
                "- Reconsider when: Review on 2026-07-01.\n"
                "- Why deferred: The current milestone is correctness.\n"
                "- Related decisions or components: Import pipeline.\n"
                "- Captured: 2026-06-01"
            ),
            1,
        )
        (root / "docs" / "PROJECT.md").write_text(content, encoding="utf-8")

    def git(self, repo: Path, *arguments: str) -> None:
        result = subprocess.run(
            ["git", "-C", str(repo), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_unavailable_repositories_do_not_fail_the_review(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = self.write_registry(
                root, [self.project_entry("alpha"), self.project_entry("beta")]
            )
            paths = self.write_paths(
                root, {"alpha": str(root / "not-cloned")}
            )
            result = self.run_reviewer(
                "--registry",
                str(registry),
                "--paths",
                str(paths),
                "--format",
                "json",
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["summary"]["unavailable"], 2)
        self.assertEqual(report["projects"][0]["availability"], "missing")
        self.assertEqual(report["projects"][1]["availability"], "unmapped")
        self.assertEqual(
            report["projects"][0]["recommended_action"],
            f"Restore or correct the local path mapping for alpha: "
            f"{root / 'not-cloned'}.",
        )
        self.assertEqual(
            report["next_action"], report["projects"][0]["recommended_action"]
        )
        self.assertIn("No repository", report["read_only_confirmation"])

    def test_project_memory_drives_stale_and_trigger_flags(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "alpha"
            self.make_project(repo)
            registry = self.write_registry(root, [self.project_entry("alpha")])
            paths = self.write_paths(root, {"alpha": str(repo)})
            result = self.run_reviewer(
                "--registry",
                str(registry),
                "--paths",
                str(paths),
                "--as-of",
                "2026-07-27",
                "--stale-after-days",
                "30",
                "--format",
                "json",
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        project = report["projects"][0]
        self.assertEqual(project["milestone"], {"name": "Import launch", "status": "Active"})
        self.assertEqual(project["last_verified"]["age_days"], 56)
        self.assertIn("stale-project-file", project["flags"])
        self.assertIn("future-trigger-candidate", project["flags"])
        self.assertEqual(project["future_ideas"][0]["signal"], "date-reached")
        self.assertEqual(
            project["next_action"], "Measure the largest representative import."
        )
        self.assertEqual(project["risks"], ["Risk: Import latency remains unmeasured."])
        self.assertIn("project-risk", project["flags"])
        self.assertEqual(
            report["next_action"],
            "Reconcile alpha project memory with project-status.",
        )

    def test_optional_git_inspection_reports_dirty_and_locally_ahead(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "alpha"
            remote = root / "alpha.git"
            repo.mkdir()
            self.git(repo, "init", "-b", "main")
            self.git(repo, "config", "user.email", "portfolio@example.invalid")
            self.git(repo, "config", "user.name", "Portfolio Test")
            self.make_project(repo)
            self.git(repo, "add", "docs/PROJECT.md")
            self.git(repo, "commit", "-m", "Add project memory")
            subprocess.run(
                ["git", "init", "--bare", str(remote)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.git(repo, "remote", "add", "origin", str(remote))
            self.git(repo, "push", "-u", "origin", "main")
            (repo / "ahead.txt").write_text("ahead\n", encoding="utf-8")
            self.git(repo, "add", "ahead.txt")
            self.git(repo, "commit", "-m", "Local ahead commit")
            (repo / "dirty.txt").write_text("dirty\n", encoding="utf-8")

            registry = self.write_registry(root, [self.project_entry("alpha")])
            paths = self.write_paths(root, {"alpha": str(repo)})
            result = self.run_reviewer(
                "--registry",
                str(registry),
                "--paths",
                str(paths),
                "--inspect-git",
                "--format",
                "json",
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        project = json.loads(result.stdout)["projects"][0]
        self.assertTrue(project["git"]["dirty"])
        self.assertEqual(project["git"]["ahead"], 1)
        self.assertIn("dirty-working-tree", project["flags"])
        self.assertIn("local-branch-ahead", project["flags"])
        self.assertEqual(
            json.loads(result.stdout)["next_action"],
            "Inspect and resolve the alpha working tree before portfolio planning.",
        )

    def test_text_output_includes_exact_action_and_read_only_confirmation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = self.write_registry(root, [])
            result = self.run_reviewer("--registry", str(registry))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "Exact portfolio next action: Adopt or register one project",
            result.stdout,
        )
        self.assertIn(
            "Read-only confirmation: no repository, registry, Git state, "
            "commit, or remote was changed.",
            result.stdout,
        )

    def test_invalid_mapping_stops_without_traceback(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = self.write_registry(root, [self.project_entry("alpha")])
            paths = self.write_paths(root, {"unknown": str(root)})
            result = self.run_reviewer(
                "--registry", str(registry), "--paths", str(paths)
            )
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown project", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
