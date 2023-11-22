import pytest

from api_ninjas.base import Result, BaseAPI
from api_ninjas.dadjokes import DadJokes, DadJokesAPI


def test_inheritance():
    assert issubclass(DadJokes, Result)
    assert issubclass(DadJokesAPI, BaseAPI)


def test_get():
    dad_jokes = DadJokesAPI.get()
    assert isinstance(dad_jokes, list)
    if len(dad_jokes) > 0:
        assert isinstance(dad_jokes[0], DadJokes)
        assert isinstance(dad_jokes[0].joke, str)


def test_get_many():
    n = 2
    dad_jokes = DadJokesAPI.get(n)
    assert len(dad_jokes) == n


def test_get_too_many():
    with pytest.raises(ValueError):
        DadJokesAPI.get(11)


def test_get_not_enough():
    with pytest.raises(ValueError):
        DadJokesAPI.get(0)
