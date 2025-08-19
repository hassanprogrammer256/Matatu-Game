import random
from Card import *

class Deck():
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    STANDARD_DICT = {'Ace':1, '2':2, '3':3, '4':4, '5':5,'6':6,'7':7, '8': 8, '9':9, '10':10,'Jack':11,'Queen':12, 'King':13}

    def __init__(self, window, rankValueDict=STANDARD_DICT):
        self.Deck = []
        for suit in Deck.SUIT_TUPLE:
            for rank, value in rankValueDict.items():
                ocard = Card(window, rank, suit, value)
                self.Deck.append(ocard)
        self.playing_deck = []
        self.shuffle()

    def shuffle(self):
        self.playing_deck = self.Deck.copy()
        random.shuffle(self.playing_deck)
        return self.playing_deck

    def pick_card(self):
        if self.playing_deck:
            return self.playing_deck.pop()