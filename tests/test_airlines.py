import pytest
from pydantic import BaseModel

from api_ninjas.airlines import Airline, AirlinesAPI
from api_ninjas.base import BaseAPI
from api_ninjas.errors import MissingArgument


def test_inheritance():
    assert issubclass(Airline, BaseModel)
    assert issubclass(AirlinesAPI, BaseAPI)


def test_get():
    airlines = AirlinesAPI.get(name="Canada")
    assert isinstance(airlines, list)
    assert len(airlines) > 0
    assert isinstance(airlines[0], Airline)


def test_no_arguments():
    with pytest.raises(MissingArgument):
        AirlinesAPI.get()
