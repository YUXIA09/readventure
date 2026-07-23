text = "Shopping List:\nMilk\nBread Loafs\nEggs\nRedApples\nChicken"

itemsLevel1 = ["Milk", "Bread Loafs", "Eggs", "Red Apples", "Chicken"]

def level1(screen, font):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(topleft=(20, 50))
    screen.blit(text_surface, text_rect)

