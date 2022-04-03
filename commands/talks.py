from discord.ext import commands
import discord


class Talks(commands.Cog):
    """Talks with user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kingbot", help="Comandos e outras mensagens")
    async def king_bot_helper(self, ctx):
        MSG = \
    """
    Comandos:
    !agenda - mostra agenda da liga dos clubes
    !add_agenda - Passe os horarios que você pode jogar. Ex: 14 15 16
    !del_agenda - Passe os horarios que você quer remover. Ex: 14 15 16
    Se tiver ideias pra me melhorar ou encontrar problemas, fale com o badman
    """
        await ctx.send(MSG)

    @commands.command(name="segredo", help="Envia um segredo no privado. Não requer argumento")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Mensagem privada")
        except discord.errors.Forbidden:
            await ctx.send(
                "Habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)"
            )


def setup(bot):
    bot.add_cog(Talks(bot))
