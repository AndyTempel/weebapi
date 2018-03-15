from .type import ImageType


class Preview(object):
    def __init__(self, snowflake: str, url: str, file_type: str, base_type: str, image_type: str):
        self.snowflake = snowflake
        self.url = url
        self.image_type = ImageType(image_type)
        self.base_type = base_type
        self.file_type = file_type

    def __str__(self):
        return self.url
