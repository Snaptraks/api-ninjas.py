from pydantic import BaseModel

from .base import BaseAPI
from .errors import MissingArgument
from .utils import filter_none_values


class Airline(BaseModel):
    iata: str
    icao: str
    fleet: dict[str, int]
    logo_url: str | None = None
    name: str


class AirlinesAPI(BaseAPI):
    """
    The Airlines API provides general and detailed fleet information for over
    1,000 airlines from small, regional service providers to publicly-traded
    international carriers.
    """

    endpoint = "/v1/airlines"

    def get(
        self,
        *,
        icao: str | None = None,
        iata: str | None = None,
        name: str | None = None,
    ) -> list[Airline]:
        """Return a list of up to 10 airline results.

        At least one of the following arguments must be provided:

        Args:
            icao: International Civil Aviation Organization (ICAO) 3-character airline code.
            iata: International Air Transport Association (IATA) 2-character airline code.
            name: Airline name. This parameter supports partial matching
                (e.g. United will match United Airlines).

        Returns:
            A list of Airline.

        Raises:
            MissingArgument: If no arguments are passed.
        """

        params = filter_none_values(
            dict(
                icao=icao,
                iata=iata,
                name=name,
            )
        )

        if len(params) == 0:
            raise MissingArgument()

        resp = self.session.get(self.url, params=params)

        return [Airline(**item) for item in resp.json()]
