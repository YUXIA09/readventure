from rects import breadAisleItems
from settings import WIDTH, HEIGHT
import pygame
import time

#Create functioon for the aisle.
def breadAisle(screen, bg_bread, font, pos, click):
    #Draw background
    screen.blit(bg_bread, (0, 0))

    #Render the text, on top left corner
    text = font.render("Press ESC to leave. Click on items to add them to your cart", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)

    #Create list with clicked items.
    added_items = []

    #If the mouse is clicked
    if click:

        #Check each breadAisle item's rect to see if the position of the mouse is in that rect.
        #The rect should be the value.
        for key, value in breadAisleItems.items():
            #If the mouse is in the rect, 
            if value.collidepoint(pos):
                #Add the key, which should be the name of the item to the added items.
                added_items.append(key) 
                #Render text showing that the item has been added.
                text = font.render(f"{key} added to cart!", True, (255, 255, 255))
                text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
                screen.blit(text, text_rect)
                #Update screen and wait a bit to ensure the messge is shown for long enough
                pygame.display.flip()
                time.sleep(0.3)

    #Return added items, recall that in main.py supermarket cart will add the items in here.
    return added_items