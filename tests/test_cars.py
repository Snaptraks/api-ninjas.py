import pytest
from pydantic import BaseModel

from api_ninjas.base import BaseAPI
from api_ninjas.cars import Car, CarsAPI
from api_ninjas.errors import MissingArgument


@pytest.fixture
def cars_api(api_token: str):
    return CarsAPI(api_token)


def test_inheritance():
    assert issubclass(Car, BaseModel)
    assert issubclass(CarsAPI, BaseAPI)


def test_get(cars_api: CarsAPI):
    cars = cars_api.get(model="corolla")
    print(cars)

    assert isinstance(cars, list)
    assert len(cars) > 0
    assert isinstance(cars[0], Car)


def test_no_arguments(cars_api: CarsAPI):
    with pytest.raises(MissingArgument):
        cars_api.get()
