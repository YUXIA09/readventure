import pygame

def welcome(screen, bg_welcome, font, events):
    #Draw welcome screen, and draw start button.
    screen.blit(bg_welcome, (0, 0))
    start = pygame.Rect(300, 400, 200, 75)
    pygame.draw.rect(screen, (150, 150, 150), start)

    text = font.render("Start", True, (0, 0, 0))

    text_rect = text.get_rect(center=start.center)
    screen.blit(text, text_rect)

    #in main.py, we set state = welcome(...)
    #This means that if start button is clicked, the state will be changed.
    return check_click(events, start)
    

def check_click(events, start):
    for event in events:
        #check if the mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.dict["pos"]
            #check if the mouse is in the start rect, if so, return main-screen
            if start.collidepoint(pos): 
                return "main-screen"
            
    return "welcome-screen"