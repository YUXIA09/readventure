def cleaningAisle(screen, bg_cleaning, font, pos, click):
    screen.blit(bg_cleaning, (0, 0))

    text = font.render("Press ESC to leave", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)