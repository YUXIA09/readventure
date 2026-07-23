import pygame
from settings import WIDTH, HEIGHT

class popup(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.visible = False

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)