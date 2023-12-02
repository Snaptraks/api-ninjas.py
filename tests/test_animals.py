import pytest
from pydantic import BaseModel

from api_ninjas.animals import Animal, AnimalsAPI, Characteristics, Taxonomy
from api_ninjas.base import BaseAPI


@pytest.fixture
def animals_api(api_token: str):
    return AnimalsAPI(api_token)


def test_inheritance():
    assert issubclass(Animal, BaseModel)
    assert issubclass(AnimalsAPI, BaseAPI)


def test_get(animals_api: AnimalsAPI):
    animals = animals_api.get(name="tiger")

    assert isinstance(animals, list)
    assert len(animals) > 0
    assert isinstance(animals[0], Animal)
    assert isinstance(animals[0].characteristics, Characteristics)
    assert isinstance(animals[0].taxonomy, Taxonomy)
