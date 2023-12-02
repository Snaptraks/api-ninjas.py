import pytest
from pydantic import BaseModel

from api_ninjas.airquality import AirQuality, AirQualityAPI, Pollutant
from api_ninjas.base import BaseAPI
from api_ninjas.errors import MissingArgument, TooManyArguments


@pytest.fixture
def airquality_api(api_token: str) -> AirQualityAPI:
    return AirQualityAPI(api_token)


def test_inheritance():
    assert issubclass(AirQuality, BaseModel)
    assert issubclass(AirQualityAPI, BaseAPI)


def test_get_lat_lon(airquality_api: AirQualityAPI):
    airquality = airquality_api.get(lat=12.345, lon=123.456)
    assert isinstance(airquality, AirQuality)
    assert airquality.overall_aqi
    assert isinstance(airquality.CO, Pollutant)


def test_get_city(airquality_api: AirQualityAPI):
    airquality = airquality_api.get(city="Tokyo")
    assert isinstance(airquality, AirQuality)
    assert airquality.overall_aqi
    assert isinstance(airquality.CO, Pollutant)


def test_missing_arguments(airquality_api: AirQualityAPI):
    with pytest.raises(MissingArgument):
        airquality_api.get(lon=12.345)


def test_no_arguments(airquality_api: AirQualityAPI):
    with pytest.raises(MissingArgument):
        airquality_api.get()


def test_too_many_arguments(airquality_api: AirQualityAPI):
    with pytest.raises(TooManyArguments):
        airquality_api.get(lat=12.345, lon=123.456, city="Paris")
