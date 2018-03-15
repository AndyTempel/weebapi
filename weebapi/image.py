from .type import ImageType
from .tag import Tag


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
