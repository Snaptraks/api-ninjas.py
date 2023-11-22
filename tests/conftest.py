from dotenv import dotenv_values
import pytest

import api_ninjas


def pytest_runtest_setup(item: pytest.Item):
    """Setup the token before each test, in case one of them changes it."""

    config = dotenv_values(".env")
    api_ninjas.set_token(config.get("TOKEN"))
