from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
INSTALLER = REPO_ROOT / "scripts" / "install"
SKILLS_SOURCE = REPO_ROOT / "skills"
GLOBAL_SOURCE = REPO_ROOT / "global" / "AGENTS.md"


class InstallerTests(unittest.TestCase):
    def run_installer(
        self,
        root: Path,
        *arguments: str,
    ) -> subprocess.CompletedProcess[str]:
        skills_dir = root / ".agents" / "skills"
        global_file = root / ".codex" / "AGENTS.md"
        environment = os.environ.copy()
        environment["HOME"] = str(root)
        return subprocess.run(
            [
                str(INSTALLER),
                "--skills-dir",
                str(skills_dir),
                "--global-file",
                str(global_file),
                *arguments,
            ],
            check=False,
            capture_output=True,
            text=True,
            env=environment,
        )

    def skill_names(self) -> list[str]:
        return sorted(
            path.name
            for path in SKILLS_SOURCE.iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        )

    def assert_installed(self, root: Path) -> None:
        skills_dir = root / ".agents" / "skills"
        for name in self.skill_names():
            target = skills_dir / name
            self.assertTrue(target.is_symlink(), name)
            self.assertEqual(target.resolve(), (SKILLS_SOURCE / name).resolve())
            self.assertTrue((target / "SKILL.md").is_file())
        global_file = root / ".codex" / "AGENTS.md"
        self.assertTrue(global_file.is_symlink())
        self.assertEqual(global_file.resolve(), GLOBAL_SOURCE.resolve())

    def test_fresh_install_and_check_mode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            install = self.run_installer(root)
            self.assertEqual(install.returncode, 0, install.stderr)
            self.assert_installed(root)
            check = self.run_installer(root, "--check")
        self.assertEqual(check.returncode, 0, check.stderr)
        self.assertIn("Installation check passed", check.stdout)

    def test_second_install_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = self.run_installer(root)
            self.assertEqual(first.returncode, 0, first.stderr)
            links_before = {
                path.name: os.readlink(path)
                for path in (root / ".agents" / "skills").iterdir()
            }
            second = self.run_installer(root)
            links_after = {
                path.name: os.readlink(path)
                for path in (root / ".agents" / "skills").iterdir()
            }
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(links_before, links_after)
        self.assertIn("0 change(s)", second.stdout)

    def test_conflict_stops_before_any_changes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skills_dir = root / ".agents" / "skills"
            global_file = root / ".codex" / "AGENTS.md"
            skills_dir.mkdir(parents=True)
            global_file.parent.mkdir(parents=True)
            conflict = skills_dir / self.skill_names()[0]
            conflict.write_text("user-owned\n", encoding="utf-8")
            global_file.write_text("unrelated guidance\n", encoding="utf-8")
            result = self.run_installer(root)
            installed_links = list(skills_dir.glob("*"))
            self.assertEqual(result.returncode, 2)
            self.assertEqual(conflict.read_text(encoding="utf-8"), "user-owned\n")
            self.assertEqual(
                global_file.read_text(encoding="utf-8"), "unrelated guidance\n"
            )
            self.assertEqual(installed_links, [conflict])
            self.assertIn("stopped before changes", result.stderr)

    def test_replace_links_refreshes_only_symlinks(self) -> None:
        with (
            tempfile.TemporaryDirectory() as directory,
            tempfile.TemporaryDirectory() as old_directory,
        ):
            root = Path(directory)
            old_root = Path(old_directory)
            skills_dir = root / ".agents" / "skills"
            global_file = root / ".codex" / "AGENTS.md"
            skills_dir.mkdir(parents=True)
            global_file.parent.mkdir(parents=True)
            first_name = self.skill_names()[0]
            old_skill = old_root / first_name
            old_skill.mkdir()
            (old_skill / "SKILL.md").write_text("old\n", encoding="utf-8")
            old_global = old_root / "AGENTS.md"
            old_global.write_text("old\n", encoding="utf-8")
            (skills_dir / first_name).symlink_to(old_skill)
            global_file.symlink_to(old_global)
            result = self.run_installer(root, "--replace-links")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assert_installed(root)

    def test_dry_run_does_not_create_destinations(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result = self.run_installer(root, "--dry-run")
            skills_dir = root / ".agents" / "skills"
            global_file = root / ".codex" / "AGENTS.md"
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(skills_dir.exists())
            self.assertFalse(global_file.exists())
            self.assertIn("no files changed", result.stdout)

    def test_install_removes_retired_checkout_skill_link(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skills_dir = root / ".agents" / "skills"
            skills_dir.mkdir(parents=True)
            retired_link = skills_dir / "lead-engineer"
            retired_link.symlink_to(SKILLS_SOURCE / "lead-engineer")
            result = self.run_installer(root)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(retired_link.is_symlink())
            self.assertIn("[REMOVE] retired skill link", result.stdout)

    def test_install_preserves_unrelated_lead_engineer_link(self) -> None:
        with (
            tempfile.TemporaryDirectory() as directory,
            tempfile.TemporaryDirectory() as unrelated_directory,
        ):
            root = Path(directory)
            unrelated = Path(unrelated_directory) / "lead-engineer"
            unrelated.mkdir()
            (unrelated / "SKILL.md").write_text("unrelated\n", encoding="utf-8")
            skills_dir = root / ".agents" / "skills"
            skills_dir.mkdir(parents=True)
            retired_link = skills_dir / "lead-engineer"
            retired_link.symlink_to(unrelated)
            result = self.run_installer(root)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(retired_link.is_symlink())
            self.assertEqual(retired_link.resolve(), unrelated.resolve())

    def test_global_only_installs_no_skill_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result = self.run_installer(root, "--global-only")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((root / ".agents" / "skills").exists())
            global_file = root / ".codex" / "AGENTS.md"
            self.assertTrue(global_file.is_symlink())
            self.assertEqual(global_file.resolve(), GLOBAL_SOURCE.resolve())
            self.assertIn('scripts/install" --global-only', result.stdout)
            check = self.run_installer(root, "--global-only", "--check")
            self.assertEqual(check.returncode, 0, check.stderr)


if __name__ == "__main__":
    unittest.main()
