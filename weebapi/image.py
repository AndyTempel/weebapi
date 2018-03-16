from .errors import *
from .tag import Tag
from .type import ImageType


class Image(object):
    def __init__(self, snowflake: str, image_type: str, base_type: str, nsfw: bool, file_type: str, mime_type: str,
                 tags: list, url: str, hidden: bool, account: str, source: str = ""):
        self.snowflake = snowflake
        self.type = ImageType(image_type)
        self.base_type = base_type
        self.nsfw = nsfw
        self.file_type = file_type
        self.mime_type = mime_type
        self.hidden = hidden
        self.account = account
        self.source = source
        self.tags = [Tag(t) for t in tags]
        self.url = url

    def __str__(self):
        return self.url

    @classmethod
    def parse(cls, response):
        status = response.get("status", 200)
        if status != 200:
            raise FileNotFoundError("This resource does not exist or you are not allowed to access.")
        try:
            data = cls(response["id"], response["type"], response["baseType"], response["nsfw"], response["fileType"],
                       response["mimeType"], response["tags"], response["url"], response["hidden"], response["account"],
                       response.get("source", ""))
        except KeyError:
            raise WeirdResponse
        else:
            return data
