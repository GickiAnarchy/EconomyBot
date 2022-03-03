from card_standard import *
import time

class HighLow:
    """
    
    """
    def __init__(self):
        self.deck = Deck()
        self.player = "Player"
        self.opp = "AI"
        self.score = 0
    
    def drawCard(self):
        self.pcard = self.deck.rm_card()
        self.ccard = self.deck.rm_card()
        
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
            
        
        
        
        
hl = HighLow()


while len(hl.deck.cards) >= 2:
    hl.drawCard()
    time.sleep(2)

if hl.getScore() > 0:
    print("\nPLAYER WINS!!!")
else:
    print("\nCOMPUTER WINS!!!")
print(f"{str(hl.getScore())}")