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
