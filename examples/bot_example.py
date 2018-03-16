from discord.ext.commands import Bot
from weebapi import Client

bot = Bot(command_prefix="+")
Client.pluggable(bot=bot, api_key="YourAmazingToken123")


@bot.command()
async def owo(ctx):
    image = await bot.weebsh.get_random(image_type="owo")
    await ctx.send(str(image))


bot.run("YourDiscordBotToken123")
