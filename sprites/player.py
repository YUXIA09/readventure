import pygame
from settings import SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self, image1, image2, x, y):
        super().__init__()

        self.image1 = image1
        self.image2 = image2
        self.image = image1

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = "right"

        self.character_image = 1
        self.count = 0

    def move(self, keys):
        moved = False

        if keys[pygame.K_UP]:
            self.rect.y -= SPEED
            moved = True

        if keys[pygame.K_DOWN]:
            self.rect.y += SPEED
            moved = True

        if keys[pygame.K_LEFT]:
            if self.direction == "right":
                self.image1 = pygame.transform.flip(self.image1, True, False)
                self.image2 = pygame.transform.flip(self.image2, True, False)
                self.direction = "left"

            self.rect.x -= SPEED
            moved = True

        if keys[pygame.K_RIGHT]:
            if self.direction == "left":
                self.image1 = pygame.transform.flip(self.image1, True, False)
                self.image2 = pygame.transform.flip(self.image2, True, False)
                self.direction = "right"

            self.rect.x += SPEED
            moved = True

        if moved:
            self.swap_image()

    def swap_image(self):
        #Thank you Max for this idea, this makes the movement more natural.
        if self.count > 12:
            if self.character_image == 1:
                self.image = self.image2
                self.character_image = 2
            else:
                self.image = self.image1
                self.character_image = 1

            self.count = 0

        self.count += 1