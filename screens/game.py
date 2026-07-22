import pygame

def game(screen, bg_main, sprites):
    screen.blit(bg_main, (0, 0))
    sprites.draw(screen)