from rects import vegetablesAisleItems

def vegetablesAisle(screen, bg_vegetables, font, pos, click):
    screen.blit(bg_vegetables, (0, 0))

    text = font.render("Press ESC to leave. Click on items to add them to your cart", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)

    added_items = []
    if click:
        for key, value in vegetablesAisleItems.items():
            if value.collidepoint(pos):
                added_items.append(key) 
    
    return added_items