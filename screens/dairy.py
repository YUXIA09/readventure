from rects import dairyAisleItems
from settings import WIDTH, HEIGHT
import pygame
import time

#Code is really similar to other aisles, check bread.py for explanations.
def dairyAisle(screen, bg_dairy, font, pos, click):
    screen.blit(bg_dairy, (0, 0))

    text = font.render("Press ESC to leave. Click on items to add them to your cart", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)

    added_items = []
    if click:
        for key, value in dairyAisleItems.items():
            if value.collidepoint(pos):
                added_items.append(key) 
                text = font.render(f"{key} added to cart!", True, (255, 255, 255))
                text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
                screen.blit(text, text_rect)
                pygame.display.flip()
                time.sleep(0.3)

    return added_items
            