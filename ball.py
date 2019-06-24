# Created by MysteryBlokHed in 2019.
import pygame
from game_object import GameObject

class Ball(GameObject):
    # _screen_width = 0
    # _screen_height = 0

    # def __init__(self, x, y, width, height, id, screen_width, screen_height):
    #     super().__init__(x, y, width, height, id)
    #     if type(screen_width) is int:
    #         self._screen_width = screen_width
    #     if type(screen_height) is int:
    #         self._screen_height = screen_height

    def render(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self._x, self._y), self._width)
    
    def tick(self):
        self._x += self._vel_x
        self._y += self._vel_y