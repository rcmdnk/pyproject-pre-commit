import sys

from . import __version__


def pre_commit(is_ruff: bool) -> None:
    if is_ruff:
        print(  # noqa: T201
            f"""repos:
  - repo: https://github.com/rcmdnk/pyproject-pre-commit
    rev: v{__version__}
    hooks:
      - id: ruff-lint-diff
      - id: ruff-lint
      - id: ruff-format-diff
      - id: ruff-format
"""
        )
    else:
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
"""
        )
    print(  # noqa: T201
        """- id: mypy
      - id: numpydoc-validation
      - id: shellcheck
      - id: mdformat-check
      - id: mdformat
"""
    )


def pyproject(is_ruff: bool) -> None:
    if is_ruff:
        print(  # noqa: T201
            """[tool.ruff]
line-length = 79
# quote-style = "single"

[tool.ruff.lint]
## select = ["ALL"]
## select = ["E4", "E7", "E9", "F"]  # default, black compatible
select = [  # similar options to black, flake8 + plugins, isort etc...)
  #"E4",  # Import (comparable to black)
  #"E7",  # Indentation (comparable to black)
  #"E9",  # Blank line (comparable to black)
  "F",   # String (comparable to black)
  "I",   # Import order (comparable to isort)
  "S",   # flake8-bandit (comparable to bandit)
  "B",   # flake8-bugbear
  "A",   # flake8-builtins
  "C4",   # flake8-comprehensions
  "T10",  # flake8-debugger
  "EXE",  # flake8-executable
  "T20", # flake8-print
  "N", # pep8-naming
  "E", # pycodestyle
  "W", # pycodestyle
  "C90", # mccabe
]

ignore = [
 "E203", # Not PEP8 compliant and black insert space around slice: [Frequently Asked Questions - Black 22.12.0 documentation](https://black.readthedocs.io/en/stable/faq.html#why-are-flake8-s-e203-and-w503-violated)
 "E501", # Line too long. Disable it to allow long lines of comments and print lines which black allows.
# "E704", # NOT in ruff. multiple statements on one line (def). This is inconsistent with black >= 24.1.1 (see ttps://github.com/psf/black/pull/3796)
# "W503", # NOT in ruff. is the counter part of W504, which follows current PEP8: [Line break occurred before a binary operator (W503)](https://www.flake8rules.com/rules/W503.html)
 "D100", "D102", "D103", "D104", "D105", "D106", # Missing docstrings other than class (D101)
 "D401", # First line should be in imperative mood
]

[tool.ruff.lint.per-file-ignores]
"tests/**" = ["S101"]

[tool.ruff.lint.mccabe]
max-complexity = 10

[tool.ruff.format]
docstring-code-format = true
"""
        )
    else:
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
"""
        )
    print(  # noqa: T201
        """[tool.mypy]
files = "src/**/*.py"
strict = true
warn_return_any = false
ignore-missing-imports = true
scripts_are_modules = true
install_types = true
non_interactive = true

[tool.numpydoc_validation]
checks = [
    "all",   # report on all checks, except the below
    "EX01",  # "No examples section found"
    "ES01",  # "No extended summary found"
    "SA01",  # "See Also section not found"
    "GL08",  # "The object does not have a docstring"
    "PR01",  # "Parameters {missing_params} not documented"
    "PR02",  # "Unknown parameters {unknown_params}"
    "RT01",  # "No Returns section found"
]
"""
    )


def main() -> None:
    usage = "Usage: ppc <--pre-commit | --pyproject> [--ruff] [--black]"
    if len(sys.argv) < 2:
        print(usage)  # noqa: T201
        sys.exit(0)
    is_ruff = "--ruff" in sys.argv
    if "--pre-commit" in sys.argv:
        pre_commit(is_ruff)
    elif "--pyproject" in sys.argv:
        pyproject(is_ruff)
    else:
        print(usage)  # noqa: T201
        sys.exit(1)


if __name__ == "__main__":
    main()
