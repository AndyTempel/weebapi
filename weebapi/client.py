from typing import Union

from .errors import *
from .request_lib import krequest
from .router import Router
from .image import Image

BASE_URL = "https://api.weeb.sh/"


class Client(object):
    def __init__(self, api_key: str, wolke_token: bool = True, check_ssl: bool = True, base_url: str = BASE_URL,
                 bot=None):
        self.api_key = api_key
        self.check_ssl = check_ssl
        self.route = Router(base_url)
        self.request = krequest(global_headers=[
            ("Authorization", f"Wolke {self.api_key}" if wolke_token else f"Bearer {self.api_key}")
        ])
        self.bot = bot

    @classmethod
    def pluggable(cls, bot, api_key: str, *args, **kwargs):
        try:
            return bot.weebsh
        except AttributeError:
            bot.weebsh = cls(api_key, bot=bot, *args, **kwargs)
            return bot.weebsh

    async def get_random(self, tags: Union(str, list) = None, image_type: str = None, nsfw: int = 1,
                         hidden: bool = False, file_type: str = None):
        params = dict
        if tags:
            if isinstance(tags, str):
                params.update({"tags": tags})
            elif isinstance(tags, list):
                params.update({"tags": ",".join(tags)})
        if image_type:
            params.update({"type": image_type})
        if not params:
            raise MissingRequiredArguments("Add tags and/or type.")
        if 1 <= nsfw <= 3:
            if nsfw == 1:
                nsfw = "false"
            elif nsfw == 2:
                nsfw = "true"
            else:
                nsfw = "only"
            params.update({"nsfw": nsfw})
        else:
            raise ValueError("Must be >=1 and <=3!")
        if hidden:
            params.update({"hidden": "true"})
        if file_type:
            if file_type in ["jpg", "jpeg", "png", "gif"]:
                params.update({"filetype": file_type})
            else:
                raise ValueError("Invalid filetype. (Available: jpg, jpeg, png, gif)")
        g = await self.request.get(self.route.random, params=params)
        return Image(g["id"], g["type"], g["baseType"], g["nsfw"], g["fileType"], g["mimeType"], g["tags"], g["url"],
                     g["hidden"], g["account"], g.get("source", ""))
