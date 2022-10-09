# Author: Alec Mateski

# Class: CSE 210

# Program: Greed

### Assignment

Rules

Greed is played according to the following rules.

    Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
    The player (#) can move left or right along the bottom of the screen.
    If the player touches a gem they earn a point.
    If the player touches a rock they lose a point.
    Gems and rocks are removed when the player touches them.
    The game continues until the player closes the window.

## _main_.py

creates and runs the game director, as well as sets up many of the values and classes used by director.

## director.py

defines the game director class.

## keyboard_service.py

defines the Keyboardservice class, which handles keyboard inputs

## video_service.py

defines the Videoservice class, which handles the renpy and visuals of the game.

## color.py

defines the color class

## point.py

defines the point class

## collectable.py

defines collecatable class, inherits from thing

## collection.py

defines the collection class

## gem.py

defines the gem class, inherits from collectable

## rock.py

defines the rock class, inherits from collectable

## thing.py

defines the thing class
