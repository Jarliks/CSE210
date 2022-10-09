from game.things.collectable import Collectable

class Rock(Collectable):
    """
    A rock to avoid collecting.
    """
    def __init__(self):
        """
        creates new rock
        """
        self._value = -10

    def get_value(self):
        """
        returns thing's value
        """
        return self._value