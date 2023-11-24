class MissingArgument(Exception):
    """Exception raised when no arguments are passed to the API."""

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message)
