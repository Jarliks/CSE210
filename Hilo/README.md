# Author: Alec Mateski

# Class: CSE 210

# Program: Hilo

### Assignment

Hilo is played according to the following rules.

    The player starts the game with 300 points.
    Individual cards are represented as a number from 1 to 13.
    The current card is displayed.
    The player guesses if the next one will be higher or lower.
    The the next card is displayed.
    The player earns 100 points if they guessed correctly.
    The player loses 75 points if they guessed incorrectly.
    If a player reaches 0 points the game is over.
    If a player has more than 0 points they decide if they want to keep playing.
    If a player decides not to play again the game is over.

## _main_.py

    Runs the game by creating a Director and calling game_start method.

## director.py

    contains the director class, which holds the methods which move the game along.

## card.py

    contains the card class, which generate random cards and hold their value.
