"""Some tasks."""
import os

from invoke import task  # type: ignore

PATH = os.path.dirname(os.path.realpath(__file__))


@task
def install(cmd):
    """Install virtualenv."""
    cmd.run(f"python -m venv {PATH}/.venv")
    with cmd.prefix(f"source {PATH}/.venv/bin/activate"):
        cmd.run(f"pip install -r {PATH}/requirements/dev.txt")


@task
def reformat(cmd):
    """Auto format using black and isort."""
    with cmd.prefix(f"source {PATH}/.venv/bin/activate"):
        cmd.run(f"unimport --gitignore -p --exclude '__init__.py' {PATH}/")
        cmd.run(f"isort {PATH}/")
        cmd.run(f"black {PATH}/")


@task
def start(cmd):
    """Start the app."""
    with cmd.prefix(f"source {PATH}/.venv/bin/activate"):
        cmd.run(f"python {PATH}/start.py", pty=True)
