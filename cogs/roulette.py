"""
Discord Bot Cog
Casino : Roulette
"""
import nextcord
from nextcord.ext import commands
import os
import random
from data import bankfunctions


class Roulette(commands.Cog):
	def __init__(self, client):
		self.client = client

	


def setup(client):
    client.add_cog(Roulette(client))
