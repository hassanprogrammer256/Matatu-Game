import pygame
import math
from Constants import *

class Card():
    def __init__(self, window, rank, suit, value, player=None):
        self.window = window
        self.player = player
        self.suit = suit
        self.rank = rank
        self.value = value
        self.cardName = f'{rank} of {suit}'
        self.img = f'images/{self.cardName}.png'
        self.back_img = BACK_OF_CARD_IMAGE
        self.card = pygwidgets.Image(window, (0, 0), self.back_img)
        self.animated_card = None
        self.current_pos = pygame.math.Vector2(0, 0)
        self.target_pos = self.current_pos
        self.is_animating = False
        self.animation_start_time = 0
        self.animation_duration = 2  # seconds
        self.start_pos = self.current_pos
        self.end_pos = self.current_pos
        self.start_angle = 0
        self.end_angle = 0

    def draw(self):
        self.card.draw()

    def setLoc(self, loc, override_animation=False):
        if not self.is_animating or override_animation:
            self.card.setLoc(loc)
            self.current_pos = pygame.math.Vector2(loc[0] + self.card.getRect().width / 2,
                                                loc[1] + self.card.getRect().height / 2)

    def hide(self):
        self.card.replace(self.back_img)

    def show(self):
        self.card.replace(self.img)

    def card_clicked(self, click_pos):
        rect = self.card.getRect()
        return rect.collidepoint(click_pos)

    def rotate(self, angle):
        self.card.rotateTo(angle)

    def animate_move(self, new_pos, duration=1.5, max_rotation=360):
        self.is_animating = True
        self.animation_start_time = pygame.time.get_ticks()
        self.animation_duration = duration * 1000  # ms
        self.start_pos = self.current_pos
        self.end_pos = pygame.math.Vector2(new_pos)
        self.start_angle = 0
        self.end_angle = max_rotation

    def update(self):
        if self.is_animating:
            now = pygame.time.get_ticks()
            elapsed = now - self.animation_start_time
            t = min(elapsed / self.animation_duration, 1)

            # Interpolated position
            new_x = (1 - t) * self.start_pos.x + t * self.end_pos.x
            new_y = (1 - t) * self.start_pos.y + t * self.end_pos.y
            self.current_pos = pygame.math.Vector2(new_x, new_y)

            # Rotate
            angle = (1 - t) * self.start_angle + t * self.end_angle
            self.rotate(angle)

            # Update the image position to current_pos
            rect = self.card.getRect()
            rect.center = (self.current_pos.x, self.current_pos.y)
            self.card.setLoc(rect.topleft)

            if t >= 1:
                self.is_animating = False
                self.rotate(0)
                rect = self.card.getRect()
                rect.center = (self.end_pos.x, self.end_pos.y)
                self.card.setLoc(rect.topleft)

    def matches(self, other):
        return self.rank == other.rank or self.suit == other.suit