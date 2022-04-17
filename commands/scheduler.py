from discord.ext import commands
import discord
from replit import db


class Scheduler(commands.Cog):
    """Scheduler"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="add_agenda", help="Adiciona os horários (horas cheias) Ex: !add_agenda 9 12 15 18")
    async def add_schedule(self, ctx, *hours):
        for hour in hours:
            player = ctx.author.display_name
            if hour.isdigit() and int(hour) < 24 and int(hour) >= 0:
                if hour in db.keys():
                    players = db[hour]
                    players.append(player)
                    db[hour] = players
                else:
                    db[hour] = [player]
                await ctx.channel.send("Adicionado {1} as {0} horas".format(hour, player))
            else:
                await ctx.channel.send(
                    "Parametros inválidos. Passe uma hora válida")

    @commands.command(name="del_agenda", help="Remove horários. Use horas cheias. Ex: !del_agenda 9 12 15 18")
    async def del_schedule(self, ctx, *hours):
        for hour in hours:
            player = ctx.author.display_name
            if hour.isdigit() and int(hour) < 24 and int(hour) >= 0:
                players = db[hour]
                players.remove(player)
                if len(players) > 0:
                    db[hour] = players
                else:
                    del db[hour]
                await ctx.channel.send("Removido {1} das {0} horas".format(hour, player))
            else:
                await ctx.channel.send("Parametros inválidos. Passe uma hora válida")


    @commands.command(name="apagar_agenda")
    async def erase_schedule(self, ctx):
        if ctx.author.id == 958096430826926080:
            for key in db.keys():
                del db[key]
            await ctx.channel.send(f"{ctx.author.name} apagou todos os registros")
        else:
            await ctx.channel.send(f"{ctx.author.name}, permissão negada")


    @commands.command(name="agenda")
    async def send_league_schedule(self, ctx):
        teams = 'Hora - Jogadores'
        for key in sorted(db.keys()):
            teams += "\n{0}hs - {1.value}".format(key, db[key])
        await ctx.send(teams)

def setup(bot):
    bot.add_cog(Scheduler(bot))
