import pygame
from settings import WIDTH, HEIGHT

#Code for the popup class
class popup(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        #Set image, self.rect to the center of the screen, and its visibility to false
        self.image = image
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.visible = False

    def draw(self, screen):
        #check if sprite is visible, if so, draw.
        if self.visible:
            screen.blit(self.image, self.rect)