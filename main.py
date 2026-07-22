import pygame

from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

from assets import *
from rects import *
from sprites.player import Player
from screens.welcome import welcome
from screens.game import game
from screens.supermarket import play
from screens.dairy import dairyAisle
from screens.bread import breadAisle
from screens.cleaning import cleaningAisle
from screens.fruit import fruitAisle
from screens.meat import meatAisle
from screens.vegetables import vegetablesAisle

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

mainPlayer = Player(character_1, character_2, 225, 135)
sprites = pygame.sprite.Group()
sprites.add(mainPlayer)

def check_click(events):
    click = False
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

    return click

def exit(state, events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "supermarket-screen", False

    return state, True

while running:
    pygame.display.flip()
    clock.tick(60)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if state == "welcome-screen":
        state = welcome(screen, bg_welcome, font, events)

    if state == "main-screen":

        if not resetPos:
            mainPlayer.rect.x = 225
            mainPlayer.rect.y = 135
            resetPos = True
        
        game(screen, bg_main, sprites)

        mainPlayer.rect.clamp_ip(screen.get_rect())
        keys = pygame.key.get_pressed()
        mainPlayer.move(keys)

        if mainPlayer.rect.colliderect(supermarket):
            state = "supermarket-screen"
            resetPos = False

    if state == "supermarket-screen":

        if not resetPos:
            mainPlayer.rect.x = 750
            mainPlayer.rect.y = 110
            resetPos = True

        keys = pygame.key.get_pressed()
        mainPlayer.move(keys)
        mainPlayer.rect.clamp_ip(supermarketBounds)

        feet = (mainPlayer.rect.centerx, mainPlayer.rect.bottom - 20)
        play(screen, bg_supermarket, sprites, font, supermarket_level)

        if dairy.collidepoint(feet):
            state = "dairy-aisle"

        if bread.collidepoint(feet):
            state = "bread-aisle"

        if fruit.collidepoint(feet):
            state = "fruit-aisle"

        if cleaning.collidepoint(feet):
            state = "cleaning-aisle"

        if vegetables.collidepoint(feet):
            state = "vegetables-aisle"

        if meat.collidepoint(feet):
            state = "meat-aisle"

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "main-screen"
                    resetPos = False

    if state == "dairy-aisle":
        dairyAisle(screen, bg_dairy, font, pygame.mouse.get_pos(), check_click(events))
        state, resetPos = exit(state, events)

    if state == "bread-aisle":
        breadAisle(screen, bg_bread, font, pygame.mouse.get_pos(), check_click(events))
        state, resetPos = exit(state, events)

    if state == "fruit-aisle":
        fruitAisle(screen, bg_fruit, font, pygame.mouse.get_pos(), check_click(events))
        state, resetPos = exit(state, events)

    if state == "cleaning-aisle":
        cleaningAisle(screen, bg_cleaning, font, pygame.mouse.get_pos(), check_click(events))
        state, resetPos = exit(state, events)

    if state == "vegetables-aisle":
        vegetablesAisle(screen, bg_vegetables, font, pygame.mouse.get_pos(), check_click(events))
        state, resetPos = exit(state, events)

    if state == "meat-aisle":
        meatAisle(screen, bg_meat, font, pygame.mouse.get_pos(), check_click(events))
        state, resetPos = exit(state, events)