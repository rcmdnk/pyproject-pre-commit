from __future__ import annotations

import sys

import pytest

from pyproject_pre_commit import __version__, main


@pytest.mark.parametrize(
    ("argv", "code", "out"),
    [
        (
            ["ppc"],
            0,
            "Usage: ppc <--pre-commit | --pyproject> [--ruff] [--black]\n",
        ),
        (
            ["ppc", "--wrong"],
            1,
            "Usage: ppc <--pre-commit | --pyproject> [--ruff] [--black]\n",
        ),
    ],
)
def test_sys_exit(
    argv: list[str], code: int, out: str | None, capsys: pytest.CaptureFixture
) -> None:
    sys.argv = argv
    with pytest.raises(SystemExit) as test:
        main()
    assert test.type is SystemExit
    assert test.value.code == code
    captured = capsys.readouterr()
    assert captured.out == out


def test_pre_commit(capsys: pytest.CaptureFixture) -> None:
    sys.argv = ["ppc", "--pre-commit"]
    main()
    captured = capsys.readouterr()
    assert captured.out.startswith("repos:\n")
    assert (
        "repo: https://github.com/rcmdnk/pyproject-pre-commit" in captured.out
    )
    assert f"v{__version__}" in captured.out


def test_pyproject(capsys: pytest.CaptureFixture) -> None:
    sys.argv = ["ppc", "--pyproject"]
    main()
    captured = capsys.readouterr()
    assert captured.out.startswith("[tool.black]\n")
