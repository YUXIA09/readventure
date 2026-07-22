def dairyAisle(screen, bg_dairy, font, pos, click):
    screen.blit(bg_dairy, (0, 0))

    text = font.render("Press ESC to leave", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)