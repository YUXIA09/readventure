import pygame

def play(screen, bg_supermarket, sprites, level):
    screen.blit(bg_supermarket, (0, 0))
    sprites.draw(screen)