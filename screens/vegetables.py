def vegetablesAisle(screen, bg_vegetables, font, pos, click):
    screen.blit(bg_vegetables, (0, 0))

    text = font.render("Press ESC to leave", True, (255, 255, 255))
    
    text_rect = text.get_rect()
    screen.blit(text, text_rect)