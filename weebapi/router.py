from .errors import RequireFormatting


class Route(object):
    def __init__(self, url: str, method: str, require_format: bool = False):
        self.url = url
        self.method = method
        self.require_format = require_format

    def __str__(self):
        if self.require_format:
            raise RequireFormatting
        return self.url

    def format_url(self, *args):
        return self.url.format(args)


class Router(object):
    def __init__(self, base_url: str):
        if not base_url.endswith("/"):
            base_url += "/"
        self.base_url = base_url
        self.upload = Route(self.base_url + "upload", "POST")
        self.types = Route(self.base_url + "types", "GET")
        self.tags = Route(self.base_url + "tags", "GET")
        self.random = Route(self.base_url + "random", "GET")
        self.image = Route(self.base_url + "info/{}", "GET", True)
        self.image_add_tags = Route(self.base_url + "info/{}/tags", "POST", True)
        self.image_remove_tags = Route(self.base_url + "info/{}/tags", "DELETE", True)
        self.image_remove = Route(self.base_url + "info/{}", "DELETE", True)
