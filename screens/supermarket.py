import pygame
from levels.level1 import *
from levels.level2 import *
from levels.level3 import *

#Create font for which the texts will be shown.
small_font = pygame.font.Font(None, 16)
def play(screen, bg_supermarket, sprites, font, level):
    #Draw supermarket background draw all sprites.
    screen.blit(bg_supermarket, (0, 0))
    sprites.draw(screen)

    #Render the text in top left corner.
    text = font.render("Press ESC to leave. Walk into aisles to collect items", True, (255, 255, 255))
    text_rect = text.get_rect()
    screen.blit(text, text_rect)

    #Check which level it is to run the respective code.
    if level == 1:
        level1(screen, small_font)
    elif level == 2:
        level2(screen, small_font)
    elif level == 3:
        level3(screen, small_font)

def check_items(shopping_cart, itemsLevel):
    #Check items in players shopping cart against the required items
    for item in itemsLevel:
        if item not in shopping_cart:
            return False
    return True