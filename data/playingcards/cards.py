#cards.py
import os
import random


image_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "images"))


class Card():
    """Single playing card class"""

    back = image_folder + "/back.png"

    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, s, v, hidden = True):
        """suit + value are ints"""
        self.value = v
        self.suit = s
        self.name = f"{self.suits[self.suit]}_{self.values[self.value]}"
        self.imagename = f"{self.name}.png"
        self.image = image_folder + f"/{self.imagename}"
        self.hidden = hidden


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


    @property
    def Image(self):
            return self.image