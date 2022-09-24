from card import Card


class Director: 
    """
    The director of the game.

    moves the game through different stages.
    """
    def __init__(self):
        """Constructs a new Director.
        Args:
            self (Director): an instance of Director.
        """
        self.total_points = 300
        self.game_active = bool(True)
        self.card_flipped = 0
        self.guess = ""
        self.card_one = Card()
        self.card_two = Card()

    def start_game(self):
        """
        Main method to be run which plays the other methods
        """
        while self.game_active:
            self.flip_card()
            self.get_input_guess()
            self.flip_card()
            self.calculate_score()
            self.get_input_continue()

    def get_input_guess(self):
        """
        gets input from player on whether they think the next card will be higher or lower.
        """
        #ends if game is set to inactive
        if not self.game_active:
            return

        #reset guess variable and get guess for new round
        self.guess = ""
        while self.guess != "h" and self.guess != "l":
            self.guess = input("Higher or lower? [h/l] ")

    def flip_card(self):
        """
        uses the Card class to generate new cards. Acts differently depending on whether it is the first or second card to be flipped.
        """
        #ends if game is set to inactive
        if not self.game_active:
            return

        if self.card_flipped == 0:
            self.card_one.draw_card()
            self.card_flipped = self.card_one.value
            print(f"The card is: {self.card_one.value}")
        else:
            self.card_two.draw_card()
            while self.card_flipped == self.card_two.value:
                self.card_two.draw_card()
            print(f"The next card was: {self.card_two.value}")
            

    def calculate_score(self):
        """
        Updates player score and resets the flipped cards.
        """
        #ends if game is set to inactive
        if not self.game_active:
            return

        if self.guess == "h":
            if self.card_one.value > self.card_two.value:
                self.total_points -= 75
            else:
                self.total_points += 100
        elif self.guess == "l":
            if self.card_one.value > self.card_two.value:
                self.total_points += 100
            else:
                self.total_points -= 75
        else:
            print("Error: improper input saved")

        print(f"Your score is: {self.total_points}\n")
        self.card_flipped = 0

    def get_input_continue(self):
        """
        Asks the player if they wish to continue playing and gets their input.
        """
        #ends if game is set to inactive
        if not self.game_active:
            return
        set_game_status = input("Play again? [y/n] ")
        self.game_active = (set_game_status == "y")