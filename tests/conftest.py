import pytest
from dotenv import dotenv_values


@pytest.fixture
def api_token() -> str:
    env = dotenv_values(".env")
    token = env.get("TOKEN", "RandomTokenString")
    assert isinstance(token, str)
    return token
