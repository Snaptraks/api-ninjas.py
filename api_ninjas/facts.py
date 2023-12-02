from pydantic import BaseModel

from .base import BaseAPI


class Facts(BaseModel):
    fact: str


class FactsAPI(BaseAPI):
    endpoint = "/v1/facts"

    def get(self, limit: int = 1) -> list[Facts]:
        """
        Return one (or more) random facts.

        Args:
            limit: How many results to return. Must be between 1 and 30. Default is 1.

        Returns:
            A list of Facts.

        Raises:
            ValueError: If the provided limit is not between 1 and 30.
        """

        if not (1 <= limit <= 30):
            raise ValueError("limit must me between 1 and 30")

        resp = self.session.get(self.url, params={"limit": limit})

        return [Facts(**item) for item in resp.json()]
