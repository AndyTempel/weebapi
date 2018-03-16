from .errors import *


class Tag(object):
    def __init__(self, tag: dict, client):
        self.name = tag.get("name", "unknown")
        self.account = tag.get("user", "unknown")
        self.is_hidden = tag.get("hidden", False)
        self.client = client

    def __str__(self) -> str:
        return self.name

    def __get__(self, instance, owner) -> str:
        return self.name

    @property
    async def is_nsfw(self) -> bool:
        g = await self.client.request.get(str(self.client.route.tags), params={"nsfw": "only"})
        if g.get("status", 200) != 200:
            raise Forbidden("You are not allowed to access this resource.")
        if self.name in g["tags"]:
            return True
        else:
            return False
