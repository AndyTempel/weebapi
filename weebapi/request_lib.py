import sys
import traceback

import aiohttp

from . import __version__


class krequest(object):
    def __init__(self, return_json=True, global_headers=[]):
        self.headers = {
            "User-Agent": "WeebAPI.py/{} (Github: AndyTempel) KRequests/alpha "
                          "(Custom asynchronous HTTP client)".format(__version__),
            "X-Powered-By": "{}".format(sys.version)
        }
        self.return_json = return_json
        for name, value in global_headers:
            self.headers.update({
                name: value
            })

    async def _proc_resp(self, response):
        if self.return_json:
            try:
                return await response.json()
            except Exception:
                print(traceback.format_exc())
                print(response)
                return {}
        else:
            return await response.text()

    async def get(self, url, params=None, headers=None, verify=True):
        headers = headers or {}
        headers.update(self.headers)
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=verify)) as session:
            async with session.get(url, params=params, headers=headers) as resp:
                return await self._proc_resp(resp)

    async def delete(self, url, params=None, headers=None, verify=True):
        headers = headers or {}
        headers.update(self.headers)
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=verify)) as session:
            async with session.delete(url, params=params, headers=headers) as resp:
                return await self._proc_resp(resp)

    async def post(self, url, data=None, json=None, headers=None, verify=True):
        headers = headers or {}
        headers.update(self.headers)
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=verify)) as session:
            if json is not None:
                async with session.post(url, json=json, headers=headers) as resp:
                    return await self._proc_resp(resp)
            else:
                async with session.post(url, data=data, headers=headers) as resp:
                    return await self._proc_resp(resp)
