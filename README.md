# weebapi

![img](https://img.shields.io/pypi/v/weebapi.svg) ![img2](https://img.shields.io/pypi/pyversions/weebapi.svg)

**Pluggable Weeb.sh API Wrapper**

```python
from discord.ext.commands import Bot
from weebapi import Client

bot = Bot(command_prefix="+")
weeb = Client.pluggable(bot=bot, api_key="VeryNiceKey123")

image = await bot.weebsh.get_random(tags="owo")
print(str(image))
>>> https://cdn.weeb.sh/images/SklMOkytDb.jpeg
```

**or without bot integration:**

```python
from discord.ext.commands import Bot
from weebapi import Client

bot = Bot(command_prefix="+")
weeb = Client(api_key="VeryNiceKey123")

image = await weeb.get_random(tags="owo")
print(str(image))
>>> https://cdn.weeb.sh/images/SklMOkytDb.jpeg
```
