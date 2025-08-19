import pygame
from pygame.locals import *
import sys
import pygwidgets
from Game import *
from Constants import *
import time

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

background = pygwidgets.Image(window, (0, 0), 'images/background.png')
Boardbackground = pygwidgets.Image(window, (50, 157), 'images/boardBg.png')

quitButton = pygwidgets.TextButton(window, (20, 530), 'Quit', width=100, height=45)
deck_btn = pygwidgets.CustomButton(window, (880, 230), BACK_OF_CARD_IMAGE)

oGame = Game(window, "hassan")

while True:
    for event in pygame.event.get():
        if ((event.type == QUIT) or
            (event.type == KEYDOWN and event.key == K_ESCAPE) or
            (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONUP:
            if oGame.state == 'player_turn':
                oGame.handle_click(event.pos)

    # Update game state
    oGame.update()

    # Drawing
    background.draw()
    Boardbackground.draw()
    quitButton.draw()
    oGame.draw()
    deck_btn.draw()

    # Handle turn transitions
    if oGame.state == 'player_turn':
        pass
    elif oGame.state == 'ai_turn':
        # AI turn triggered inside update
        pass
    elif oGame.state == 'waiting':
        # Waiting handled in update
        pass
    elif oGame.state == 'animating':
        pass

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)