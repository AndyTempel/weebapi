# -*- coding: utf-8 -*-

from weebapi.errors import RequireFormatting


class Route(object):
    def __init__(self, url: str, method: str, require_format: bool = False):
        self.url = url
        self.method = method
        self.require_format = require_format

    def __str__(self) -> str:
        if self.require_format:
            raise RequireFormatting
        return self.url

    def __get__(self, instance, owner) -> str:
        if self.require_format:
            raise RequireFormatting
        return self.url

    def format_url(self, *args) -> str:
        return self.url.format(*args)


class Router(object):
    def __init__(self, base_url: str):
        if not base_url.endswith("/"):
            base_url += "/"
        self.base_url = base_url
        self.base_image = base_url + "images/"
        self.base_imggen = base_url + "auto-image/"

        self.upload = Route(self.base_image + "upload", "POST")
        self.types = Route(self.base_image + "types", "GET")
        self.tags = Route(self.base_image + "tags", "GET")
        self.random = Route(self.base_image + "random", "GET")

        self.image = Route(self.base_image + "info/{}", "GET", True)
        self.image_add_tags = Route(self.base_image + "info/{}/tags", "POST", True)
        self.image_remove_tags = Route(self.base_image + "info/{}/tags", "DELETE", True)
        self.image_remove = Route(self.base_image + "info/{}", "DELETE", True)

        self.imggen_simple = Route(self.base_imggen + "generate", "GET")
        self.imggen_status = Route(self.base_imggen + "discord-status", "GET")
        self.imggen_license = Route(self.base_imggen + "license", "POST")
        self.imggen_waifu = Route(self.base_imggen + "waifu-insult", "POST")
        self.imggen_love = Route(self.base_imggen + "love-ship", "POST")
