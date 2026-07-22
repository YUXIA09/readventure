import pygame

def welcome(screen, bg_welcome, font, events):
    screen.blit(bg_welcome, (0, 0))
    start = pygame.Rect(300, 400, 200, 75)
    pygame.draw.rect(screen, (150, 150, 150), start)

    text = font.render("Start", True, (0, 0, 0))

    text_rect = text.get_rect(center=start.center)
    screen.blit(text, text_rect)

    return check_click(events, start)
    

def check_click(events, start):
    for event in events:

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.dict["pos"]
            if start.collidepoint(pos): 
                return "main-screen"
            
    return "welcome-screen"