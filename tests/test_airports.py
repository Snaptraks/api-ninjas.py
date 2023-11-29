import pytest
from pydantic import BaseModel

from api_ninjas.airports import Airport, AirportsAPI
from api_ninjas.base import BaseAPI
from api_ninjas.errors import MissingArgument


@pytest.fixture
def airports_api(api_token: str) -> AirportsAPI:
    return AirportsAPI(api_token)


def test_inheritance():
    assert issubclass(Airport, BaseModel)
    assert issubclass(AirportsAPI, BaseAPI)


def test_get(airports_api: AirportsAPI):
    airports = airports_api.get(country="CA")
    assert isinstance(airports, list)
    assert len(airports) > 0
    assert isinstance(airports[0], Airport)


def test_no_arguments(airports_api: AirportsAPI):
    with pytest.raises(MissingArgument):
        airports_api.get()
