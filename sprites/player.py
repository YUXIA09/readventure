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

        self.character_image = 1

    def move(self, keys):
        moved = False

        if keys[pygame.K_UP]:
            self.rect.y -= SPEED
            moved = True

        if keys[pygame.K_DOWN]:
            self.rect.y += SPEED
            moved = True

        if keys[pygame.K_LEFT]:
            self.rect.x -= SPEED
            moved = True

        if keys[pygame.K_RIGHT]:
            self.rect.x += SPEED
            moved = True

        if moved:
            self.swap_image()

    def swap_image(self):
        if self.character_image == 1:
            self.image = self.image2
            self.character_image = 2
        else:
            self.image = self.image1
            self.character_image = 1