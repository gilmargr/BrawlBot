import datetime
from replit import db
from discord.ext import commands, tasks


class Dates(commands.Cog):
    """Work with dates"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    def erase_schedules():
        for key in db.keys():
          del db[key]
  
    @tasks.loop(minutes=30)
    async def current_time(self):
        ...
        now = datetime.datetime.now()
        channel = self.bot.get_channel(958393680014766110)

      . # Apaga a agenda de Segunda, Quinta e Sabado após as 18
        if(now.hour == 18 and now.minute < 30 
           and (now.weekday() == 4 or now.weekday() == 6 or now.weekday() == 0)):
            self.erase_schedules()
            await channel.send("Agenda apagada! Agendem os próximos horarios!")
        else:
          print("Não é hora" )

def setup(bot):
    bot.add_cog(Dates(bot))
