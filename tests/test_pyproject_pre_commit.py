import sys

import pytest

from pyproject_pre_commit import __version__, main


@pytest.mark.parametrize(
    "argv, code, out",
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
def test_sys_exit(argv, code, out, capsys):
    sys.argv = argv
    with pytest.raises(SystemExit) as test:
        main()
    assert test.type is SystemExit
    assert test.value.code == code
    captured = capsys.readouterr()
    assert captured.out == out


def test_pre_commit(capsys):
    sys.argv = ["ppc", "--pre-commit"]
    main()
    captured = capsys.readouterr()
    assert captured.out.startswith("repos:\n")
    assert (
        "repo: https://github.com/rcmdnk/pyproject-pre-commit" in captured.out
    )
    assert f"v{__version__}" in captured.out


def test_pyproject(capsys):
    sys.argv = ["ppc", "--pyproject"]
    main()
    captured = capsys.readouterr()
    assert captured.out.startswith("[tool.black]\n")
