from api_ninjas.aircraft import AircraftAPI
from api_ninjas.airlines import AirlinesAPI


def test_set_token():
    token = "RandomTokenString"
    aircraft_api = AircraftAPI(token)
    assert token in set(aircraft_api.session.headers.values())


def test_session_is_shared(api_token: str):
    api1 = AircraftAPI(api_token)
    api2 = AirlinesAPI(api_token)

    assert api1 is not api2
    assert api1.session is api2.session
