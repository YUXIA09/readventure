import pygame

supermarket = pygame.Rect(320, 100, 110, 70)
supermarketBounds = pygame.Rect(175, 100, 610, 480)

cartList = pygame.Rect(10, 450, 160, 140)

dairy = pygame.Rect(185, 200, 240, 60)
bread = pygame.Rect(500, 200, 240, 60)

fruit = pygame.Rect(185, 310, 240, 60)
cleaning = pygame.Rect(500, 310, 240, 60)

vegetables = pygame.Rect(185, 430, 240, 60)
meat = pygame.Rect(500, 430, 240, 60)

milk = pygame.Rect(40, 120, 260, 150)
chocolate_milk = pygame.Rect(305, 130, 135, 140)
yogurt = pygame.Rect(445, 130, 100, 140)
strawberry_yogurt = pygame.Rect(560, 130, 100, 140)
blueberry_yogurt = pygame.Rect(670, 130, 100, 140)
butter = pygame.Rect(40, 350, 320, 140)
cheese = pygame.Rect(370, 350, 400, 140)

dairyAisleItems = {
                    "Milk": milk,
                    "Chocolate Milk": chocolate_milk, 
                    "Yogurt": yogurt, 
                    "Strawberry Yogurt": strawberry_yogurt, 
                    "Blueberry Yogurt": blueberry_yogurt, 
                    "Butter": butter, 
                    "Cheese": cheese
                   }

