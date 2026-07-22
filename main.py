import pygame

from settings import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

from assets import bg_main, bg_welcome, bg_supermarket, character_1, character_2
from sprites.player import Player
from screens.welcome import welcome
from screens.game import game
from screens.supermarket import play

clock = pygame.time.Clock()
running = True

state = "supermarket-screen"
font = pygame.font.Font(None, 36)

mainPlayer = Player(character_1, character_2, 225, 135)
sprites = pygame.sprite.Group()
sprites.add(mainPlayer)

supermarket_level = 1
resetPos = False

while running:
    clock.tick(60)
    events = pygame.event.get()
    pygame.display.flip()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if state == "welcome-screen":
        state = welcome(screen, bg_welcome, font, events)

    if state == "main-screen":
        game(screen, bg_main, sprites)

        mainPlayer.rect.clamp_ip(screen.get_rect())
        keys = pygame.key.get_pressed()
        mainPlayer.move(keys)

        supermarket = pygame.Rect(320, 100, 110, 70)
        if mainPlayer.rect.colliderect(supermarket):
            state = "supermarket-screen"

    if state == "supermarket-screen":
        
        if not resetPos:
            mainPlayer.rect.x = 750
            mainPlayer.rect.y = 110
            resetPos = True

        play(screen, bg_supermarket, sprites, supermarket_level)

        supermarket = pygame.Rect(320, 100, 110, 70)
        supermarketBounds = pygame.Rect(217, 100, 565, 465)

        keys = pygame.key.get_pressed()
        mainPlayer.move(keys)
        mainPlayer.rect.clamp_ip(supermarketBounds)

        if mainPlayer.rect.colliderect(supermarket):
            state = "supermarket-screen"

    pygame.display.flip()
    
