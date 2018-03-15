class ImageType(object):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    async def get_preview(self):
        raise NotImplementedError
