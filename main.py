import os
from discord.ext import commands
import keep_alive

bot = commands.Bot("!")


def load_cogs(bot):
    bot.load_extension("manager")
    bot.load_extension("tasks.dates")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")


load_cogs(bot)

keep_alive.keep_alive()

TOKEN = os.environ['BOT_TOKEN']
bot.run(TOKEN)
