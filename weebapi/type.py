from .preview import Preview


class ImageType(object):
    def __init__(self, name: str, client):
        self.name = name
        self.client = client

    def __str__(self):
        return self.name

    def __get__(self, instance, owner):
        return self.name

    @property
    async def get_preview(self):
        g = await self.client.request.get(str(self.client.route.types), params={
            "nsfw": "true",
            "preview": "true"
        })
        for p in g["preview"]:
            if p["type"] == self.name:
                return Preview.parse(p, self.client)
        raise FileNotFoundError
