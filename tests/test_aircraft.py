import pytest
from pydantic import BaseModel

from api_ninjas.aircraft import Aircraft, AircraftAPI, EngineType
from api_ninjas.base import BaseAPI
from api_ninjas.errors import MissingArgument


@pytest.fixture
def aircraft_api(api_token: str) -> AircraftAPI:
    return AircraftAPI(api_token)


def test_inheritance():
    assert issubclass(Aircraft, BaseModel)
    assert issubclass(AircraftAPI, BaseAPI)


def test_get(aircraft_api: AircraftAPI):
    aircrafts = aircraft_api.get(manufacturer="Airbus")
    assert isinstance(aircrafts, list)
    assert len(aircrafts) > 0
    assert isinstance(aircrafts[0], Aircraft)
    assert isinstance(aircrafts[0].manufacturer, str)
    assert isinstance(aircrafts[0].length_ft, float)


def test_engine_type(aircraft_api: AircraftAPI):
    aircrafts = aircraft_api.get(engine_type=EngineType.PISTON)
    assert isinstance(aircrafts[0].engine_type, EngineType)


def test_get_many(aircraft_api: AircraftAPI):
    n = 2
    aircrafts = aircraft_api.get(n, manufacturer="Airbus")
    assert len(aircrafts) == n


def test_get_too_many(aircraft_api: AircraftAPI):
    with pytest.raises(ValueError):
        aircraft_api.get(31)


def test_get_not_enough(aircraft_api: AircraftAPI):
    with pytest.raises(ValueError):
        aircraft_api.get(0)


def test_no_arguments(aircraft_api: AircraftAPI):
    with pytest.raises(MissingArgument):
        aircraft_api.get()
