import pygame

from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

from assets import *
from rects import *
from sprites.player import Player
from sprites.popups import popup
from screens.welcome import welcome
from screens.game import game
from screens.supermarket import *
from screens.dairy import dairyAisle
from screens.bread import breadAisle
from screens.cleaning import cleaningAisle
from screens.fruit import fruitAisle
from screens.meat import meatAisle
from screens.vegetables import vegetablesAisle


clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)
itemFont = pygame.font.Font(None, 18)

mainPlayer = Player(character_1, character_2, 225, 135)
sprites = pygame.sprite.Group()
sprites.add(mainPlayer)

complete_popup = popup(supermarket_complete_popup)
failure_popup = popup(supermarket_failure_popup)

supermarket_level = 1

def check_click(events):
    click = False
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

    return click

def exitAisles(state, events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "supermarket-screen", False

    return state, True

def waitForSpace():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

def endGame(Win):
    global supermarket_level
    text = font.render("Press Space to Continue", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
    screen.blit(text, text_rect)
    if Win:
        print("You Win!")
        
        complete_popup.visible = True
        complete_popup.draw(screen)
        pygame.display.flip()
        
        supermarket_level += 1
                            
        waitForSpace()
        complete_popup.visible = False
                            
        shopping_cart.clear()
        
        if supermarket_level == 4:
            print("You have completed all levels!")
            supermarket_level = 1
    
    else:
        print("You Lose!")
    
        failure_popup.visible = True
        failure_popup.draw(screen)
        pygame.display.flip()
    
        waitForSpace()
    
        failure_popup.visible = False
        shopping_cart.clear()

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

        keys = pygame.key.get_pressed()
        moved = mainPlayer.move(keys)
        mainPlayer.rect.clamp_ip(screen.get_rect())
        
        if moved:
            movedInitial =True

        if not movedInitial:
            textMove = font.render("Use arrow keys to move", True, (255, 255, 255))
            textMove_rect = textMove.get_rect()
            screen.blit(textMove, textMove_rect)

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

        pygame.draw.rect(screen, (255,255,255), cartList)

        cart = "Shopping Cart:\n"
        for item in shopping_cart:
            cart += item 
            cart += "\n"

        if cashierRect.collidepoint(mainPlayer.rect.center):
            text = font.render("Click on Cashier to Checkout", True, (255, 255, 255))
            text_rect = text.get_rect(topleft=cashierRect.topleft)
            screen.blit(text, text_rect)

            if cashierRect.collidepoint(pygame.mouse.get_pos()) and check_click(events):
                if supermarket_level == 1:
                    if check_items(shopping_cart, itemsLevel1):
                        endGame(True)
                    else:
                        endGame(False)
                elif supermarket_level == 2:
                    if check_items(shopping_cart, itemsLevel2):
                        endGame(True)
                    else:
                        endGame(False)
                elif supermarket_level == 3:
                    if check_items(shopping_cart, itemsLevel3):
                        endGame(True)
                    else:
                        endGame(False)

        text = itemFont.render(cart, True, (0, 0, 0))   
        text_rect = text.get_rect(topleft=cartList.topleft)
        screen.blit(text, text_rect)
        
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
        addeditems = dairyAisle(screen, bg_dairy, font, pygame.mouse.get_pos(), check_click(events))
        shopping_cart.extend(addeditems)
        state, resetPos = exitAisles(state, events)

    if state == "bread-aisle":
        addeditems = breadAisle(screen, bg_bread, font, pygame.mouse.get_pos(), check_click(events))
        shopping_cart.extend(addeditems)
        state, resetPos = exitAisles(state, events)

    if state == "fruit-aisle":
        addeditems = fruitAisle(screen, bg_fruit, font, pygame.mouse.get_pos(), check_click(events))
        shopping_cart.extend(addeditems)
        state, resetPos = exitAisles(state, events)

    if state == "cleaning-aisle":
        addeditems = cleaningAisle(screen, bg_cleaning, font, pygame.mouse.get_pos(), check_click(events))
        shopping_cart.extend(addeditems)
        state, resetPos = exitAisles(state, events)

    if state == "vegetables-aisle":
        addeditems = vegetablesAisle(screen, bg_vegetables, font, pygame.mouse.get_pos(), check_click(events))
        shopping_cart.extend(addeditems)
        state, resetPos = exitAisles(state, events)

    if state == "meat-aisle":
        addeditems = meatAisle(screen, bg_meat, font, pygame.mouse.get_pos(), check_click(events))
        shopping_cart.extend(addeditems)
        state, resetPos = exitAisles(state, events)