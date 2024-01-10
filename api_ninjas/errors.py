class APINinjaException(Exception):
    """Base exception for the API Ninja library."""

    pass


class MissingArgument(APINinjaException):
    """Exception raised when no arguments are passed to the API."""

    def __init__(self) -> None:
        message = "More arguments are needed."
        super().__init__(message)


class TooManyArguments(APINinjaException):
    """Exception raised when too many confilcting arguments are passed to the API."""

    def __init__(self) -> None:
        message = "Too many conflicting arguments were passed."
        super().__init__(message)


class ValueOutOfRange(APINinjaException):
    """Exception raised when a value is out of the required range."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
