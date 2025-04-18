#  Game class
from Deck import *
from Player import *
from Card import *
from Constants import *


class Game:
    def __init__(self, window,player_name):
        self.window = window
        self.current_player_index = 0
        self.human = Player(window,player_name)
        self.computer = AI_Player(window,"AI")
        self.players = [self.human,self.computer]
        self.oDeck = Deck(self.window)  
        self.score = 100
        self.played_cards = []
        self.cardXPositionsList = []
        self.BoardcardXPositionsList = []
        self.BoardcardYPositionsList = 220
        thisLeft = CARDS_LEFT
        dist_x = random.choice([400,450])
        self.angles = []
        self.player_hand = []
        self.cards_on_board = []
        for cardNum in range(0,30):
            self.cardXPositionsList.append(thisLeft)
            self.BoardcardXPositionsList.append(dist_x)
            thisLeft = thisLeft + CARD_OFFSET
            dist_x = dist_x + random.randint(-10,10)
            self.angles.append(random.randint(0,360))
        self.start_Game()
    
# ---STARTING THE GAME RESETS---------------
    def start_Game(self):
        self.players[0].hand = []
        self.players[1].hand = []
        self.oDeck.shuffle()
        for _ in range(NCARDS):
            for player in self.players:
                player.pick_card(self.oDeck)
# ----DRAWING EACH PLAYER`S HAND-------------`
    def draw(self):
        for player in (self.players):
            if isinstance(player , AI_Player):
               for index,card in enumerate(player.hand):
                    card.setLoc((self.cardXPositionsList[index],CARDS_TOP)) 
                    # card.hide()
                    card.draw()
            else:
                for index,card in enumerate(player.hand):
                    card.setLoc((self.cardXPositionsList[index],CARDS_DOWN))
                    card.draw()
                    self.player_hand.append(card)
            
            for index,card in enumerate(self.played_cards):
                card.setLoc((self.BoardcardXPositionsList[index],self.BoardcardYPositionsList))
                card.rotate(self.angles[index])
                card.draw()
                self.cards_on_board.append(card)

            

# ----EACH PLAYER PLAYING A TURN---------

    def played(self,card):
        if self.current_player_index == 0:
           if self.human.has_valid_card(card):
               self.human.play_card(self.human.hand.index(card))
               self.current_player_index = 1
               self.played_cards.append(card)
          
    def comp(self):
        if self.current_player_index == 1:
           corr_cards = []
           if self.computer.has_valid_card(self.played_cards[-1]):
               for card in self.computer.hand:
                    if card.matches(self.played_cards[-1]):
                        corr_cards.append(card)
                        break
           if len(corr_cards) >= 1:
                    self.computer.hand.remove(corr_cards[0])
                    card.show()
                    self.played_cards.append(card)
                    
        self.current_player_index = 0
            #    self.computer.play_card(self.computer.hand.index(card))
            #    self.current_player_index = 0
            #    self.played_cards.append(card)
            #    self.draw()
            #    print('yes')




    

            
        

