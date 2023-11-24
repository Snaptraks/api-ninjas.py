from pydantic import BaseModel

BASE_URL = "https://api.api-ninjas.com"


class BaseAPI:
    endpoint: str

    def get(self, **kwargs) -> list[BaseModel]:
        raise NotImplementedError
