from game.things.collectable import Collectable

class Gem(Collectable):
    """
    A gem to collect
    """
    def __init__(self):
        """
        creates new gem
        """
        self._value = 30

    def get_value(self):
        """
        returns thing's value
        """
        return self._value