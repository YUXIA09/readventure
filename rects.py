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

cashierRect = pygame.Rect(320, 60, 170, 90)

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

bread_loafs = pygame.Rect(40, 120, 200, 140)
bread_buns = pygame.Rect(250, 120, 100, 140)
baguette = pygame.Rect(365, 100, 130, 160)
whole_wheat_baguette = pygame.Rect(510, 100, 120, 160)
bagels = pygame.Rect(640, 140, 120, 110)
flour = pygame.Rect(40, 335, 490, 125)
eggs = pygame.Rect(540, 335, 210, 135)

breadAisleItems = {
    "Bread Loafs": bread_loafs,
    "Bread Buns": bread_buns,
    "Baguette": baguette,
    "Whole Wheat Baguette": whole_wheat_baguette,
    "Bagels": bagels,
    "Flour": flour,
    "Eggs": eggs,
                   }

bananas = pygame.Rect(30, 130, 125, 140)
oranges = pygame.Rect(165, 140, 95, 130)
red_apples = pygame.Rect(270, 140, 90, 130)
green_apples = pygame.Rect(370, 140, 85, 130)
purple_grapes = pygame.Rect(470, 140, 85, 130)
green_grapes = pygame.Rect(570, 140, 85, 130)
peaches = pygame.Rect(670, 140, 85, 130)
strawberies = pygame.Rect(30, 350, 105, 120)
blueberries = pygame.Rect(148, 360, 72, 110)
lemons = pygame.Rect(235, 350, 85, 120)
limes = pygame.Rect(335, 350, 80, 120)
pears = pygame.Rect(425, 360, 110, 110)
kiwis = pygame.Rect(550, 360, 65, 110)
pineapples = pygame.Rect(630, 330, 130, 140)

fruitAisleItems = {
    "Bananas": bananas,
    "Oranges": oranges,
    "Red Apples": red_apples,
    "Green Apples": green_apples,
    "Purple Grapes": purple_grapes,
    "Green Grapes": green_grapes,
    "Peaches": peaches,
    "Strawberies": strawberies,
    "Blueberries": blueberries,
    "Lemons": lemons,
    "Limes": limes,
    "Pears": pears,
    "Kiwis": kiwis,
    "Pineapples": pineapples
}

detergent = pygame.Rect(40, 140, 170, 130)
window_cleaner = pygame.Rect(225, 140, 130, 130)
fabric_softener = pygame.Rect(370, 140, 120, 130)
dishwashing_liquid = pygame.Rect(510, 140, 250, 130)
surface_cleaner = pygame.Rect(40, 330, 170, 150)
toilet_cleaner = pygame.Rect(225, 330, 125, 150)
disinfecting_wipes = pygame.Rect(367, 330, 135, 150)
soap = pygame.Rect(510, 380, 130, 100)
sponges = pygame.Rect(655, 415, 112, 65)

cleaningAisleItems = {
    "Detergent": detergent,
    "Window Cleaner": window_cleaner,
    "Fabric Softener": fabric_softener,
    "Dishwashing Liquid": dishwashing_liquid,
    "Surface Cleaner": surface_cleaner,
    "Toilet Cleaner": toilet_cleaner,
    "Disinfecting Wipes": disinfecting_wipes,
    "Soap": soap,
    "Sponges": sponges
}

carrots = pygame.Rect(40, 130, 140, 140)
onions = pygame.Rect(190, 130, 110, 140)
potatoes = pygame.Rect(315, 130, 100, 140)
tomatoes = pygame.Rect(430, 130, 115, 140)
cucumbers = pygame.Rect(555, 130, 90, 140)
green_bell_peppers = pygame.Rect(660, 130, 100, 140)
lettuce = pygame.Rect(40, 335, 130, 140)
eggplants = pygame.Rect(180, 335, 85, 140)
red_bell_peppers = pygame.Rect(280, 335, 95, 140)
broccoli = pygame.Rect(395, 335, 115, 140)
garlic = pygame.Rect(525, 335, 95, 140)
spinach = pygame.Rect(635, 335, 125, 140)

vegetablesAisleItems = {
    "Carrots": carrots,
    "Onions": onions,
    "Potatoes": potatoes,
    "Tomatoes": tomatoes,
    "Cucumbers": cucumbers,
    "Green Bell Peppers": green_bell_peppers,
    "Lettuce": lettuce,
    "Eggplants": eggplants,
    "Red Bell Peppers": red_bell_peppers,
    "Broccoli": broccoli,
    "Garlic": garlic,
    "Spinach": spinach
}

chicken = pygame.Rect(40, 120, 170, 120)
steak = pygame.Rect(220, 120, 200, 120)
ground_beef = pygame.Rect(440, 120, 190, 120)
burger_patties = pygame.Rect(640, 120, 130, 120)
tenderloins = pygame.Rect(40, 330, 190, 140)
pork_belly = pygame.Rect(240, 330, 195, 140)
sausages = pygame.Rect(450, 330, 120, 140)
bacon = pygame.Rect(580, 330, 190, 140)

meatAisleItems = {
    "Chicken": chicken,
    "Steak": steak,
    "Ground Beef": ground_beef,
    "Burger Patties": burger_patties,
    "Tenderloins": tenderloins,
    "Pork Belly": pork_belly,
    "Sausages": sausages,
    "Bacon": bacon
}