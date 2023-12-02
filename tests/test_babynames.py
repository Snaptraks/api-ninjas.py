import pytest

from api_ninjas.babynames import BabyNamesAPI, Gender
from api_ninjas.base import BaseAPI


@pytest.fixture
def babynames_api(api_token: str) -> BabyNamesAPI:
    return BabyNamesAPI(api_token)


def test_inheritance():
    assert issubclass(BabyNamesAPI, BaseAPI)


def test_get(babynames_api: BabyNamesAPI):
    names = babynames_api.get()
    assert isinstance(names, list)
    assert len(names) > 0
    assert isinstance(names[0], str)


def test_get_gender(babynames_api: BabyNamesAPI):
    names = babynames_api.get(gender=Gender.GIRL)
    assert isinstance(names, list)
    assert len(names) > 0


def test_get_gender_not_popular(babynames_api: BabyNamesAPI):
    names = babynames_api.get(gender=Gender.NEUTRAL, popular_only=False)
    assert isinstance(names, list)
    assert len(names) > 0
