# pyproject-pre-commit

[![test](https://github.com/rcmdnk/pyproject-pre-commit/actions/workflows/test.yml/badge.svg)](https://github.com/rcmdnk/pyproject-pre-commit/actions/workflows/test.yml)
[![test coverage](https://img.shields.io/badge/coverage-check%20here-blue.svg)](https://github.com/rcmdnk/pyproject-pre-commit/tree/coverage)

pre-commit hooks for python projects using pyproject.toml.

**.pre-commit-hooks.yaml** provides pre-defined ids which you just need to add these ids to your **.pre-commit-config.yaml**.

## Requirement

- Python 3.11, 3.10, 3.9, 3.8
- Poetry (For development)

## Installation

If your project uses poetry, do:

```
$ poetry add --group dev pyproject-pre-commit
```

Otherwise, install by pip:

```
$ pip install pyproject-pre-commit
```

## The repository features

If you install this package, several linters/formatters will be installed, too.

This repository has following hooks for [pre-commit](https://pre-commit.com/):

- For Python
  - black-diff: Just show Black result.
  - [black](https://black.readthedocs.io/en/stable): Black: The uncompromising Python code formatter.
  - [blacken-docs](https://github.com/adamchainz/blacken-docs): Run `black` on python code blocks in documentation files.
  - autoflake-diff: Just show autoflake result.
  - [autoflake](https://github.com/PyCQA/autoflake): autoflake removes unused imports and unused variables from Python code.
  - autopep8-diff: Just show autopep8.
  - [autopep8](https://github.com/hhatto/autopep8): autopep8 automatically formats Python code to conform to the PEP 8 style guide.
  - isort-diff: Just show isort result.
  - [isort](https://github.com/PyCQA/isort): isort your imports, so you don't have to.
  - [flake8](https://github.com/PyCQA/flake8): `flake8` is a command-line utility for enforcing style consistency across Python projects.
    - With following plugins:
      - [flake8-pyproject](https://github.com/csachs/pyproject-flake8)
      - [flake8-annotations-complexity](https://github.com/best-doctor/flake8-annotations-complexity)
      - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
      - [flake8-builtins](https://github.com/gforcada/flake8-builtins)
      - [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
      - [flake8-debugger](https://github.com/jbkahn/flake8-debugger)
      - [flake8-docstrings](https://github.com/pycqa/flake8-docstrings)
      - [flake8-executable](https://github.com/xuhdev/flake8-executable)
      - [flake8-pep3101](https://github.com/gforcada/flake8-pep3101)
      - [flake8-print](https://github.com/jbkahn/flake8-print)
      - [flake8-rst-docstrings](https://github.com/peterjc/flake8-rst-docstrings)
      - [flake8-string-format](https://github.com/xZise/flake8-string-format)
      - [pep8-naming](https://github.com/PyCQA/pep8-naming)
      - [pycodestyle](https://pycodestyle.pycqa.org/en/latest/)
  - [bandit](https://github.com/PyCQA/bandit): Bandit is a tool for finding common security issues in Python code.
  - [mypy](https://www.mypy-lang.org/): Mypy is a static type checker for Python.
- For Shell script
  - [shellcheck](https://www.shellcheck.net/): ShellCheck - A shell script static analysis tool
- For Markdown
  - mdformat-check: Just show mdformat result.
  - [mdformat](https://mdformat.readthedocs.io/en/stable/): CommonMark compliant Markdown formatter.
    - with following plugins:
      - [mdformat-gfm](https://github.com/hukkin/mdformat-gfm)
      - [mdformat-frontmatter](https://github.com/butler54/mdformat-frontmatter)
      - [mdformat-footnote](https://github.com/executablebooks/mdformat-footnote)

All tools are installed as dependencies of this package.

shellcheck and mdformat are given in addition to python tools
as they can be managed by pip and most projects have README.md
and some have shell scripts.

For tools which can format files, there are additional ids ids with `-diff` or `--check`
which just show the results and not modify files.
You can see the difference after formatting if you place these ids before ids w/o `--diff` or `--check`.

You can set options in pyproject.toml for all tools above:

- flake8: flake8-pyproject allows to read options from pyproject.toml
- bandit: There is a plugin for the flake8, but plugin version does not read options from pyproject.toml even with pyproject.toml. Therefore, use bandit directly and give `-c pyproject.toml` option in the hooks.

## .pre-commit-config.yaml

Prepare **.pre-commit-config.yaml** like:

```yaml
repos:
- repo: https://github.com/rcmdnk/pyproject-pre-commit
  rev: v0.0.1
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
  - id: shellcheck
  - id: mdformat-check
  - id: mdformat
```

This can be made by `ppc` command:

```
$ ppc --pre-commit > .pre-commit-config.yaml
```

If you already have it, add hooks w/o `repos:` by

```
$ ppc --pre-commit |grep -v "^repos:" >> .pre-commit-config.yaml
```

You may want to modify after adding these configurations.

## pyproject.toml

You can set options in pyproject.toml for all tools.

Example options can be made by `ppc` command:

```
$ ppc --pyproject >> pyproject.toml
```

You may want to modify after adding these configurations.
