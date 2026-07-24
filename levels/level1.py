#Format the text that will be shown on screen, here we use \n but in the other
#levels we use '''
text = "Shopping List:\nMilk\nBread Loafs\nEggs\nRedApples\nChicken"

#Create list for the actual items needed, we will check this against
#shopping cart.
itemsLevel1 = ["Milk", "Bread Loafs", "Eggs", "Red Apples", "Chicken"]
#itemsLevel1 = []

def level1(screen, font):
    #render the level's text
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(topleft=(20, 50))
    screen.blit(text_surface, text_rect)

