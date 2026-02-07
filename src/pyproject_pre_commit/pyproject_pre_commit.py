import sys

from . import __version__


def pre_commit(is_black: bool, is_mypy: bool) -> None:
    if is_black:
        print(f"""repos:
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
      - id: bandit""")  # noqa: T201
    else:
        print(f"""repos:
  - repo: https://github.com/rcmdnk/pyproject-pre-commit
    rev: v{__version__}
    hooks:
      - id: ruff-lint-diff
      - id: ruff-lint
      - id: ruff-format-diff
      - id: ruff-format""")  # noqa: T201
    if is_mypy:
        print("""      - id: mypy""")  # noqa: T201
    else:
        print("""      - id: ty""")  # noqa: T201
    print("""      - id: numpydoc-validation
      - id: shellcheck
      - id: mdformat-check
      - id: mdformat""")  # noqa: T201


def pyproject(is_black: bool, is_mypy: bool) -> None:
    if is_black:
        print("""[tool.black]
line-length = 79

[tool.autoflake]
remove-all-unused-imports = true
expand-star-imports = true
remove-duplicate-keys = true
remove-unused-variables = true

[tool.autopep8]
ignore = "E203,E501,W503"
recursive = true
aggressive = 3

[tool.isort]
profile = "black"
line_length = 79

[tool.flake8]
# E203 is not PEP8 compliant and black insert space around slice: [Frequently Asked Questions - Black 22.12.0 documentation](https://black.readthedocs.io/en/stable/faq.html#why-are-flake8-s-e203-and-w503-violated)
# E501: Line too long. Disable it to allow long lines of comments and print lines which black allows.
# E704: multiple statements on one line (def). This is inconsistent with black >= 24.1.1 (see ttps://github.com/psf/black/pull/3796)
# W503 is the counter part of W504, which follows current PEP8: [Line break occurred before a binary operator (W503)](https://www.flake8rules.com/rules/W503.html)
# D100~D106: Missing docstrings other than class (D101)
# D401: First line should be in imperative mood
ignore = "E203,E501,E704,W503,D100,D102,D103,D104,D105,D106,D401"
max-complexity = 10
docstring-convention = "numpy"

[tool.bandit]
exclude_dirs = ["tests"]
""")  # noqa: T201
    else:
        print("""[tool.ruff]
line-length = 79

[tool.ruff.lint]
select = ["ALL"]

ignore = [
    "E203", # Not PEP8 compliant and black insert space around slice: [Frequently Asked Questions - Black 22.12.0 documentation](https://black.readthedocs.io/en/stable/faq.html#why-are-flake8-s-e203-and-w503-violated)
    "E501", # Line too long. Disable it to allow long lines of comments and print lines which black allows.
    "D100", "D102", "D103", "D104", "D105", "D106", # Missing docstrings other than class (D101)
    "D401", # First line should be in imperative mood
    "D211", # `one-blank-line-before-class` (D203) and `no-blank-line-before-class` (D211) are incompatible. Ignoring `one-blank-line-before-class`.
    "D213", # `multi-line-summary-first-line` (D212) and `multi-line-summary-second-line` (D213) are incompatible. Ignoring `multi-line-summary-second-line`.
    "COM812", "D203", "ISC001", # The following rules may cause conflicts when used with the formatter: `COM812`, `D203`, `ISC001`. To avoid unexpected behavior, we recommend disabling these rules, either by removing them from the `select` or `extend-select` configuration, or adding them to the `ignore` configuration.
    "FBT001", # Boolean-typed positional argument in function definition
    "FBT002", # Boolean default positional argument in function definition
    "FBT003", # Boolean positional value in function call
    "TID252", # Prefer absolute imports over relative imports from parent modules
    "PLC0415", # `import` should be at the top-level of a file
    "PLR2004", # Magic value used in comparison
]

[tool.ruff.lint.per-file-ignores]
"tests/**" = [
  "S101", # Use of `assert` detected
  "PLR0913", # Too many arguments in function definition
]

[tool.ruff.lint.mccabe]
max-complexity = 10

[tool.ruff.format]
quote-style = "single"
docstring-code-format = true
""")  # noqa: T201
    if is_mypy:
        print("""[tool.mypy]
files = ["src/**/*.py"]
strict = true
warn_return_any = false
ignore_missing_imports = true
scripts_are_modules = true
install_types = true
non_interactive = true
""")  # noqa: T201
    else:
        print("""[tool.ty.tules]

""")  # noqa: T201

    print("""[tool.numpydoc_validation]
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
""")  # noqa: T201


def main() -> None:
    usage = 'Usage: ppc <pre-commit | pyproject> [--black] [--mypy]'
    if len(sys.argv) < 2:
        print(usage)  # noqa: T201
        sys.exit(0)
    is_black = '--black' in sys.argv
    is_mypy = '--mypy' in sys.argv
    if 'pre-commit' in sys.argv:
        pre_commit(is_black, is_mypy)
    elif 'pyproject' in sys.argv:
        pyproject(is_black, is_mypy)
    else:
        print(usage)  # noqa: T201
        sys.exit(1)


if __name__ == '__main__':
    main()
