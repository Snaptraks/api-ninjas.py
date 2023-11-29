from pydantic import BaseModel

from .http import HTTPSession

BASE_URL = "https://api.api-ninjas.com"


class BaseAPI:
    endpoint: str

    def __init__(self, token: str) -> None:
        self.session = HTTPSession
        self.session.headers.update({"X-Api-Key": token})

    @property
    def url(self) -> str:
        """Return the complete API URL based on the endpoint."""

        return f"{BASE_URL}{self.endpoint}"

    def get(self, **kwargs) -> list[BaseModel]:
        raise NotImplementedError
