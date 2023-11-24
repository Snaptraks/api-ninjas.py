from pydantic import BaseModel
import pytest

from api_ninjas.base import BaseAPI
from api_ninjas.facts import Facts, FactsAPI


def test_inheritance():
    assert issubclass(Facts, BaseModel)
    assert issubclass(FactsAPI, BaseAPI)


def test_get():
    facts = FactsAPI.get()
    assert isinstance(facts, list)
    if len(facts) > 0:
        assert isinstance(facts[0], Facts)
        assert isinstance(facts[0].fact, str)
        assert facts[0].fact != ""


def test_get_many():
    n = 2
    facts = FactsAPI.get(n)
    assert len(facts) == n


def test_get_too_many():
    with pytest.raises(ValueError):
        FactsAPI.get(31)


def test_get_not_enough():
    with pytest.raises(ValueError):
        FactsAPI.get(0)
