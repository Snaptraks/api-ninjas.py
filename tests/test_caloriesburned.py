import pytest

from api_ninjas.caloriesburned import (
    Activity,
    CaloriesBurnedActivitiesAPI,
    CaloriesBurnedAPI,
)
from api_ninjas.errors import ValueOutOfRange


@pytest.fixture
def caloriesburnedactivities_api(api_token: str) -> CaloriesBurnedActivitiesAPI:
    return CaloriesBurnedActivitiesAPI(api_token)


@pytest.fixture
def caloriesburned_api(api_token: str) -> CaloriesBurnedAPI:
    return CaloriesBurnedAPI(api_token)


def test_get_activities(caloriesburnedactivities_api: CaloriesBurnedActivitiesAPI):
    activity_names = caloriesburnedactivities_api.get()

    assert isinstance(activity_names, list)
    assert len(activity_names) > 0
    assert isinstance(activity_names[0], str)


def test_get_calories_activity(caloriesburned_api: CaloriesBurnedAPI):
    activities = caloriesburned_api.get(activity="trampoline")

    assert isinstance(activities, list)
    assert len(activities) > 0
    assert isinstance(activities[0], Activity)


def test_get_calories_weight(caloriesburned_api: CaloriesBurnedAPI):
    caloriesburned_api.get(activity="walk", weight=70)


def test_get_calories_duration(caloriesburned_api: CaloriesBurnedAPI):
    caloriesburned_api.get(activity="walk", duration=120)


def test_weight_out_of_range(caloriesburned_api: CaloriesBurnedAPI):
    with pytest.raises(ValueOutOfRange):
        caloriesburned_api.get(activity="walk", weight=700)

    with pytest.raises(ValueOutOfRange):
        caloriesburned_api.get(activity="walk", weight=40)


def test_duration_out_of_range(caloriesburned_api: CaloriesBurnedAPI):
    with pytest.raises(ValueOutOfRange):
        caloriesburned_api.get(activity="walk", duration=0.5)
