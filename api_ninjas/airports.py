from pydantic import BaseModel

from .base import BaseAPI
from .errors import MissingArgument
from .utils import filter_none_values


class Airport(BaseModel):
    icao: str
    iata: str
    name: str
    city: str
    region: str
    country: str
    elevation_ft: float
    latitude: float
    longitude: float
    timezone: str


class AirportsAPI(BaseAPI):
    """
    The Airports API provides vital information on nearly 30,000 airports
    worldwide including major international airports and small regional airports.
    """

    endpoint = "/v1/airports"

    def get(
        self,
        icao: str | None = None,
        iata: str | None = None,
        name: str | None = None,
        country: str | None = None,
        region: str | None = None,
        city: str | None = None,
        timezone: str | None = None,
        min_elevation: float | None = None,
        max_elevation: float | None = None,
        offset: int | None = None,
    ) -> list[Airport]:
        """Return a list of up to 30 airport results.
        Use the offset parameter to access more results if available.

        At least one of the following arguments must be provided:

        Args:
            icao: International Civil Aviation Organization (ICAO) 4-character airport code.
            iata: International Air Transport Association (IATA) 3-character airport code.
            name: Airport name. This parameter supports partial matching (e.g. Heathrow will match London Heathrow Airport)
            country: Airport country. Must be 2-character ISO-2 country code (e.g. GB)
            region: Administrative region such as state or province within a country (e.g. California)
            city: Airport city (e.g. London)
            timezone: Airport timezone (e.g. Europe/London)
            min_elevation: Minimum airport elevation in feet.
            max_elevation: Maximum airport elevation in feet.
            offset: Number of results to offset for pagination.

        Returns:
            A list of Airport

        Raises:
            MissingArgument: If no arguments are passed
        """

        params = filter_none_values(
            dict(
                icao=icao,
                iata=iata,
                name=name,
                country=country,
                region=region,
                city=city,
                timezone=timezone,
                min_elevation=min_elevation,
                max_elevation=max_elevation,
                offset=offset,
            )
        )
        if len(params) == 0:
            raise MissingArgument("At least one argument must be passed.")

        resp = self.session.get(self.url, params=params)

        return [Airport(**item) for item in resp.json()]
