# weebapi

![img](https://img.shields.io/pypi/v/weebapi.svg) ![img2](https://img.shields.io/pypi/pyversions/weebapi.svg)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FAndyTempel%2Fweebapi.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FAndyTempel%2Fweebapi?ref=badge_shield)

## Pluggable Weeb.sh API Wrapper

### Documentation

**All available documentation can be found here:** [weebapi.readthedocs.io](https://weebapi.readthedocs.io)

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


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FAndyTempel%2Fweebapi.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FAndyTempel%2Fweebapi?ref=badge_large)