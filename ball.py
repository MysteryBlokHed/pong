# Created by MysteryBlokHed in 2019.
import pygame
from game_object import GameObject

class Ball(GameObject):
    def render(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self._x, self._y), self._width)
    
    def tick(self):
        self._x += self._vel_x
        self._y += self._vel_y