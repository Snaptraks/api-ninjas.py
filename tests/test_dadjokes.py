import pytest
from pydantic import BaseModel

from api_ninjas.base import BaseAPI
from api_ninjas.dadjokes import DadJokes, DadJokesAPI


@pytest.fixture
def dadjokes_api(api_token: str) -> DadJokesAPI:
    return DadJokesAPI(api_token)


def test_inheritance():
    assert issubclass(DadJokes, BaseModel)
    assert issubclass(DadJokesAPI, BaseAPI)


def test_get(dadjokes_api: DadJokesAPI):
    dad_jokes = dadjokes_api.get()
    assert isinstance(dad_jokes, list)
    if len(dad_jokes) > 0:
        assert isinstance(dad_jokes[0], DadJokes)
        assert isinstance(dad_jokes[0].joke, str)


def test_get_many(dadjokes_api: DadJokesAPI):
    n = 2
    dad_jokes = dadjokes_api.get(n)
    assert len(dad_jokes) == n


def test_get_too_many(dadjokes_api: DadJokesAPI):
    with pytest.raises(ValueError):
        dadjokes_api.get(11)


def test_get_not_enough(dadjokes_api: DadJokesAPI):
    with pytest.raises(ValueError):
        dadjokes_api.get(0)
