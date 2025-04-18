# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from Game import Game
from Constants import *

# 3 - Initialize the world
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Load assets: image(s), sounds,  etc.
background = pygwidgets.Image(window, (0, 0),'images/background.png')
Boardbackground = pygwidgets.Image(window, (50, 157),'images/boardBg.png')

# ........BUTTONS...........
quitButton = pygwidgets.TextButton(window, (20, 530),'Quit', width=100, height=45)#the quit button
deck_btn = pygwidgets.CustomButton(window,(880,230),BACK_OF_CARD_IMAGE)

# =====SOUNDS SETTINGS======

    
# ---INSTANCES---------------
oGame = Game(window,"hassan")
oGame.start_Game()
# 6 - Loop forever
while True:
    for event in pygame.event.get():
        if ((event.type == QUIT) or
            ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
            (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP :
            for card in oGame.player_hand:
               if card.card_clicked(event.pos):
                    oGame.played(card)
#   =====DRAWING THE INTERFACES===========
    background.draw() #background
    Boardbackground.draw() # board
    quitButton.draw()
    oGame.draw()
    deck_btn.draw()
    # pygame.time.wait(1000)
    oGame.comp()        
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
