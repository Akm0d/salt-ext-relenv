import pytest
import salt.modules.test as testmod
import saltext.relenv.modules.relenv_mod as relenv_module
import saltext.relenv.states.relenv_mod as relenv_state


@pytest.fixture
def configure_loader_modules():
    return {
        relenv_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        relenv_state: {
            "__salt__": {
                "relenv.example_function": relenv_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'relenv.example_function' returned: '{echo_str}'",
    }
    assert relenv_state.exampled(echo_str) == expected
