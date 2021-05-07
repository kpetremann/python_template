[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## What it includes

Set for python3.9

- Linters: pylint, mypy, pycodestyle, pydocstyle
- Code analysis: pytest, bandit
- Auto format: black, isort, unimport
- Build: tox, setuptools, pex
- Pretty stacktraces: pretty-errors

## Bootstrap

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/dev.txt
```

Or using invoke (you need invoke package to be installed on your system):
```bash
invoke install
```

Put your code in `app/`

> :warning: **NOTE**: If you add or rename the packages at root level (app/), you need to update the following files:
> - tox.ini
> - setup.py

## Run your app

Run the start script:
```bash
python start.py
```

Install the PEX in your environment, and run it:
```bash
pip install -e .  # To do only once
run-app
```

Run from invoke:
```bash
invoke start
```

## Autoformat script

The template configuration includes: black, isort and unimport.

They can all be executed in the righ order thanks to tox:
```bash
tox -e format
```

It can also be triggered with invoke:
```bash
invoke reformat
```

## Lint and build

Simply use `tox`:

```bash
tox  # check your code
tox -e bundle  # build the python PEX in dist/
```
