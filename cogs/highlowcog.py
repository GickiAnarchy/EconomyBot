import nextcord
from nextcord.ext import commands
from references.cards.card_standard import *



class HighLowCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.guild_only()
    async def highlow(self, ctx):
        





def setup(client):
    client.add_cog(HighLowCog(client))