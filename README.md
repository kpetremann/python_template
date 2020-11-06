## What it includes

Set for python3.8

- Linters: pylint, mypy, pycodestyle, pydocstyle
- Code analysis: pytest, bandit
- Auto format: black, isort, unimport
- Build: tox, setuptools, pex

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
> - autoformat.sh
> - check_grammar.sh

## Autoformat script

The template configuration includes: black, isort and unimport.

They can all be executed in the righ order thanks to this script:
```bash
bash autoformat.sh
```

## Lint and build

Simply use `tox`:

```bash
tox  # check your code
tox -e bundle  # build the python PEX in dist/
```
