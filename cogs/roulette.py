"""Discord Bot Cog - Casino : Roulette"""
import nextcord
from nextcord.ext import commands
import os
import pickle
import random
from data import bankfunctions


class RouletteCog(commands.Cog):
	def __init__(self, client):
		self.client = client
		


def setup(client):
    client.add_cog(RouletteCog(client))


class Roulette:

    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

    def __init__(self, user: nextcord.User):
        self.user = user

    #   lets roll the roulette wheel
    def rollTheRouletteWheel(self):
        print('--- Spinning the '+self.rouletteStyle+' roullete wheel ---')
        #   the picked bet must be an interger between -1 and 36 (00,0,1,2,3.....)
        theRoll = random.randint(-1,36)
        #    add the roll to the history     
        self.rollHistory.append(theRoll)
        print('The ball has landed on '+str(theRoll)+' '+str(self.colorHistory[-1]))
        return(theRoll) 