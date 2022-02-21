import nextcord
from nextcord.ext import commands
import os
import random
from data import bankfunctions

class BasicInteraction(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["rob"])
	@commands.guild_only()
	async def steal(self, ctx, victim = None):
		self.user = ctx.author
		self.victim = victim
		schance = random.randint(1, 100)
		self.change = 0
		
		#User ends up losing money
		if schance < 20:
			print("<20")		
		#User is not successful in the robbery attempt
		elif schance < 68:
			print("<68")
		#User was successful at the robbery
		elif schance < 95:
			print("<95")		
		#User robs tge victim for ALOT
		elif schance <= 100:
			print("<=100")
		


	@commands.command(aliases = ["donate", "charity"])
	@commands.guild_only()
	async def givecash(self, ctx, target = None, amount = 0):
		self.user: nextcord.User= ctx.author
		self.user_account = await bankfunctions.get_bank_data(self.user)
		self.user_wallet = self.user_account[1]
		self.target: nextcord.User = target
		if self.target == None:
			self.target = ctx.author
		else:
			self.target_account = await bankfunctions.get_bank_data(self.target)
			self.target_wallet = self.target_account[1]
		
		if self.user == self.target:
			await ctx.send("Uhhh, wtf are you tryimg to do?/nAnyways....")			
		if self.user_wallet < int(amount):
			await ctx.send("You do not have that much money to give away!")
			return
		if int(amount) < 0:
			await ctx.send("Invalid amount. Can't give a negative amoint!")
			return

		await bankfunctions.update_bank(self.user, -1 * int(amount))
		await bankfunctions.update_bank(self.target, int(amount))
		await ctx.send(f"{self.target.mention} just recieved ${str(amount)} from {self.user.name}.")



def setup(client):
    client.add_cog(BasicInteraction(client))
