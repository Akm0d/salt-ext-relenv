"""
Define the required entry-points functions in order for Salt to know
what and from where it should load this extension's loaders
"""
from . import PACKAGE_ROOT  # pylint: disable=unused-import


def get_module_dirs():
    """
    Return a list of paths from where salt should load module modules
    """
    return [str(PACKAGE_ROOT / "modules")]


def get_state_dirs():
    """
    Return a list of paths from where salt should load state modules
    """
    return [str(PACKAGE_ROOT / "states")]
