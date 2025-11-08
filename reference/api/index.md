# griffe_public_redundant_aliases

griffe-public-redundant-aliases package.

Mark objects imported with redundant aliases as public.

Classes:

- **`PublicRedundantAliasesExtension`** – Mark objects imported with redundant aliases as public.

## PublicRedundantAliasesExtension

Bases: `Extension`

Mark objects imported with redundant aliases as public.

Methods:

- **`on_alias_instance`** – Mark alias as public if it corresponds to an import with a redundant alias.

### on_alias_instance

```
on_alias_instance(
    *, node: AST | ObjectNode, alias: Alias, **kwargs: Any
) -> None
```

Mark alias as public if it corresponds to an import with a redundant alias.

Source code in `src/griffe_public_redundant_aliases/_internal/extension.py`

```
def on_alias_instance(self, *, node: ast.AST | griffe.ObjectNode, alias: griffe.Alias, **kwargs: Any) -> None:  # noqa: ARG002
    """Mark alias as public if it corresponds to an import with a redundant alias."""
    # Only static analysis and import nodes are supported.
    if isinstance(node, ast.AST) and isinstance(node, (ast.Import, ast.ImportFrom)):
        # Search import corresponding to alias.
        for name in node.names:
            if name.name == alias.name and name.name == name.asname:
                # Found import corresponding to alias,
                # and import uses a redundant alias.
                alias.public = True
                return
```
