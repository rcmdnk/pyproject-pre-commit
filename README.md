# pyproject-pre-commit

[![test](https://github.com/rcmdnk/pyproject-pre-commit/actions/workflows/test.yml/badge.svg)](https://github.com/rcmdnk/pyproject-pre-commit/actions/workflows/test.yml)
[![test coverage](https://img.shields.io/badge/coverage-check%20here-blue.svg)](https://github.com/rcmdnk/pyproject-pre-commit/tree/coverage)

pre-commit hooks for python projects using pyproject.toml.

If you install this package, several linters/formatters will be installed, too.

**.pre-commit-hooks.yaml** provides pre-defined ids which you just need to add these ids to your **.pre-commit-config.yaml**.

## Requirement

- Python 3.11, 3.10, 3.9, 3.8, 3.7
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

## Usage

Add hooks to your **.pre-commit-config.yaml**.
Example configurations are provided by `ppc` command as below.

All options for these tools can be written in **pyproject.toml**.
Example options are provided by `ppc` command as below.

Then, use `pre-commit` as usual.

### Prepare configurations

#### pre-commit

Add pre-commit hooks to your **.pre-commit-config.yaml**.

If you don't have it, do:

```
$ ppc --pre-commit > .pre-commit-config.yaml
```

If you already have it, add hooks by

```
$ ppc --pre-commit |grep -v "^repos:" >> .pre-commit-config.yaml
```

You may want to modify after adding these configurations.

#### pyproject.toml

Add configurations for tools:

```
$ ppc --pyproject >> pyproject.toml
```

You may want to modify after adding these configurations.
