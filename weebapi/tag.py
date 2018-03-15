class Tag(object):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    @property
    async def is_nsfw(self) -> bool:
        raise NotImplementedError

    @property
    async def is_hidden(self) -> bool:
        raise NotImplementedError
