import pygame 

from settings import WIDTH, HEIGHT

bg_welcome = pygame.image.load("assets/background_welcome.png").convert()
bg_welcome = pygame.transform.scale(bg_welcome, (WIDTH, HEIGHT))

bg_main = pygame.image.load("assets/background_main.png").convert()
bg_main = pygame.transform.scale(bg_main, (WIDTH, HEIGHT))

bg_supermarket = pygame.image.load("assets/background_supermarket.png").convert()
bg_supermarket = pygame.transform.scale(bg_supermarket, (WIDTH, HEIGHT))

bg_dairy = pygame.image.load("assets/background_dairy.png").convert()
bg_dairy = pygame.transform.scale(bg_dairy, (WIDTH, HEIGHT))

bg_bread = pygame.image.load("assets/background_bread.png").convert()
bg_bread  = pygame.transform.scale(bg_bread , (WIDTH, HEIGHT))

bg_cleaning = pygame.image.load("assets/background_cleaning.png").convert()
bg_cleaning = pygame.transform.scale(bg_cleaning, (WIDTH, HEIGHT))

bg_fruit = pygame.image.load("assets/background_fruit.png").convert()
bg_fruit = pygame.transform.scale(bg_fruit, (WIDTH, HEIGHT))

bg_meat = pygame.image.load("assets/background_meat.png").convert()
bg_meat = pygame.transform.scale(bg_meat, (WIDTH, HEIGHT))

bg_vegetables = pygame.image.load("assets/background_vegetables.png").convert()
bg_vegetables = pygame.transform.scale(bg_vegetables, (WIDTH, HEIGHT))

supermarket_complete_popup = pygame.image.load("assets/supermarket_complete.png").convert()
supermarket_complete_popup = pygame.transform.scale(supermarket_complete_popup, (200, 160))

supermarket_failure_popup = pygame.image.load("assets/supermarket_failure.png").convert()
supermarket_failure_popup = pygame.transform.scale(supermarket_failure_popup, (200, 160))

character_1 = pygame.image.load("assets/character_1.gif").convert_alpha()
character_1 = pygame.transform.scale(character_1, (30, 75))

character_2 = pygame.image.load("assets/character_2.gif").convert_alpha()
character_2 = pygame.transform.scale(character_2, (30, 75))
