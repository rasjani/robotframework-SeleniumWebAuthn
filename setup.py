# -*- coding: utf-8 -*-
"""
SeleniumWebAuthn
"""
from pathlib import Path
from setuptools import setup

LIBRARY_NAME = "SeleniumWebAuthn"
CWD = Path(__file__).parent

requirements_file = CWD / "requirements.txt"
readme_file = CWD / "README.md"

# Get requirements
with requirements_file.open(encoding="utf-8") as f:
    REQUIREMENTS = f.read().splitlines()

# Get the long description from the README file
with readme_file.open(encoding="utf-8") as f:
    long_description = f.read()

CLASSIFIERS = """
Development Status :: 3 - Alpha
Topic :: Software Development :: Testing
Operating System :: OS Independent
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3.12
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
""".strip().splitlines()

setup(
    name="robotframework-%s" % LIBRARY_NAME.lower(),
    version="0.0.1",
    description="SeleniumWebauthn plugin that provides Webauthn support and keywords for SeleniumLibrary.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rasjani/robotframework-%s" % LIBRARY_NAME.lower(),
    author="Jani Mikkonen",
    author_email="jani.mikkonen@gmail.com",
    license="Apache License 2.0",
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    keywords="robotframework testing automation selenium seleniumlibrary webauthn",
    platforms="any",
    packages=[LIBRARY_NAME],
    package_dir={"": "src"},
)
