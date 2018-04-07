import os
import tempfile
import uuid

from .data_objects import ImageFile


class ImgGen:
    def __init__(self, client):
        self.client = client
        self.http = self.client.request

    async def get_simple(self, img_type: str, face_color: str = None, hair_color: str = None) -> ImageFile:
        """|coro|

        Generates simple image.

        Available types:
         * ``awooo``
         * ``eyes``
         * ``won``

        Parameters
        -----------
        img_type: :class:`str`
            Type of the image. See available types above.
        face_color: :class:`str`
            Only for ``awooo`` type. HEX string for color.
        hair_color: :class:`str`
            Only for ``awooo`` type. HEX string for color.


        :return: :class:`weebapi.data_objects.ImageFile`

        """
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

        r = await self.http.download_get(str(self.client.route.imggen_simple), filename, params=params)

        return ImageFile(filename)

    async def discord_status(self, status: str="online", avatar: str=None) -> ImageFile:
        """|coro|

        Generates a discord status image.

        Available types:
         * ``online``
         * ``idle``
         * ``dnd``
         * ``streaming``
         * ``offline``

        Parameters
        -----------
        status: :class:`str`
            Type of the image. See available types above.
        avatar: :class:`str`
            URL of the avatar.


        :return: :class:`weebapi.data_objects.ImageFile`

        """
        if status not in ["online", "idle", "dnd", "streaming", "offline"]:
            raise ValueError("Type can be either: online, idle, dnd, streaming or offline!")
        params = {
            "status": status
        }
        if avatar:
            params.update({"avatar": avatar})

        filename = os.path.join(tempfile.gettempdir(), f"img_gen_status_{uuid.uuid4()}.png")

        r = await self.http.download_get(str(self.client.route.imggen_status), filename, params=params)

        return ImageFile(filename)

    async def license(self, title: str, avatar: str, badges: list=[], widgets: list=[]) -> ImageFile:
        """|coro|

        Generates a spook license.

        Parameters
        -----------
        title: :class:`str`
            Title of the card.
        avatar: :class:`str`
            URL of the avatar.
        badges: :class:`list` Optional
            List of string URLs of the images. Max 3.
        widgets: :class:`list` Optional
            List of strings. Max 3.


        :return: :class:`weebapi.data_objects.ImageFile`

        """
        params = {
            "title": title,
            "avatar": avatar,
        }
        if badges:
            if len(badges) > 3:
                badges = badges[:3]
            params.update({"badges": badges})
        if widgets:
            if len(widgets) > 3:
                widgets = widgets[:3]
            params.update({"widgets": widgets})

        filename = os.path.join(tempfile.gettempdir(), f"img_gen_spook_{uuid.uuid4()}.png")

        r = await self.http.download_post(str(self.client.route.imggen_license), filename, json=params)

        return ImageFile(filename)

    async def waifu_insult(self, avatar: str) -> ImageFile:
        """|coro|

        Generates a waifu insult.

        Parameters
        -----------
        avatar: :class:`str`
            URL of the avatar.


        :return: :class:`weebapi.data_objects.ImageFile`

        """
        params = {
            "avatar": avatar,
        }

        filename = os.path.join(tempfile.gettempdir(), f"img_gen_waifu_{uuid.uuid4()}.png")

        r = await self.http.download_post(str(self.client.route.imggen_waifu), filename, json=params)

        return ImageFile(filename)

    async def love(self, avatar1: str, avatar2: str) -> ImageFile:
        """|coro|

        Generates a love image.

        Parameters
        -----------
        avatar1: :class:`str`
            URL of the avatar displayed on the left.
        avatar2: :class:`str`
            URL of the avatar displayed on the right.


        :return: :class:`weebapi.data_objects.ImageFile`

        """
        params = {
            "targetOne": avatar1,
            "targetTwo": avatar2
        }

        filename = os.path.join(tempfile.gettempdir(), f"img_gen_love_{uuid.uuid4()}.png")

        r = await self.http.download_post(str(self.client.route.imggen_love), filename, json=params)

        return ImageFile(filename)
