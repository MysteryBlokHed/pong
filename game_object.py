# Created by MysteryBlokHed in 2019.
class GameObject(object):
    _x = 0
    _y = 0

    _vel_x = 0
    _vel_y = 0

    _width = 0
    _height = 0

    def __init__(self, x, y, width, height):
        # Check the type of x
        if type(x) is int:
            self._x = x
        if type(y) is int:
            self._y = y
        if type(width) is int:
            self._width = width
        if type(height) is int:
            self._height = height

    # Getters
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_vel_x(self):
        return self._vel_x

    def get_vel_y(self):
        return self._vel_y
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    # Setters
    def set_x(self, x):
        if type(x) is int:
            self._x = x
    
    def set_y(self, y):
        if type(y) is int:
            self._y = y

    def set_vel_x(self, vel_x):
        if type(vel_x) is int:
            self._vel_x = vel_x
    
    def set_vel_y(self, vel_y):
        if type(vel_y) is int:
            self._vel_y = vel_y
    
    def set_width(self, width):
        if type(width) is int:
            self._width = width
    
    def set_height(self, height):
        if type(height) is int:
            self._height = height
    
    # Other functions

    def render(self):
        pass
    
    def tick(self):
        pass
    
    def check_collision_rect_autohitbox(self, x, y, width, height, mode=0):
        """Check a collision with another rectangular object. x, y, width, and height are for the other object.
        mode: The current object's shape. 0=rectangle, 1=oval."""
        # Check collision as rectange
        if mode == 0:
            if self._x <= x + width and self._x >= x and self._y <= y + height and self._y >= y:
                return True
            else:
                return False
        # Check collision as oval
        elif mode == 1:
            # if self._x - self._width/2 <= x + width and self._x + self._width/2 >= x and self._y - self._height/2 <= y + height and self._y + self._height/2 >= y:
            if self._x - self._width <= x + width and self._x + self._width >= x and self._y - self._height <= y + height and self._y + self._height >= y:
                return True
            else:
                return False