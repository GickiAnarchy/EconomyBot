from random import shuffle
import os
from PIL import Image, ImageTk
import tkinter as tk

class Card:
    """ Class for a single basic playing card

    """
    suits = ["spades", "hearts", "diamonds", "clubs"]
    
    values = [None, None,"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    file_path = r"cards/cardsPNG/"

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s
        self.imagefile = f"{self.file_path}{self.suits[self.suit]}_{self.values[self.value].lower()}.png"
        

    def __lt__(self, c2):
        """Handles the 'less than' operator (<)"""
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        """Handles the 'greater than' operator (>)"""
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        """Returns a string format of the object"""
        v = self.values[self.value] +\
            " of " + \
            self.suits[self.suit]
        return v
    
    def imgPath(self):
        """Returns the PNG file image of the card"""
        print(f"Getting {self.imagepath}....")
        return self.imagefile


class Deck:
    """ Class of 52 Card() to create a full deck.

    """
    def __init__(self):
        self.cards = []
        
    def createDeck(self):
        for i in range(2, 15):
            for j in range(4):
                crd = Card(i, j)
                self.cards.append(crd)
        self.shuffle()

    def shuffle(self):
        if len(self.cards) == 0:
            return
        shuffle(self.cards)
        print(f"Shuffling {str(len(self.cards))} cards..")

    def drawCard(self):
        if len(self.cards) == 0:
            return
        pulled = self.cards.pop()
        print(f"Pulled card:\n{pulled}")
        return 


####################################################
####################################################
####################################################

