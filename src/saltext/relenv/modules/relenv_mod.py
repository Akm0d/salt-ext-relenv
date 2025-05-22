"""
Salt execution module
"""
import logging

log = logging.getLogger(__name__)

__virtualname__ = "relenv"


def __virtual__():
    return __virtualname__


def example_function(text):
    """
    This example function should be replaced

    CLI Example:

    .. code-block:: bash

        salt '*' relenv.example_function text="foo bar"
    """
    return __salt__["test.echo"](text)
