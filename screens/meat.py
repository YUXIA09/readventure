def meatAisle(screen, bg_meat, font, pos, click):
    screen.blit(bg_meat, (0, 0))

    text = font.render("Press ESC to leave", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)