from pathlib import Path

from pyproject_pre_commit import __version__


def test_version() -> None:
    try:
        import tomllib
    except ModuleNotFoundError:
        import tomli as tomllib
    with (Path(__file__).parents[1] / "pyproject.toml").open("rb") as f:
        version = tomllib.load(f)["project"]["version"]
    assert version == __version__
