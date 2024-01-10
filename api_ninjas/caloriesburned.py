from pydantic import BaseModel

from api_ninjas.base import BaseAPI
from api_ninjas.errors import ValueOutOfRange
from api_ninjas.utils import filter_none_values


class Activity(BaseModel):
    name: str
    calories_per_hour: int
    duration_minutes: int
    total_calories: int


class CaloriesBurnedAPI(BaseAPI):
    """
    The Calories Burned API calculates the total calories burned for hundreds
    of sports and activities. It supports custom weight and duration.
    """

    endpoint = "/v1/caloriesburned"

    def get(
        self, *, activity: str, weight: float = 160, duration: float = 60
    ) -> list[Activity]:
        """
        Return the calories burned per hour and total calories burned according
        to given parameters for given activities (up to 10).

        Args:
            activity: Name of the given activity. This value can be partial
                (e.g. ski will match water skiing and downhill skiing)
            weight: Weight of the user performing the activity in pounds.
                Must be between 50 and 500. Default value is 160.
            duration: How long the activity was performed in minutes.
                Must be 1 or greater. Default value is 60 (1 hour).

        Returns:
            A list of Activity
        """

        weight_lower, weight_upper = 50, 500
        if not (weight_lower <= weight <= weight_upper):
            raise ValueOutOfRange(
                f"weight must be between {weight_lower} and {weight_upper}."
            )

        duration_lower = 1
        if duration < duration_lower:
            raise ValueOutOfRange(
                f"duration must be more or greater than {duration_lower}."
            )

        params = filter_none_values(
            dict(
                activity=activity,
                weight=weight,
                duration=duration,
            )
        )

        resp = self.session.get(self.url, params=params)

        return [Activity(**item) for item in resp.json()]


class CaloriesBurnedActivitiesAPI(BaseAPI):
    endpoint = "/v1/caloriesburnedactivities"

    def get(self):
        """
        Returns the full list of activities supported by this API.
        """
        resp = self.session.get(self.url)
        return resp.json()["activities"]
