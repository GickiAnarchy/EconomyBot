from cards.card_standard import *
import time
from PIL import Image, ImageTk
import tkinter as tk


class HighLow:
    """
    
    """
    def __init__(self):
        self.deck = Deck()
        self.player = "Player"
        self.opp = "AI"
        self.score = 0
    
    
    def pullCard(self):
        self.pcard = self.deck.drawCard()
        self.ccard = self.deck.drawCard()
        
        print(f"{repr(self.pcard)} VS {repr(self.ccard)}")

        if self.pcard > self.ccard:
            print("Player wins")
            self.score += 1          
        else:
            print("Computer wins")
            self.score -= 1
        
        print(f"{str(self.deck.cards.__len__())} cards left\n\n")

    def getScore(self):
        return self.score
