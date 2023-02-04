from pathlib import Path

import tomli

from python_template import __version__


def test_version():
    with open(Path(__file__).parents[1] / "pyproject.toml", "rb") as f:
        version = tomli.load(f)["tool"]["poetry"]["version"]
    assert version == __version__
