from pydantic import BaseModel

from .base import BASE_URL, BaseAPI
from .http import HTTP


class Facts(BaseModel):
    fact: str


class FactsAPI(BaseAPI):
    endpoint = "/v1/facts"

    @classmethod
    def get(cls, limit: int = 1) -> list[Facts]:
        """Return one (or more) random facts.

        Args:
            limit: How many results to return. Must be between 1 and 30. Default is 1.

        Returns:
            A list of Facts.

        Raises:
            ValueError: If the provided limit is not between 1 and 30.
        """

        if not (1 <= limit <= 30):
            raise ValueError("limit must me between 1 and 30")

        resp = HTTP.session.get(f"{BASE_URL}{cls.endpoint}", params={"limit": limit})

        return [Facts(**r) for r in resp.json()]
