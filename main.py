import pygame

from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#import all necessary files
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

#Please read README for a short reflection on the game's code.

clock = pygame.time.Clock()

#Set font for text in game
font = pygame.font.Font(None, 30)
itemFont = pygame.font.Font(None, 18)

#Create player sprite and add to sprite group
mainPlayer = Player(character_1, character_2, 225, 135)
sprites = pygame.sprite.Group()
sprites.add(mainPlayer)

#Create popups sprites for when the player completes or fails a level
complete_popup = popup(supermarket_complete_popup)
failure_popup = popup(supermarket_failure_popup)

#Create functions to check if the player has clicked the mouse, exit the aisles, wait for spacebar to be pressed, and end the Supermarket game
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

#Main game loop
while running:
    #Update screen, tick clock and get all events
    pygame.display.flip()
    clock.tick(60)
    events = pygame.event.get()

    #Check if the player has quit the game
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    #Check the current state of the game and call the appropriate function to handle that state
    if state == "welcome-screen":
        state = welcome(screen, bg_welcome, font, events)

    if state == "main-screen":
        #Check if the player's position should be reseted to the starting position in the main screen
        if not resetPos:
            mainPlayer.rect.x = 225
            mainPlayer.rect.y = 135
            resetPos = True

        #Call the game function to handle the main screen
        game(screen, bg_main, sprites)

        #Get all keys pressed, move the player and ensure the player does not exit the screen bounds
        keys = pygame.key.get_pressed()
        moved = mainPlayer.move(keys)
        mainPlayer.rect.clamp_ip(screen.get_rect())

        #Check if the player has moved for the first time
        if moved:
            movedInitial = True

        #If the player has not moved, showed the text to explain use arrow keys to move
        if not movedInitial:
            textMove = font.render("Use arrow keys to move", True, (255, 255, 255))
            textMove_rect = textMove.get_rect()
            screen.blit(textMove, textMove_rect)

        #Check if the player is colliding with the supermarket icon and if so, change state to supermarket-screen and reset the player's position in the supermarket
        if mainPlayer.rect.colliderect(supermarket):
            state = "supermarket-screen"
            resetPos = False

    if state == "supermarket-screen":
        #Check if the player's position should be reseted to the starting position in the supermarket
        if not resetPos:
            mainPlayer.rect.x = 750
            mainPlayer.rect.y = 110
            resetPos = True

        #Get all keys pressed, move the player and ensure the player does not exit the screen bounds
        keys = pygame.key.get_pressed()
        mainPlayer.move(keys)
        mainPlayer.rect.clamp_ip(supermarketBounds)

        #Get the position of the player's feet and call the play function.
        feet = (mainPlayer.rect.centerx, mainPlayer.rect.bottom - 20)
        play(screen, bg_supermarket, sprites, font, supermarket_level)

        #Draw the rect where the shopping cart list will be shown
        pygame.draw.rect(screen, (255,255,255), cartList)

        #Prepare the shopping cart text to be rendered.
        cart = "Shopping Cart:\n"
        for item in shopping_cart:
            cart += item 
            cart += "\n"

        #Check if the player is close enough to the cashier to checkout
        if cashierRect.collidepoint(mainPlayer.rect.center):
            #Render instructions to checkout
            text = font.render("Click on Cashier to Checkout", True, (255, 255, 255))
            text_rect = text.get_rect(topleft=cashierRect.topleft)
            screen.blit(text, text_rect)

            #Check if the player has clicked on the cashier
            if cashierRect.collidepoint(pygame.mouse.get_pos()) and check_click(events):
                #Check which supermarket level it is, and check if the shopping cart 
                # items are the same as the required items for each level. If so, run 
                # win function, if not, run lose function.
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

        #Render the shopping cart list and display within the cartList rect
        text = itemFont.render(cart, True, (0, 0, 0))   
        text_rect = text.get_rect(topleft=cartList.topleft)
        screen.blit(text, text_rect)

        #Check if the player's feet is within any aisles rect. If so, change state to that aisle
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

        #Check if escape is pressed, if so, return to main-screen

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "main-screen"
                    resetPos = False

    #Check which state the player is in, get the clicked items,
    #add to shopping cart, and check if the player decides to exit
    #the aisle, if so resetPos will be set True.
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