import pytest

from api_ninjas.base import Result, BaseAPI
from api_ninjas.facts import Facts, FactsAPI


def test_inheritance():
    assert issubclass(Facts, Result)
    assert issubclass(FactsAPI, BaseAPI)


def test_get():
    dad_jokes = FactsAPI.get()
    assert isinstance(dad_jokes, list)
    if len(dad_jokes) > 0:
        assert isinstance(dad_jokes[0], Facts)
        assert isinstance(dad_jokes[0].fact, str)


def test_get_many():
    n = 2
    dad_jokes = FactsAPI.get(n)
    assert len(dad_jokes) == n


def test_get_too_many():
    with pytest.raises(ValueError):
        FactsAPI.get(31)


def test_get_not_enough():
    with pytest.raises(ValueError):
        FactsAPI.get(0)
