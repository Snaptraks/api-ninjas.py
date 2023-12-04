from pydantic import BaseModel, Field

from api_ninjas.base import BaseAPI


class Taxonomy(BaseModel):
    kingdom: str
    phylum: str | None = None
    class_: str = Field(None, alias="class")
    order: str | None = None
    family: str | None = None
    genus: str | None = None
    scientific_name: str | None = None


class Characteristics(BaseModel):
    age_of_fledgling: str | None = None
    age_of_independence: str | None = None
    age_of_molting: str | None = None
    age_of_sexual_maturity: str | None = None
    age_of_weaning: str | None = None
    aggression: str | None = None
    average_clutch_size: str | None = None
    average_litter_size: str | None = None
    average_spawn_size: str | None = None
    biggest_threat: str | None = None
    color: str | None = None
    common_name: str | None = None
    diet: str | None = None
    distinctive_feature: str | None = None
    estimated_population_size: str | None = None
    favorite_food: str | None = None
    gestation_period: str | None = None
    group: str | None = None
    group_behavior: str | None = None
    habitat: str | None = None
    height: str | None = None
    incubation_period: str | None = None
    length: str | None = None
    lifespan: str | None = None
    lifestyle: str | None = None
    litter_size: str | None = None
    location: str | None = None
    main_prey: str | None = None
    migratory: str | None = None
    most_distinctive_feature: str | None = None
    name_of_young: str | None = None
    nesting_location: str | None = None
    number_of_species: str | None = None
    optimum_ph_level: str | None = None
    origin: str | None = None
    other_names: str | None = Field(None, alias="other_name(s)")
    predators: str | None = None
    prey: str | None = None
    skin_type: str | None = None
    slogan: str | None = None
    special_features: str | None = None
    temperament: str | None = None
    top_speed: str | None = None
    training: str | None = None
    type_: str | None = Field(None, alias="type")
    venomous: str | None = None
    water_type: str | None = None
    weight: str | None = None
    wingspan: str | None = None


class Animal(BaseModel):
    name: str
    taxonomy: Taxonomy
    locations: list[str]
    characteristics: Characteristics


class AnimalsAPI(BaseAPI):
    """
    The Animals API provides interesting scientific facts on
    thousands of different animal species.
    """

    endpoint = "/v1/animals"

    def get(self, *, name: str) -> list[Animal]:
        """
        Return up to 10 results matching the input name parameter.

        Args:
            name: Common name of animal to search.
                This parameter supports partial matches
                (e.g. fox will match gray fox and red fox)

        Returns:
            A list of Animals.
        """
        resp = self.session.get(self.url, params={"name": name})

        return [Animal(**item) for item in resp.json()]
