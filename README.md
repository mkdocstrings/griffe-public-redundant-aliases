# griffe-public-redundant-aliases

[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe-public-redundant-aliases/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-708FCC.svg?style=flat)](https://gitpod.io/#https://github.com/mkdocstrings/griffe-public-redundant-aliases)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#griffe-public-redundant-aliases:gitter.im)

Mark objects imported with redundant aliases as public.

## Installation

This project is available to sponsors only, through my Insiders program.
See Insiders [explanation](https://mkdocstrings.github.io/griffe-public-redundant-aliases/insiders/)
and [installation instructions](https://mkdocstrings.github.io/griffe-public-redundant-aliases/insiders/installation/).

## Usage

[Enable](https://mkdocstrings.github.io/griffe/guide/users/extending/#using-extensions) the `griffe_public_redundant_aliases` extension. Now all objects imported with redundant aliases will be marked as public, as per the convention.

```python
# Following objects will be marked as public.
from somewhere import Thing as Thing
from somewhere import Other as Other

# Following object won't be marked as public.
from somewhere import Stuff
```

With MkDocs:

```yaml
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_public_redundant_aliases
```
