# ====REQUIRED MODULES AND PACKAGES====
import pygwidgets
from Constants import *
import random
# ====CARD CLASS========
class Card():
    def __init__(self,window,rank,suit,value):
        self.window = window
        self.suit = suit
        self.rank = rank
        self.value = value
        self.cardName = f'{rank} of {suit}'
        self.img = f'images/{self.cardName}.png'
        self.card = pygwidgets.Image(window,(0,0),self.img)
# -------DRAWING A CARD---------------
    def draw(self):
             self.card.draw()
# -------SETTING LOCATION  OF A CARD----------
    def setLoc(self,loc):
        self.card.setLoc(loc)
# -------CLOSING A RECENTLY OPENED CARD---------------
    def hide(self):
        self.card.replace(BACK_OF_CARD_IMAGE) 
# -------OPENING A RECENTLY CLOSED CARD---------------
    def show(self):
        self.card.replace(self.img) 
# -------CHECKING FOR A CLICK EVENT ON A  CARD---------------
    def card_clicked(self,click):
         rect = self.card.getRect()
         clicked=rect.collidepoint(click)
         return clicked
# ----ROTATING THE CARD HORIZONTALY======
    def rotate(self,angle):
        self.card.rotateTo(angle)
# ---TERMINATING A CARD----------
    def matches(self, other):
         return self.rank == other.rank or self.suit == other.suit
    
    
