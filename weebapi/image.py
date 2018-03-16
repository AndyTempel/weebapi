from .errors import *
from .tag import Tag
from .type import ImageType


class Image(object):
    def __init__(self, snowflake: str, image_type: str, base_type: str, nsfw: bool, file_type: str, mime_type: str,
                 tags: list, url: str, hidden: bool, account: str, client, source: str = ""):
        self.client = client
        self.snowflake = snowflake
        self.type = ImageType(image_type, self.client)
        self.base_type = base_type
        self.nsfw = nsfw
        self.file_type = file_type
        self.mime_type = mime_type
        self.hidden = hidden
        self.account = account
        self.source = source
        self.tags = [Tag(t, self.client) for t in tags]
        self.url = url

    def __str__(self):
        return self.url

    @classmethod
    def parse(cls, response, client):
        status = response.get("status", 200)
        if status != 200:
            raise FileNotFoundError("This resource does not exist or you are not allowed to access.")
        try:
            data = cls(response["id"], response["type"], response["baseType"], response["nsfw"], response["fileType"],
                       response["mimeType"], response["tags"], response["url"], response["hidden"], response["account"],
                       client=client, source=response.get("source", ""))
        except KeyError:
            raise WeirdResponse
        else:
            return data

    async def delete(self):
        g = await self.client.request.delete(str(self.client.route.image_remove.format_url(self.snowflake)))
        if g.get("status", 200) != 200:
            raise Forbidden("You are not allowed to access this resource.")

    async def add_tags(self, tags: list):
        g = await self.client.request.post(str(self.client.route.image_add_tags.format_url(self.snowflake)), data={
            "tags": ",".join(tags)
        })
        if g.get("status", 200) != 200:
            raise Forbidden("You are not allowed to access this resource.")

    async def remove_tags(self, tags: list):
        g = await self.client.request.delete(str(self.client.route.image_remove_tags.format_url(self.snowflake)),
                                             params={
                                                 "tags": ",".join(tags)
                                             })
        if g.get("status", 200) != 200:
            raise Forbidden("You are not allowed to access this resource.")
