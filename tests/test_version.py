from pathlib import Path

import tomli

from pyproject_pre_commit import __version__


def test_version():
    with open(Path(__file__).parents[1] / "pyproject.toml", "rb") as f:
        version = tomli.load(f)["tool"]["poetry"]["version"]
    assert version == __version__
