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

"""Test the extension."""

import griffe


def test_objects_imported_within_same_package() -> None:
    """Objects imported with redundant aliases as marked as public."""
    with griffe.temporary_visited_package(
        "package",
        {
            "__init__.py": "from package.module import Thing as Thing, Stuff",
            "module.py": "class Thing: ...\nclass Stuff: ...",
        },
        extensions=griffe.load_extensions("griffe_public_redundant_aliases"),
    ) as package:
        assert package["Thing"].public
        assert package["Thing"].is_public
        assert package["Stuff"].public is None
        assert not package["Stuff"].is_public


def test_objects_imported_from_external_package() -> None:
    """Objects imported with redundant aliases as marked as public."""
    with griffe.temporary_visited_module(
        "from external import Thing as Thing, Stuff",
        extensions=griffe.load_extensions("griffe_public_redundant_aliases"),
    ) as package:
        assert package["Thing"].public
        assert package["Thing"].is_public
        assert package["Stuff"].public is None
        assert not package["Stuff"].is_public


def test_not_stoping_too_early() -> None:
    """Don't stop too early on several aliases of the same object."""
    with griffe.temporary_visited_module(
        "from external import Thing as Stuff, Thing as Thing",
        extensions=griffe.load_extensions("griffe_public_redundant_aliases"),
    ) as package:
        assert package["Thing"].public
        assert package["Thing"].is_public
        assert package["Stuff"].public is None
        assert not package["Stuff"].is_public
