import pytest
from pydantic import BaseModel

from api_ninjas.aircraft import Aircraft, AircraftAPI, EngineType
from api_ninjas.base import BaseAPI
from api_ninjas.errors import MissingArgument


def test_inheritance():
    assert issubclass(Aircraft, BaseModel)
    assert issubclass(AircraftAPI, BaseAPI)


def test_get():
    aircrafts = AircraftAPI.get(manufacturer="Airbus")
    assert isinstance(aircrafts, list)
    assert len(aircrafts) > 0
    assert isinstance(aircrafts[0], Aircraft)
    assert isinstance(aircrafts[0].manufacturer, str)
    assert isinstance(aircrafts[0].length_ft, float)


def test_engine_type():
    aircrafts = AircraftAPI.get(engine_type=EngineType.PISTON)
    assert isinstance(aircrafts[0].engine_type, EngineType)


def test_get_many():
    n = 2
    aircrafts = AircraftAPI.get(n, manufacturer="Airbus")
    assert len(aircrafts) == n


def test_get_too_many():
    with pytest.raises(ValueError):
        AircraftAPI.get(31)


def test_get_not_enough():
    with pytest.raises(ValueError):
        AircraftAPI.get(0)


def test_no_arguments():
    with pytest.raises(MissingArgument):
        AircraftAPI.get()
