from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument
from discord.ext import commands


class Manager(commands.Cog):
    """Manage the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logado como {0}'.format(self.bot.user))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        msg = message.content
        username = message.author.display_name

        if "bot" in msg and not "!kingbot" in msg:
            await message.channel.send(f"E ai {username}! Chamou? Escreve !kingbot para saber o que sei fazer")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send(
                "Favor enviar todos os Argumentos. Digite !help para ver os parâmetros de cada comando"
            )
        elif isinstance(error, CommandNotFound):
            await ctx.send(
                "O comando não existe. Digite !help para ver todos os comandos"
            )
        else:
            raise error


def setup(bot):
    bot.add_cog(Manager(bot))
