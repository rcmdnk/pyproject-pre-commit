import sys

from . import __version__


def pre_commit() -> None:
    print(  # noqa: T201
        f"""repos:
  - repo: https://github.com/rcmdnk/pyproject-pre-commit
    rev: v{__version__}
    hooks:
      - id: black-diff
      - id: black
      - id: blacken-docs
      - id: autoflake-diff
      - id: autoflake
      - id: autopep8-diff
      - id: autopep8
      - id: isort-diff
      - id: isort
      - id: flake8
      - id: bandit
      - id: mypy
      - id: numpydoc-validation
      - id: shellcheck
      - id: mdformat-check
      - id: mdformat
"""
    )


def pyproject() -> None:
    print(  # noqa: T201
        """[tool.black]
line-length = 79

[tool.autoflake]
remove-all-unused-imports = true
expand-star-imports = true
remove-unused-variables = true
remove-duplicate-keys = true

[tool.autopep8]
ignore = "E203,E501,W503"
recursive = true
aggresive = 3

[tool.isort]
profile = "black"
line-length = 79

[tool.flake8]
ignore = "E203,E501,W503,D100,D102,D103,D104,D105,D106,D401"
max-line-length = 79
max-complexity = 10
docstring-convention = "numpy"

[tool.bandit]
targets = "."
exclude = "tests"

[tool.mypy]
files = "src/**/*.py"
strict = true
warn_return_any = false
ignore-missing-imports = true
scripts_are_modules = true
install_types = true
non_interactive = true
"""
    )


def main() -> None:
    if len(sys.argv) != 2:
        print(  # noqa: T201
            "Please specify only one of --pre-commit and --pyproject."
        )
        sys.exit(1)
    if sys.argv[1] == "--pre-commit":
        pre_commit()
    elif sys.argv[1] == "--pyproject":
        pyproject()
    else:
        print(  # noqa: T201
            "Please specify only one of --pre-commit and --pyproject."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
