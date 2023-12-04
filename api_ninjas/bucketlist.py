from pydantic import BaseModel

from api_ninjas.base import BaseAPI


class BucketList(BaseModel):
    item: str


class BucketListAPI(BaseAPI):
    """
    The Bucket List API provides thousands of innovative
    bucket list ideas for every type of person.
    """

    endpoint = "/v1/bucketlist"

    def get(self) -> BucketList:
        """
        Return a random bucket list idea.

        Returns:
            A BucketList idea.
        """

        resp = self.session.get(self.url)

        return BucketList(**resp.json())
