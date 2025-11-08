from __future__ import annotations

import ast
from typing import Any

import griffe


class PublicRedundantAliasesExtension(griffe.Extension):
    """Mark objects imported with redundant aliases as public."""

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
