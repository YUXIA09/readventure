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

character_1 = pygame.image.load("assets/character_1.png").convert_alpha()
character_1 = pygame.transform.scale(character_1, (20, 50))

character_2 = pygame.image.load("assets/character_2.png").convert_alpha()
character_2 = pygame.transform.scale(character_2, (20, 50))
