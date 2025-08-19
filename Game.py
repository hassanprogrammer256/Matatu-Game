from Deck import *
from Player import *
from Card import *
from Constants import *
import time

class Game:
    def __init__(self, window, player_name):
        self.window = window
        self.current_player_index = 0
        self.human = Player(window, player_name)
        self.computer = AI_Player(window, "AI")
        self.players = [self.human, self.computer]
        self.oDeck = Deck(self.window)
        self.score = 100
        self.played_cards = []
        self.cardXPositionsList = []
        self.BoardcardXPositionsList = []
        self.BoardcardYPositionsList = 220
        self.angles = []
        self.player_hand = []
        self.cards_on_board = []

        self.state = 'player_turn'  # 'player_turn', 'ai_turn', 'animating', 'waiting'
        self.delay_start_time = None
        self.delay_duration = 1.0  # seconds

        # Initialize positions and angles
        thisLeft = CARDS_LEFT
        dist_x = random.choice([400, 450])
        for _ in range(30):
            self.cardXPositionsList.append(thisLeft)
            self.BoardcardXPositionsList.append(dist_x)
            thisLeft += CARD_OFFSET
            dist_x += random.randint(-10, 10)
            self.angles.append(random.randint(0, 360))
        self.start_Game()

    def start_Game(self):
        self.human.hand = []
        self.computer.hand = []
        self.oDeck.shuffle()

        for _ in range(NCARDS):
            for player in self.players:
                player.pick_card(self.oDeck)

    def draw(self):
        # Draw human hand
        for index, card in enumerate(self.human.hand):
            card.setLoc((self.cardXPositionsList[index], CARDS_DOWN))
            card.show()
            card.draw()

        # Draw AI hand
        for index, card in enumerate(self.computer.hand):
            card.setLoc((self.cardXPositionsList[index], CARDS_TOP))
            card.draw()

        # Draw played cards
        for index, card in enumerate(self.played_cards):
            card.setLoc((self.BoardcardXPositionsList[index], self.BoardcardYPositionsList))
            card.rotate(self.angles[index])
            card.draw()

    def handle_click(self, pos):
        if self.state == 'player_turn':
            for card in self.human.hand:
                if card.card_clicked(pos):
                    self.played(card)
                    self.start_player_move(card)
                    break

    def played(self, card):
        if self.current_player_index == 0:
            if self.human.has_valid_card(card):
                self.human.play_card(self.human.hand.index(card))
                self.played_cards.append(card)
                self.current_player_index = 1
                self.state = 'waiting'
                self.delay_start_time = time.time()

    def start_player_move(self, card):
        index = len(self.played_cards) - 1
        target_x = self.BoardcardXPositionsList[index]
        target_y = self.BoardcardYPositionsList
        card.animate_move((target_x, target_y))
        print(target_x,target_y)
        self.state = 'animating'

    def ai_move(self):
        if self.computer.hand:
            last_played = self.played_cards[-1] if self.played_cards else None
            valid_card = None
            for c in self.computer.hand:
                if not last_played or c.matches(last_played):
                    valid_card = c
                    break
            if valid_card:
                self.computer.hand.remove(valid_card)
                self.played_cards.append(valid_card)
                self.start_computer_move(valid_card)
                self.current_player_index = 0
                self.state = 'waiting'
                self.delay_start_time = time.time()
            else:
                self.computer.pick_card(self.oDeck)

    def start_computer_move(self, card):
        index = len(self.played_cards) - 1
        target_x = self.BoardcardXPositionsList[index]
        target_y = self.BoardcardYPositionsList
        print(target_x,target_y)
        card.animate_move((target_x, target_y))
        card.show()
        self.state = 'animating'

    def update(self):
        if self.state == 'animating':
            for card in self.played_cards:
                card.update()
            if not any(card.is_animating for card in self.played_cards):
                self.state = 'waiting'
                self.delay_start_time = time.time()

        elif self.state == 'waiting':
            if self.delay_start_time and (time.time() - self.delay_start_time >= self.delay_duration):
                self.delay_start_time = None
                if self.current_player_index == 0:
                    self.state = 'player_turn'
                else:
                    self.state = 'ai_turn'
                    self.ai_move()

        elif self.state == 'ai_turn':
            self.ai_move()