# SPDX-License-Identifier: ISC
#
# ISC License
#
# Copyright (c) 2024, Timothée Mazzucotelli and contributors
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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
