#!/usr/bin/env python3
"""Configure all the PEX."""

import os

import setuptools  # type: ignore


def _read_reqs(relpath):
    fullpath = os.path.join(os.path.dirname(__file__), relpath)
    with open(fullpath) as open_file:
        return [s.strip() for s in open_file.readlines() if (s.strip() and not s.startswith("#"))]


_INSTALL_REQUIRES = []
_REQUIREMENTS_FILES = ["requirements/base.txt"]

for req in _REQUIREMENTS_FILES:
    _REQUIREMENTS_TXT = _read_reqs(req)
    _INSTALL_REQUIRES.extend([line for line in _REQUIREMENTS_TXT])

setuptools.setup(
    name="app",
    version="0.1",
    include_package_data=True,
    install_requires=_INSTALL_REQUIRES,
    tests_require=_read_reqs("requirements/tests.txt"),
    dependency_links=[],
    entry_points={"console_scripts": ["app = app.main:main"]},
    packages=setuptools.find_packages(),
)
