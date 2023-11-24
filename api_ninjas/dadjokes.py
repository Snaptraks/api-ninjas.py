from pydantic import BaseModel

from .base import BASE_URL, BaseAPI
from .http import HTTP


class DadJokes(BaseModel):
    joke: str


class DadJokesAPI(BaseAPI):
    endpoint = "/v1/dadjokes"

    @classmethod
    def get(cls, limit: int = 1) -> list[DadJokes]:
        """Return one (or more) random dad jokes.

        Args:
            limit: How many jokes to return. Must be between 1 and 10. Default is 1.

        Returns:
            A list of DadJokes.

        Raises:
            ValueError: If the provided limit is not between 1 and 10.
        """

        if not (1 <= limit <= 10):
            raise ValueError("limit must be between 1 and 10.")

        resp = HTTP.session.get(f"{BASE_URL}{cls.endpoint}", params={"limit": limit})

        return [DadJokes(**r) for r in resp.json()]
