from .type import ImageType
from .errors import *


class Preview(object):
    def __init__(self, snowflake: str, url: str, file_type: str, base_type: str, image_type: str, client):
        self.client = client
        self.snowflake = snowflake
        self.url = url
        self.image_type = ImageType(image_type, self.client)
        self.base_type = base_type
        self.file_type = file_type

    def __str__(self):
        return self.url

    @classmethod
    def parse(cls, response, client):
        status = response.get("status", 200)
        if status != 200:
            raise FileNotFoundError("This resource does not exist or you are not allowed to access.")
        try:
            data = cls(response["id"], response["url"], response["fileType"], response["baseType"], response["type"],
                       client)
        except KeyError:
            raise WeirdResponse
        else:
            return data
