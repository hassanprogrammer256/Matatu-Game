
class Player:
    def __init__(self,window,name):
        self.window =window
        self.name = name
        self.hand = []

    def pick_card(self,deck): #pick a card from deck
        card = deck.pick_card()
        if card:
            self.hand.append(card)
    def play_card(self,index):
        return self.hand.pop(index)
    def has_valid_card(self,top_card):
        return any(card.matches(top_card) for card in self.hand)
    

class AI_Player(Player):
    def play_card(self):
        if self.hand:
            card_to_play = self.hand[0]  # Naive AI
            self.play_card(card_to_play)
            return card_to_play
        return None

    # def check_cards(self,top_card):
    #     if self.hand:
    #         correct_cards = []
    #         for card in self.hand:
    #             if card.matches(top_card):
    #              correct_cards.append(card)
    #         return correct_cards

        
    
