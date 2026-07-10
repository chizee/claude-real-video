"""Minimal smoke tests: the package imports and the CLI answers --help."""

import subprocess
import sys


def test_import():
    import claude_real_video

    assert hasattr(claude_real_video, "process")


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "-m", "claude_real_video", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "crv" in result.stdout.lower() or "video" in result.stdout.lower()
