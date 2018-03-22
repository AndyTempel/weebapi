# weebapi

![img](https://img.shields.io/pypi/v/weebapi.svg) ![img2](https://img.shields.io/pypi/pyversions/weebapi.svg)

## Pluggable Weeb.sh API Wrapper

### How to install:

**1. With pip**

`pip install -U weebapi`

**2. From GitHub**

`pip install -U git+https://github.com/AndyTempel/weebapi#egg=weebapi`

### Usage:

**With bot integration:**

```python
from discord.ext.commands import Bot
from weebapi import Client

bot = Bot(command_prefix="+")
Client.pluggable(bot=bot, api_key="VeryNiceKey123")

@bot.command()
async def owo(ctx):
    image = await bot.weebsh.get_random(image_type="owo")
    await ctx.send(str(image))

>>> https://cdn.weeb.sh/images/SklMOkytDb.jpeg
```

**or without bot integration:**

```python
from discord.ext.commands import Bot
from weebapi import Client

bot = Bot(command_prefix="+")
weeb = Client(api_key="VeryNiceKey123")

@bot.command()
async def owo(ctx):
    image = await weeb.get_random(image_type="owo")
    await ctx.send(str(image))

>>> https://cdn.weeb.sh/images/SklMOkytDb.jpeg
```
