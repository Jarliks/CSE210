import random
from game.shared.point import Point
from game.shared.color import Color

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        
    def start_game(self, collection):
        """Starts the game using the given collection. Runs the main game loop.

        Args:
            collection (collection): The collection of things.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(collection)
            self._do_updates(collection)
            self._do_outputs(collection)
        self._video_service.close_window()

    def _get_inputs(self, collection):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            collection (collection): The collection of things.
        """
        player = collection.get_first_thing("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, collection):
        """Updates the player's position and resolves any collisions with things.
        
        Args:
            collection (collection): The collection of things.
        """
        banner = collection.get_first_thing("banners")
        player = collection.get_first_thing("players")
        things = collection.get_things("things")

        banner.set_text(str(self._score))
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for thing in things:
            thing.fall(600)
            if player.get_position().equals(thing.get_position()):
                value = thing.get_value()
                self._score += value
                new_position = Point(random.randint(1, 60 - 1), 1)
                thing.set_position(new_position)
                new_color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                thing.set_color(new_color)

        
    def _do_outputs(self, collection):
        """Draws the things on the screen.
        
        Args:
            collection (collection): The collection of things.
        """
        self._video_service.clear_buffer()
        things = collection.get_all_things()
        self._video_service.draw_things(things)
        self._video_service.flush_buffer()