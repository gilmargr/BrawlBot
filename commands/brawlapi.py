import os
import requests

from discord.ext import commands
class BrawlApi(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="membros", help="Lista membros do clube"
    )
    async def clubsapi(self, ctx):
        try:
          my_secret = os.environ['BRAWLAPI_TOKEN']
          head = {'Authorization': 'Bearer {}'.format(my_secret)}
          
          response = requests.get(
                f"https://api.brawlstars.com/v1/clubs/%23GCVJC92P/members",headers=head
          )

          print(response)
          data = response.json()
          members = data.get("items")
          print("\n\n\nMembros\n")
          print(members)
          members_str = ""
          for member in members:
            members_str += member["name"] + "\n"

          await ctx.send(f"Membros:\n{members_str}")
         
        except Exception as error:
            await ctx.send("Ops... Deu algum erro!")
            print(error)

def setup(bot):
    bot.add_cog(BrawlApi(bot))
