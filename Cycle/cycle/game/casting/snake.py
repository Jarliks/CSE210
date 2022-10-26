import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, player, starting_x, starting_y, color):
        super().__init__()
        self._segments = []
        self._color = color
        self._prepare_body(starting_x, starting_y)
        self._playernumber = player

    def get_color(self):
        return self._color

    def get_segments(self):
        return self._segments

    def move_next(self):
        # update velocities
        segment = Actor()
        position = self._segments[0]._position
        segment.set_position(position)
        segment.set_velocity(0)
        segment.set_text("#")
        segment.set_color(self._color)
        self._segments.append(segment)

        # move Bike
        self._segments[0].move_next()

    def get_head(self):
        return self._segments[0]

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, starting_x, starting_y):
        x = starting_x
        y = starting_y

        for i in range(1):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = self._color
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)