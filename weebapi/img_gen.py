import os
import tempfile
import uuid

from .data_objects import ImageFile


class ImgGen:
    def __init__(self, client):
        self.client = client
        self.http = self.client.request

    async def get_simple(self, img_type: str, face_color: str = None, hair_color: str = None) -> ImageFile:
        if img_type not in ["awooo", "eyes", "won"]:
            raise ValueError("Type can be either: awooo, eyes or won!")
        params = {
            "type": img_type
        }
        if img_type == "awooo" and face_color:
            params.update({"face": face_color})
        if img_type == "awooo" and hair_color:
            params.update({"hair": hair_color})

        filename = os.path.join(tempfile.gettempdir(), f"img_gen_simple_{uuid.uuid4()}.png")

        r = await self.http.download_get(self.client.route.imggen_simple, filename, params=params)

        return ImageFile(filename)
