import pygame
from levels.level1 import *
from levels.level2 import *
from levels.level3 import *

small_font = pygame.font.Font(None, 16)
def play(screen, bg_supermarket, sprites, font, level):
    screen.blit(bg_supermarket, (0, 0))
    sprites.draw(screen)

    text = font.render("Press ESC to leave. Walk into aisles to collect items", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)

    if level == 1:
        level1(screen, small_font)
    elif level == 2:
        level2(screen, small_font)
    elif level == 3:
        level3(screen, small_font)

def check_items(shopping_cart):
    for item in itemsLevel1:
        if item not in shopping_cart:
            return False
    return True