"""griffe-public-redundant-aliases package.

Mark objects imported with redundant aliases as public.
"""

from __future__ import annotations

from griffe_public_redundant_aliases._internals.extension import PublicRedundantAliasesExtension

__all__: list[str] = ["PublicRedundantAliasesExtension"]
