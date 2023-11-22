import api_ninjas


def test_set_token():
    token = "RandomTokenString"
    api_ninjas.set_token(token)
    headers = api_ninjas.http.HTTP.session.headers
    assert token in set(headers.values())
