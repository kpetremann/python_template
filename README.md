## What it includes

Set for python3.8

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

Put your code in `app/`

> :warning: **NOTE**: If you add or rename the packages at root level (app/), you need to update the following files:
> - tox.ini
> - setup.py

## Run your app

Two possibilies:

Run the start script:
```bash
python start.py
```

Install the PEX in your environment, and run it:
```bash
pip install -e .  # To do only once
run-app
```

## Autoformat script

The template configuration includes: black, isort and unimport.

They can all be executed in the righ order thanks to tox:
```bash
tox -e format
```

## Lint and build

Simply use `tox`:

```bash
tox  # check your code
tox -e bundle  # build the python PEX in dist/
```
