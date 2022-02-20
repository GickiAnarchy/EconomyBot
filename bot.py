import nextcord
from nextcord.ext import commands
import os
from private import botprivate
from data import bankfunctions


intents = nextcord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = ".!", intents = intents)

toke = botprivate.TokenClass()

@client.command()
async def loadcog(ctx, cog):
    
    client.load_extension(f"{cog}")
    await ctx.send(f"{cog} has been loaded!")

@client.command()
async def unloadcog(ctx, cog):
    client.unload_extension(f"cogs.{cog}")

@client.event
async def on_ready():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Game("*WIP* Economy Bot -  '.!'"))
    
@client.command()
@commands.has_role("Cool Kid")
async def clr(ctx, amount = 0):
		await ctx.channel.purge(limit=amount)

@clr.error
async def clr_error(ctx, error):
		if isinstance(error, commands.CheckFailure):
			await ctx.send("`You dont have permissions to run this command.`")


#Run the f'n thing!
client.run(toke.getToken())