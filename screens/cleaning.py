from rects import cleaningAisleItems

def cleaningAisle(screen, bg_cleaning, font, pos, click):
    screen.blit(bg_cleaning, (0, 0))

    text = font.render("Press ESC to leave. Click on items to add them to your cart", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)

    added_items = []
    if click:
        for key, value in cleaningAisleItems.items():
            if value.collidepoint(pos):
                added_items.append(key) 
        
    return added_items