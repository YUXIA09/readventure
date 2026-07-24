import pygame
from settings import SPEED

#Define Player class.
class Player(pygame.sprite.Sprite):
    def __init__(self, image1, image2, x, y):
        super().__init__()

        #Have two different images to allow for an animation
        self.image1 = image1
        self.image2 = image2
        self.image = image1

        #Set the players rec, it's inital position, and which direction 
        # it is facing.
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = "right"

        #Keep track of which image the sprite is on and count of 
        # how many frames it has passed since the last image swap.
        self.character_image = 1
        self.count = 0

    def move(self, keys):

        moved = False

        #Player movement logic.    
        if keys[pygame.K_UP]:
            self.rect.y -= SPEED
            moved = True

        if keys[pygame.K_DOWN]:
            self.rect.y += SPEED
            moved = True

        if keys[pygame.K_LEFT]:
            #If the player is facing the opposite direction to movement, flip all images.
            if self.direction == "right":
                self.image1 = pygame.transform.flip(self.image1, True, False)
                self.image2 = pygame.transform.flip(self.image2, True, False)
                self.direction = "left"

            self.rect.x -= SPEED
            moved = True

        if keys[pygame.K_RIGHT]:
            #If the player is facing the opposite direction to movement, flip all images.
            if self.direction == "left":
                self.image1 = pygame.transform.flip(self.image1, True, False)
                self.image2 = pygame.transform.flip(self.image2, True, False)
                self.direction = "right"

            self.rect.x += SPEED
            moved = True

        if moved:
            self.swap_image()

        return moved

    def swap_image(self):
        #Thank you Max for this idea, this makes the movement more natural.
        #Keeps count of how many frames it has been since the last image 
        # swap, every 12 frames, the icon will swap.
        if self.count > 12:
            if self.character_image == 1:
                self.image = self.image2
                self.character_image = 2
            else:
                self.image = self.image1
                self.character_image = 1

            self.count = 0

        self.count += 1