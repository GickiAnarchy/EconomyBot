import nextcord
import random
from nextcord.ext import commands
from data import bankfunctions
from data.playingcards import * 


class CardGames(command.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def highcard(self, ctx):
        self.player = ctx.author
        await bankfunctions.open_bank(self.player)
        users = await bankfunctions.get_bank_data(self.player)
        self.wallet_amt = users[1]
        
        await ctx.send(f"How much do you want to wager?  Max:${self.wallet_amt}")

        def is_correct(m):
            return m.author == ctx.author and m.content.isdigit()

        try:
            self.wager = await bot.wait_for('message', check=is_correct, timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.send(f'Sorry, I can't wait forever.')'
            
            if int(self.wager) > self.wallet_amt:
                await ctx.send(f"You can't afford ${str(self.wager)}")
                return
            
            self.deck = data.playingcards.Deck()
            self.com = self.deck.drawCard()
            self.card = self.deck.drawCard()
            
            





def setup(client):
    client.add_cog(CardGames(client))