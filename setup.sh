#!/usr/bin/env bash

py_ver="3.10" # "3.10, 3.9, 3.8", need quotes for each version in the quote.
py_main=${py_ver%%,*}
os="ubuntu-latest" # "ubuntu-latest, macos-latest, windows-latest"
os_main=${os%%,*}
cli="no" # "yes" or "no"

user=$(git config --get user.name)
email=$(git config --get user.email)

year=$(date +%Y)
repo_url=$(git remote get-url origin)
repo_name=$(basename "$repo_url")
repo_user=$(basename "$(dirname "$repo_url)")")
repo_name_underscore=${repo_name//-/_}

py_max=0
py_min=100
py_vers=""
for p in ${py_ver//,/ };do
  if [ -n "$py_vers" ];then
    py_vers="${py_vers}, "
  fi
  py_vers="${py_vers}\"$p\""
  ver=${p#*.}
  if (( ver > py_max ));then
    py_max=$ver
  fi
  if (( ver < py_min ));then
    py_min=$ver
  fi
done


if [[ "$(sed --version 2>/dev/null)" == "GNU" ]];then
  function sedi {
    sed -i"" "$@"
  }
else
  function sedi {
    sed -i "" "$@"
  }
fi

cat << EOF > README.md
# $repo_name

[![test](https://github.com/$repo_user/$repo_name/actions/workflows/test.yml/badge.svg)](https://github.com/$repo_user/$repo_name/actions/workflows/test.yml)
[![test coverage](https://img.shields.io/badge/coverage-check%20here-blue.svg)](https://github.com/$repo_user/$repo_name/tree/coverage)

...

## Requirement

- Python ${py_vers//\"/}
- Poetry (For development)

## Installation

...

## Usage

...

## Development

### Poetry

Use [Poetry](https://python-poetry.org/) to setup environment.

To install poetry, run:

\`\`\`
$ pip install poetry
\`\`\`

or use \`pipx\` (\`x\` is \`3\` or anything of your python version).

Setup poetry environment:

\`\`\`
$ poetry install
\`\`\`

Then enter the environment:

\`\`\`
$ poetry shell
\`\`\`

## pre-commit

To check codes at the commit, use [pre-commit](https://pre-commit.com/).

\`pre-commit\` command will be installed in the poetry environment.

First, run:

\`\`\`
$ pre-commit install
\`\`\`

Then \`pre-commit\` will be run at the commit.

Sometimes, you may want to skip the check. In that case, run:

\`\`\`
$ git commit --no-verify
\`\`\`

You can run \`pre-commit\` on entire repository manually:

\`\`\`
$ pre-commit run -a
\`\`\`

### pytest

Tests are written with [pytest](https://docs.pytest.org/).

Write tests in **/tests** directory.

To run tests, run:

\`\`\`
$ pytest
\`\`\`

The default setting runs tests in parallel with \`-n auto\`.
If you run tests in serial, run:

\`\`\`
$ pytest -n 0
\`\`\`

## GitHub Actions

If you push a repository to GitHub, GitHub Actions will run a test job
by [GitHub Actions](https://github.co.jp/features/actions).

The job runs at the Pull Request, too.

It checks codes with \`pre-commit\` and runs tests with \`pytest\`.
It also makes a test coverage report and uploads it to [the coverage branch](https://github.com/$repo_user/$repo_name/tree/coverage).

You can see the test status as a badge in the README.

### Renovate

If you want to update dependencies automatically, [install Renovate into your repository](https://docs.renovatebot.com/getting-started/installing-onboarding/).
EOF

sedi "s/USER/$user/" pyproject.toml
sedi "s/EMAIL/$email/" pyproject.toml
sedi "s/python-template/$repo_name/" pyproject.toml
sedi "s/python_template/$repo_name_underscore/" pyproject.toml
sedi "s/python = \">=3.10,<3.11\"/python = \">=3.$py_min,<3.$((py_max+1))\"/" pyproject.toml

sedi "s/yyyy/$year/" LICENSE
sedi "s/name of copyright owner/@${user}/" LICENSE

mv "src/python_template" "src/$repo_name_underscore"
sedi "s/python_template/$repo_name_underscore/" tests/test_version.py

sedi "s/python-version: \[\"3.10\"\]/python-version: \[$py_vers\]/" .github/workflows/test.yml
sedi "s/test \"\${{ matrix.python-version }}\" == \"3.10\"/test \"\${{ matrix.python-version }}\" == \"$py_main\"/" .github/workflows/test.yml
sedi "s/os: \[ubuntu-latest\]/os: \[$os\]/" .github/workflows/test.yml
sedi "s/test \"\${{ matrix.os }}\" == \"ubuntu-latest\"/test \"\${{ matrix.os }}\" == \"$os_main\"/" .github/workflows/test.yml

if [ "$cli" = "yes" ];then
  cat << EOF >> pyproject.toml

[tool.poetry.scripts]
$repo_name = "$repo_name_underscore:main"
EOF
  cat << EOF > "src/$repo_name_underscore/${repo_name_underscore}.py"
import sys


def main() -> None:
    match len(sys.argv):
        case 1:
            print("Hello World!")
        case 2:
            print(f"Hello {sys.argv[1]}!")
        case _:
            print(f"Hello {', '.join(sys.argv[1:])}!")


if __name__ == "__main__":
    main()
EOF
  cat << EOF >> "src/$repo_name_underscore/__init__.py"
__program__ = "$repo_name"
from .${repo_name_underscore} import main

__all__ = ["main"]
EOF
  cat << EOF > "tests/test_${repo_name_underscore}.py"
import sys

import pytest

from $repo_name_underscore import main


@pytest.mark.parametrize(
    "argv, out",
    [
        (["$repo_name_underscore"], "Hello World!\n"),
        (["$repo_name_underscore", "Alice"], "Hello Alice!\n"),
        (
            ["$repo_name_underscore", "Alice", "Bob", "Carol"],
            "Hello Alice, Bob, Carol!\n",
        ),
    ],
)
def test_main(argv, out, capsys):
    sys.argv = argv
    main()
    captured = capsys.readouterr()
    assert captured.out == out
EOF
fi

rm -f setup.sh poetry.lock .github/workflows/template_test.yml .github/FUNDING.yml
