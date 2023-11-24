def filter_none_values(params: dict) -> dict:
    """Return a dict where the keys with value None are removed"""

    return {k: v for k, v in params.items() if v is not None}
