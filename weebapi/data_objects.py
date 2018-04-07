try:
    import discord
except ImportError:
    discord = None

import contextlib
import os
from .errors import *


class Image:
    """Represents an image from Weeb.sh.

    Attributes
    ------------
    snowflake: :class:`str`
        The image ID.
    image_type: :class:`ImageType`
        Type of the image.
    base_type: :class:`str`
        Base type of the image.
    nsfw: :class:`bool`
        Is image NSFW (not safe for work).
    file_type: :class:`str`
        Image file type.
    mime_type: :class:`str`
        Image MIME type.
    hidden: :class:`bool`
        Is image private.
    account: :class:`str`
        ID of the poster.
    source: Optional[:class:`str`]
        Source of the image.
    tags: :class:`list`
        List of `Tag` objects.
    url: :class:`str`
        CDN URL of the image.
    """

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
        """|coro|

        Removes current image.

        Raises
        --------
        Forbidden:
            If required permissions are absent.

        """
        g = await self.client.request.delete(str(self.client.route.image_remove.format_url(self.snowflake)))
        if g.get("status", 200) != 200:
            raise Forbidden("You are not allowed to access this resource.")

    async def add_tags(self, tags: list):
        """|coro|

        Adds tags to this image.

        Parameters
        -----------
        tags: :class:`list`
            List of strings.

        Raises
        --------
        Forbidden:
            If required permissions are absent.

        """
        g = await self.client.request.post(str(self.client.route.image_add_tags.format_url(self.snowflake)), data={
            "tags": ",".join(tags)
        })
        if g.get("status", 200) != 200:
            raise Forbidden("You are not allowed to access this resource.")

    async def remove_tags(self, tags: list):
        """|coro|

        Removes tags from this image.

        Parameters
        -----------
        tags: :class:`list`
            List of strings.

        Raises
        --------
        Forbidden:
            If required permissions are absent.

        """
        g = await self.client.request.delete(str(self.client.route.image_remove_tags.format_url(self.snowflake)),
                                             params={
                                                 "tags": ",".join(tags)
                                             })
        if int(g.get("status", 200)) != 200:
            raise Forbidden("You are not allowed to access this resource.")


class ImageType:
    """
    This object represents an image type. By itself returns the name.

    .. container::

        .. describe:: str()

            Returns the name of the image type.


    Attributes
    -------------
    name: :class:`str`
        Name of the image type.
    """
    def __init__(self, name: str, client):
        self.name = name
        self.client = client

    def __str__(self):
        return self.name

    def __get__(self, instance, owner):
        return self.name

    @property
    async def get_preview(self):
        """|coro|

        Returns a :class:`Preview` object of the image type.

        :return: :class:`Preview`
        """
        g = await self.client.request.get(str(self.client.route.types), params={
            "nsfw": "true",
            "preview": "true"
        })
        for p in g["preview"]:
            if p["type"] == self.name:
                return Preview.parse(p, self.client)
        raise FileNotFoundError


class Preview:
    """
    This class represents a preview object.

    .. container:: Options

        .. describe:: str()

            By itself it returns the image URL.


    Attributes
    -------------
    snowflake: :class:`str`
        Unique image identifier.
    url: :class:`str`
        URL of the preview image.
    image_type: :class:`ImageType`
        :class:`ImageType` object.
    base_type: :class:`str`
        Image base type.
    file_type: :class:`str`
        Image file type.
    """
    def __init__(self, snowflake: str, url: str, file_type: str, base_type: str, image_type: str, client):
        self.client = client
        self.snowflake = snowflake
        self.url = url
        self.image_type = ImageType(image_type, self.client)
        self.base_type = base_type
        self.file_type = file_type

    def __str__(self) -> str:
        return self.url

    @classmethod
    def parse(cls, response, client):
        status = response.get("status", 200)
        if status != 200:
            raise FileNotFoundError("This resource does not exist or you are not allowed to access.")
        try:
            data = cls(response["id"], response["url"], response["fileType"], response["baseType"], response["type"],
                       client)
        except KeyError:
            raise WeirdResponse
        else:
            return data


class Tag:
    """
    This class represents a Tag object.

    .. container:: Options

        .. describe:: str()

            Returns name of the tag.

        .. describe:: __get__

            By it self it returns the name of the tag.

    """
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
        """|coro|

        Checks if the tag is NSFW (not safe for work).

        :return: :class:`bool`
        """
        g = await self.client.request.get(str(self.client.route.tags), params={"nsfw": "only"})
        if g.get("status", 200) != 200:
            raise Forbidden("You are not allowed to access this resource.")
        if self.name in g["tags"]:
            return True
        else:
            return False


class ImageFile:
    """
    Represents a image file object usually retrieved from image generation.

    Attributes
    -----------
    file_path: :class:`str`
        Returns file path.
    discord_file: :class:`discord.File`
        If discord.py is installed it returns a :class:`discord.File` object, else raises an exception.

    Raises
    -------
    :class:`weebapi.errors.DiscordPyNotInstalled`
        Raised if discord.py is not installed, but :class:`discord.File` object is requested.

    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    @property
    def discord_file(self):
        if discord:
            return discord.File(open(self.file_path, 'rb'))
        else:
            raise DiscordPyNotInstalled

    def delete(self):
        """
        This function deletes the file.
        """
        with contextlib.suppress(FileNotFoundError):
            os.remove(self.file_path)
