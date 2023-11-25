from enum import StrEnum

from pydantic import BaseModel

from .base import BASE_URL, BaseAPI
from .errors import MissingArgument
from .http import HTTP
from .utils import filter_none_values


class EngineType(StrEnum):
    PISTON = "Piston"
    PROPJET = "Propjet"
    JET = "Jet"


class Aircraft(BaseModel):
    manufacturer: str
    model: str
    engine_type: EngineType
    engine_thrust_lb_ft: float | None = None
    max_speed_knots: float | None = None
    cruise_speed_knots: float | None = None
    ceiling_ft: float | None = None
    takeoff_ground_run_ft: float | None = None
    landing_ground_roll_ft: float | None = None
    gross_weight_lbs: float | None = None
    empty_weight_lbs: float | None = None
    length_ft: float | None = None
    height_ft: float | None = None
    wing_span_ft: float | None = None
    range_nautical_miles: float | None = None


class AircraftAPI(BaseAPI):
    """
    The Aircraft API provides detailed technical specs on over 1,000
    airplane models from propeller planes to jumbo jets.
    """

    endpoint = "/v1/aircraft"

    @classmethod
    def get(
        cls,
        limit: int = 1,
        *,
        manufacturer: str | None = None,
        model: str | None = None,
        engine_type: EngineType | None = None,
        min_speed: float | None = None,
        max_speed: float | None = None,
        min_range: float | None = None,
        max_range: float | None = None,
        min_length: float | None = None,
        max_length: float | None = None,
        min_height: float | None = None,
        max_height: float | None = None,
        min_wingspan: float | None = None,
        max_wingspan: float | None = None,
    ) -> list[Aircraft]:
        """Return a list of aircrafts that match the given parameters.
        This API only supports airplanes - for helicopter specs please use our
        Helicopter API.

        At least one of the following arguments (excluding the limit argument)
        must be set.

        Args:
            manufacturer: Company that designed and built the aircraft.
            model: Aircraft model name.
            engine_type: Type of engine. Must be one of: piston, propjet, jet.
            min_speed: Minimum max. air speed in knots.
            max_speed: Maximum max. air speed in knots.
            min_range: Minimum range of the aircraft in nautical miles.
            max_range: Maximum range of the aircraft in nautical miles.
            min_length: Minimum length of the aircraft in feet.
            max_length: Maximum length of the aircraft in feet.
            min_height: Minimum height of the aircraft in feet.
            max_height: Maximum height of the aircraft in feet.
            min_wingspan: Minimum wingspan of the aircraft in feet.
            max_wingspan: Maximum wingspan of the aircraft in feet.
            limit: How many results to return. Must be between 1 and 30. Default is 1.

        Returns:
            A list of Aircraft

        Raises:
            ValueError: If the provided limit is not between 1 and 30.
            MissingArgument: If no arguments are passed.
        """

        if not (1 <= limit <= 30):
            raise ValueError("limit must me between 1 and 30")

        params = filter_none_values(
            dict(
                manufacturer=manufacturer,
                model=model,
                engine_type=engine_type,
                min_speed=min_speed,
                max_speed=max_speed,
                min_range=min_range,
                max_range=max_range,
                min_length=min_length,
                max_length=max_length,
                min_height=min_height,
                max_height=max_height,
                min_wingspan=min_wingspan,
                max_wingspan=max_wingspan,
            )
        )

        if len(params) == 0:
            raise MissingArgument("...")

        params["limit"] = limit

        resp = HTTP.session.get(
            f"{BASE_URL}{cls.endpoint}",
            params=params,
        )

        return [Aircraft(**item) for item in resp.json()]
