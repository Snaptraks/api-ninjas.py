from api_ninjas.utils import filter_none_values


def test_filter_none_values():
    start_dict = dict(
        a=1,
        b=2.5,
        c=None,
        d="a",
        e=None,
    )
    end_dict = dict(
        a=1,
        b=2.5,
        d="a",
    )

    assert filter_none_values(start_dict) == end_dict
