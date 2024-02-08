# Working with SeleniumWebAuthn

## Build & Development Requirements

To Be Defined


## Workflow

At the moment, none


### Generate and activate venv

Clone the repo and cd inside to it and execute following commands:

```bash
python3 -mvenv venv       # Generates the virtual env
source venv/bin/activate  # activates it!
```

### Install dependencies
All project dependencies are listed in root level requirements.txt
and requirements-dev.txt files. These can be used to download and
install into previously activated virtual env via:

```bash
python -m pip install -r requirements-dev.txt
```

This will install all development time dependencies but also runtime
dependencies from requirements.txt file.

## Architecture

WebAuthn uses Selenium 4's Virtual Authenticator implementation and its
implemented as plugin for SeleniumLibrary


## Building and Testing

```bash
inv check
inv test
```

### Pull Requests

Maybe not yet but ping me if you have something.

### Release

To Be Defined

## Coding Guideles

To Be Defined

