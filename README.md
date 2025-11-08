# griffe-public-redundant-aliases

[![ci](https://github.com/mkdocstrings/griffe-public-redundant-aliases/workflows/ci/badge.svg)](https://github.com/mkdocstrings/griffe-public-redundant-aliases/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe-public-redundant-aliases/)
[![pypi version](https://img.shields.io/pypi/v/griffe-public-redundant-aliases.svg)](https://pypi.org/project/griffe-public-redundant-aliases/)
[![gitter](https://img.shields.io/badge/matrix-chat-4DB798.svg?style=flat)](https://app.gitter.im/#/room/#griffe-public-redundant-aliases:gitter.im)

Mark objects imported with redundant aliases as public.

## Installation

```bash
pip install griffe-public-redundant-aliases
```

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

## Sponsors

<!-- sponsors-start -->
<!-- sponsors-end -->
