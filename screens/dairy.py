from rects import dairyAisleItems



def dairyAisle(screen, bg_dairy, font, pos, click):
    screen.blit(bg_dairy, (0, 0))

    text = font.render("Press ESC to leave", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)

    added_items = []
    if click:
        for key, value in dairyAisleItems.items():
            if value.collidepoint(pos):
                added_items.append(f"{key}".split('=')[0]) 

    return added_items
            
                

                
        

