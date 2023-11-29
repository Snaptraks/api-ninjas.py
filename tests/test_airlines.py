import pytest
from pydantic import BaseModel

from api_ninjas.airlines import Airline, AirlinesAPI
from api_ninjas.base import BaseAPI
from api_ninjas.errors import MissingArgument


@pytest.fixture
def airlines_api(api_token: str) -> AirlinesAPI:
    return AirlinesAPI(api_token)


def test_inheritance():
    assert issubclass(Airline, BaseModel)
    assert issubclass(AirlinesAPI, BaseAPI)


def test_get(airlines_api: AirlinesAPI):
    airlines = airlines_api.get(name="Canada")
    assert isinstance(airlines, list)
    assert len(airlines) > 0
    assert isinstance(airlines[0], Airline)


def test_no_arguments(airlines_api: AirlinesAPI):
    with pytest.raises(MissingArgument):
        airlines_api.get()
