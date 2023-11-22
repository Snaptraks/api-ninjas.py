import requests


class HTTP:
    session = requests.Session()

    @classmethod
    def set_token(cls, token: str) -> None:
        cls.session.headers.update({"X-Api-Key": token})
