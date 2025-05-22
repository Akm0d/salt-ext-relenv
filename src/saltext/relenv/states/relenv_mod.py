"""
Salt state module
"""
import logging

log = logging.getLogger(__name__)

__virtualname__ = "relenv"

# TODO wrap pip.installed passing in the bin_env from relenv
# TODO put new relenvs in /opt/relenv/?
# TODO wrap virtualenv.managed?

def __virtual__():
    return __virtualname__


def exampled(name):
    """
    This example function should be replaced
    """
    ret = {"name": name, "changes": {}, "result": False, "comment": ""}
    value = __salt__["relenv.example_function"](name)
    if value == name:
        ret["result"] = True
        ret["comment"] = f"The 'relenv.example_function' returned: '{value}'"
    return ret
