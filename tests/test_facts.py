import pytest
from pydantic import BaseModel

from api_ninjas.base import BaseAPI
from api_ninjas.facts import Facts, FactsAPI


@pytest.fixture
def facts_api(api_token: str) -> FactsAPI:
    return FactsAPI(api_token)


def test_inheritance():
    assert issubclass(Facts, BaseModel)
    assert issubclass(FactsAPI, BaseAPI)


def test_get(facts_api: FactsAPI):
    facts = facts_api.get()
    assert isinstance(facts, list)
    if len(facts) > 0:
        assert isinstance(facts[0], Facts)
        assert isinstance(facts[0].fact, str)
        assert facts[0].fact != ""


def test_get_many(facts_api: FactsAPI):
    n = 2
    facts = facts_api.get(n)
    assert len(facts) == n


def test_get_too_many(facts_api: FactsAPI):
    with pytest.raises(ValueError):
        facts_api.get(31)


def test_get_not_enough(facts_api: FactsAPI):
    with pytest.raises(ValueError):
        facts_api.get(0)
