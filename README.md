# pyproject-pre-commit

[![test](https://github.com/rcmdnk/pyproject-pre-commit/actions/workflows/test.yml/badge.svg)](https://github.com/rcmdnk/pyproject-pre-commit/actions/workflows/test.yml)
[![test coverage](https://img.shields.io/badge/coverage-check%20here-blue.svg)](https://github.com/rcmdnk/pyproject-pre-commit/tree/coverage)

[pre-commit](https://pre-commit.com/) hooks for python projects.

**.pre-commit-hooks.yaml** provides pre-defined ids which you just need to add these ids to your **.pre-commit-config.yaml**.

By installing **pyproject-pre-commit** package,
all necessary tools are installed as dependencies.

## Requirement

- Python >= 3.8.1
- Poetry (For development)

## Usage

### Install pyproject-pre-commit

If your project uses poetry, do:

```
$ poetry add --group dev pyproject-pre-commit
```

Otherwise, install the package in your working environment.

If you use pip, do:

```
$ pip install pyproject-pre-commit
```

This will install tools for pre-commit hooks in your working environment,
so that you can use these tools, such as black, directly.

### Prepare .pre-commit-config.yaml

Add **https://github.com/rcmdnk/pyproject-pre-commit** to your **.pre-commit-config.yaml**, like:

```yaml
repos:
- repo: https://github.com/rcmdnk/pyproject-pre-commit
  rev: v0.1.1
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

By using **pyproject-pre-commit**, you can simplify your **.pre-commit-config.yaml**
that you need only repo of **https://github.com/rcmdnk/pyproject-pre-commit**.

These hooks uses local installation of tools, so pre-commit will use
tools installed in your working environment.

This can be made by `ppc` command:

```
$ ppc --pre-commit > .pre-commit-config.yaml
```

> \[!NOTE\]
> If you are using poetry, run `poetry run ppc ... ` or run after `poetry shell`.

If you already have it, add hooks w/o `repos:` by

```
$ ppc --pre-commit |grep -v "^repos:" >> .pre-commit-config.yaml
```

You may want to modify after adding these configurations.

### Run pre-commit

`pre-commit` command is installed as dependencies of **pyproject-pre-commit** package.

After installing **pyproject-pre-commit** package, you can run `pre-commit` command.

First, install pre-commit hooks by:

```
$ pre-commit install
```

then you can run pre-commit by:

```
$ pre-commit run --all-files
```

> \[!NOTE\]
> If you are using poetry, run `poetry run pre-commit ... ` or run after `poetry shell`.

## Available ids

You can find ids in **.pre-commit-hooks.yaml**.

There are ids for following tools:

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

All tools are installed as dependencies of **pyproject-pre-commit** package.

shellcheck and mdformat are given in addition to python tools
as they can be managed by pip and most projects have README.md
and some have shell scripts.

For tools which can format files, there are additional ids with `-diff` or `--check`
which show the results before modifying files.
You can see the differences after formatting if you place these ids before ids w/o `--diff` or `--check`.

## Options for tools

You can set options in pyproject.toml for all tools above.

For flake8, flake8-pyproject allows to read options from pyproject.toml

About bandit, there is a plugin for the flake8, but plugin version does not read options from pyproject.toml even with pyproject.toml. Therefore, use bandit directly and give `-c pyproject.toml` option in the hooks.

## pyproject.toml

You can set options in pyproject.toml for all tools.

Example options can be made by `ppc` command:

```
$ ppc --pyproject >> pyproject.toml
```

You may want to modify after adding these configurations.
