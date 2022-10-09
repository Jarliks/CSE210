import os
import random

from game.things.thing import Thing
from game.things.collectable import Collectable
from game.things.gem import Gem
from game.things.rock import Rock
from game.things.collection import Collection

from game.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
TOTAL_ROCKS = 30


def main():
    
    # create the cast
    collection = Collection()
    
    # create the banner
    banner = Thing()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    collection.add_thing("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(585)
    position = Point(x, y)

    player = Thing()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    collection.add_thing("players", player)
    
    # create the collectables
    for n in range(TOTAL_ROCKS):
        rock_or_gem = random.randint(0,1)

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        #if rock
        if rock_or_gem == 0:
            text = "*"
            thing = Gem()
        #if gem
        elif rock_or_gem == 1:
            text = "0"
            thing = Rock()
        
        thing.set_text(text)
        thing.set_font_size(FONT_SIZE)
        thing.set_color(color)
        thing.set_position(position)
        collection.add_thing("things", thing)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(collection)

if __name__ == "__main__":
    main()