# griffe-public-redundant-aliases

Mark objects imported with redundant aliases as public.

## Installation

```
pip install griffe-public-redundant-aliases
```

## Usage

[Enable](https://mkdocstrings.github.io/griffe/guide/users/extending/#using-extensions) the `griffe_public_redundant_aliases` extension. Now all objects imported with redundant aliases will be marked as public, as per the convention.

```
# Following objects will be marked as public.
from somewhere import Thing as Thing
from somewhere import Other as Other

# Following object won't be marked as public.
from somewhere import Stuff
```

With MkDocs:

```
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_public_redundant_aliases
```

## Sponsors
