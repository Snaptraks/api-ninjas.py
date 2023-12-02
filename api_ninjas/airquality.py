from typing import Any

from pydantic import BaseModel, Field

from .base import BaseAPI
from .errors import MissingArgument, TooManyArguments
from .utils import filter_none_values


class Pollutant(BaseModel):
    concentration: float
    aqi: int


class AirQuality(BaseModel):
    overall_aqi: int
    CO: Pollutant
    PM10: Pollutant
    SO2: Pollutant
    PM2_5: Pollutant = Field(alias="PM2.5")
    O3: Pollutant
    NO2: Pollutant


class AirQualityAPI(BaseAPI):
    """
    The Air Quality API provides the latest air quality information for any
    city or geographic location in the world. It provides not only the wholistic
    Air Quality Index (AQI) but also concentrations for major pollutants:

    - Carbon monoxide (CO)
    - Nitrogen dioxide (NO2)
    - Ozone (O3)
    - Sulphur dioxide (SO2)
    - PM2.5 particulates
    - PM10 particulates
    """

    endpoint = "/v1/airquality"

    def get(
        self,
        *,
        lat: float | None = None,
        lon: float | None = None,
        city: str | None = None,
        state: str | None = None,
        country: str | None = None,
    ) -> AirQuality:
        """
        Get air quality by city or location coordinates (latitude/longitude).
        Return the air quality index (AQI) and concentrations of major pollutants.

        Either provide lat (required) and lon (required)
        OR
        city (required), state (optional), and country (optional)

        Args:
            lat: Latitude of desired location.
            lon: Longitude of desired location.
            city: City Name
            state: US state (for United States cities only).
            country: Country name.

        Returns:
            The AirQuality of the city or location.

        Raises:
            ...
        """
        using_lat_lon = (lat is not None) and (lon is not None)
        using_city = city is not None

        if using_lat_lon and using_city:
            raise TooManyArguments()

        if not (using_lat_lon or using_city):
            raise MissingArgument()

        params = filter_none_values(
            dict(
                lat=lat,
                lon=lon,
                city=city,
                state=state,
                country=country,
            )
        )

        if len(params) == 0:
            raise MissingArgument()

        resp = self.session.get(self.url, params=params)

        airquality_data: dict[str, Any] = resp.json()

        return AirQuality(**airquality_data)
