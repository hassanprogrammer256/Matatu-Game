class Player:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.hand = []

    def pick_card(self, deck):
        card = deck.pick_card()
        if card:
            self.hand.append(card)
        return self.hand

    def play_card(self, index):
        return self.hand.pop(index)

    def has_valid_card(self, top_card):
        return any(card.matches(top_card) for card in self.hand)

class AI_Player(Player):
    def play_card(self):
        if self.hand:
            card_to_play = self.hand[0]  # naive AI
            self.hand.remove(card_to_play)
            return card_to_play
        return None