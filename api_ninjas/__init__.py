from .http import HTTP


def set_token(token: str | None) -> None:
    """Set the token in the Config singleton."""

    if token is None:
        raise ValueError("Token cannot be empty")

    HTTP.set_token(token=token)
