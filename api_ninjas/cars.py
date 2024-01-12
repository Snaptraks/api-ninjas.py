from typing import Literal

from pydantic import BaseModel, Field

from api_ninjas.base import BaseAPI
from api_ninjas.errors import MissingArgument, ValueOutOfRange
from api_ninjas.utils import filter_none_values

Cylinders = Literal[2, 3, 4, 5, 6, 8, 10, 12, 16]
Drive = Literal["fwd", "rwd", "awd", "4wd"]
FuelType = Literal["gas", "diesel", "electricity"]
Transmission = Literal["m", "a"]


class Car(BaseModel):
    city_mpg: float
    class_: str = Field(None, alias="class")
    combination_mpg: float
    cylinders: Cylinders
    displacement: float
    drive: Drive
    fuel_type: FuelType
    highway_mpg: float
    make: str
    model: str
    transmission: Transmission
    year: int


class CarsAPI(BaseAPI):
    """
    The Cars API provides detailed information on thousands of
    vehicle models from over a hundred automakers.
    """

    endpoint = "/v1/cars"

    def get(
        self,
        *,
        make: str | None = None,
        model: str | None = None,
        fuel_type: FuelType | None = None,
        drive: Drive | None = None,
        cylinders: Cylinders | None = None,
        transmission: Transmission | None = None,
        year: int | None = None,
        min_city_mpg: float | None = None,
        max_city_mpg: float | None = None,
        min_hwy_mpg: float | None = None,
        max_hwy_mpg: float | None = None,
        min_comb_mpg: float | None = None,
        max_comb_mpg: float | None = None,
        limit: int = 5,
    ) -> list[Car]:
        """
        Get car data from given parameters.
        Returns a list of car models (and their information) that satisfy
        the parameters.

        Args:
            make: Vehicle manufacturer (e.g. audi or toyota).
            model: Vehicle manufacturer (e.g. a4 or corolla).
            fuel_type: Type of fuel used. Possible values: gas, diesel, electricity.
            drive: Drive transmission. Possible values: fwd (front-wheel drive),
                rwd (rear-wheel drive), awd (all-wheel drive), 4wd (four-wheel drive).
            cylinders: Number of cylinders in engine. Possible values: 2, 3 4, 5, 6,
                8, 10, 12, 16.
            transmission: Type of transmission. Possible values: m (for manual),
                a (for automatic).
            year: Vehicle model year (e.g. 2018).
            min_city_mpg: Minimum city fuel consumption (in miles per gallon).
            max_city_mpg: Maximum city fuel consumption (in miles per gallon).
            min_hwy_mpg: Minimum highway fuel consumption (in miles per gallon).
            max_hwy_mpg: Maximum highway fuel consumption (in miles per gallon).
            min_comb_mpg: Minimum combination (city and highway) fuel consumption
                (in miles per gallon).
            max_comb_mpg: Maximum combination (city and highway) fuel consumption
                (in miles per gallon).
            limit: How many results to return. Must be between 1 and 50. Default is 5.

        Returns:
            A list of Car.

        Raises:
            ValueOutOfRange: If the provided limit is not between 1 and 50.
            MissingArgument: If no arguments are passed.
        """

        limit_lower, limit_upper = 1, 50
        if not (limit_lower <= limit <= limit_upper):
            raise ValueOutOfRange(
                f"limit must be between {limit_lower} and {limit_upper}."
            )

        params = filter_none_values(
            dict(
                make=make,
                model=model,
                fuel_type=fuel_type,
                drive=drive,
                cylinders=cylinders,
                transmission=transmission,
                year=year,
                min_city_mpg=min_city_mpg,
                max_city_mpg=max_city_mpg,
                min_hwy_mpg=min_hwy_mpg,
                max_hwy_mpg=max_hwy_mpg,
                min_comb_mpg=min_comb_mpg,
                max_comb_mpg=max_comb_mpg,
            )
        )

        if len(params) == 0:
            raise MissingArgument()

        resp = self.session.get(self.url, params=params)

        return [Car(**item) for item in resp.json()]
