from enum import StrEnum

from api_ninjas.base import BaseAPI
from api_ninjas.utils import filter_none_values


class Gender(StrEnum):
    BOY = "boy"
    GIRL = "girl"
    NEUTRAL = "neutral"


class BabyNamesAPI(BaseAPI):
    """
    The Baby Names API provides tens of thousands of unique and
    popular baby names for boys, girls, and gender-neutral names.
    """

    endpoint = "/v1/babynames"

    def get(
        self, *, gender: Gender | None = None, popular_only: bool = True
    ) -> list[str]:
        """
        Return 10 baby name results.

        Args:
            gender: Baby name gender. Must be one of the following:
                Gender.BOY, Gender.GIRL, Gender.NEUTRAL
            popular_only: Whether to only return popular (top 10%) of names.
                Must be either True or False. If unset, default is True.

        Returns:
            A list of baby names.
        """

        params = filter_none_values(
            dict(
                gender=gender,
                popular_only=popular_only,
            )
        )

        resp = self.session.get(self.url, params=params)

        return resp.json()
