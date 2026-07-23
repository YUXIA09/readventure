from rects import meatAisleItems

def meatAisle(screen, bg_meat, font, pos, click):
    screen.blit(bg_meat, (0, 0))

    text = font.render("Press ESC to leave. Click on items to add them to your cart", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)

    added_items = []
    if click:
        for key, value in meatAisleItems.items():
            if value.collidepoint(pos):
                added_items.append(key) 
    
    return added_items