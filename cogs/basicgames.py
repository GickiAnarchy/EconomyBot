import nextcord
import random
from nextcord.ext import commands
from data import bankfunctions

class BasicGames(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases = ["flip", "cf"], description = "Coin <amount to bet> <'Heads' or 'Tails'")
    @commands.guild_only()
    async def coin(self, ctx, bet = 0, coincall = "heads"):
        """Flips a coin.

        Args:
            ctx (_type_): Context of the command usage
            bet (int, optional): _description_. Defaults to 0.
            coincall (str, optional): _description_. Defaults to "heads".
        """
        ca = await bankcommands.canAfford(user, bet)
        if ca == false:
            await ctx.send(f"You can't afford ${str(bet)}!")
            return
        self.user = ctx.author
        seq = ["heads", "tails"]
        ran = random.choice(seq)
        pick = coincall.lower()
        print(f"{str(ran)}")
        
        if str(ran) == pick:
            await bankfunctions.update_bank(self.user, bet)
            print(f"{self.user.name} won.")
        else:
            await bankfunctions.update_bank(self.user, bet)
            print(f"{self.user.name} lost.")



def setup(client):
    client.add_cog(BasicGames(client))