import random

class Card:
    """
    Card class holds value of a card, and generates a random card.
    """

    def __init__(self):
        """
        creates new card, prepping it to hold a value.
        """
        self.value = int()

    def draw_card(self):
        """
        Generates a random value between 1 and 13 and stores it in the class' value variable.
        """
        self.value = random.randrange(1,13)