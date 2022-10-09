import pyray
from game.shared.point import Point


class KeyboardService:
    """
    gets and returns direction based on kayboard inputs
    """

    def __init__(self, cell_size = 1):
        """
        creates new instance
        """
        self._cell_size = cell_size

    def get_direction(self):
        """
        gets keyboard inputs and returns a direction
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        #Removed to ensure only horizontal movement
        """if pyray.is_key_down(pyray.KEY_UP):
            dy = -1
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1"""

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction