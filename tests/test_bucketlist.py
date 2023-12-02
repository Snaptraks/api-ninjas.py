import pytest

from api_ninjas.base import BaseAPI
from api_ninjas.bucketlist import BucketList, BucketListAPI


@pytest.fixture
def bucketlist_api(api_token: str) -> BucketListAPI:
    return BucketListAPI(api_token)


def test_inheritance():
    assert issubclass(BucketListAPI, BaseAPI)


def test_get(bucketlist_api: BucketListAPI):
    bucketlist = bucketlist_api.get()
    assert isinstance(bucketlist, BucketList)
    assert isinstance(bucketlist.item, str)
    assert bucketlist.item != ""
