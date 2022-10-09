from game.things.thing import Thing
from game.shared.point import Point

class Collectable(Thing):
    """
    A thing that the palyer can collect.
    its purpose is to manage falling
    """

    def fall(self, max_y):
        """
        moves the collectable down the grid.
        """
        x = self._position.get_x()
        y = (self._position.get_y() + 3) % max_y
        self._position = Point(x, y)