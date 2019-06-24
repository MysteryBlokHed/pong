# Created by MysteryBlokHed in 2019.
import pygame
from game_object import GameObject

class Player(GameObject):
    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self._x, self._y, self._width, self._height))
    
    def tick(self):
        self._y += self._vel_y