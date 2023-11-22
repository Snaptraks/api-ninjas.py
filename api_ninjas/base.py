from dataclasses import dataclass

BASE_URL = "https://api.api-ninjas.com"


@dataclass
class Result:
    ...


class BaseAPI:
    endpoint: str

    def get(self, **kwargs) -> list[Result]:
        raise NotImplementedError
