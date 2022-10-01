class Jumper:
    """
    A class that keeps track of how healthy your jumper's parachute is, and prints the correlated visual.
    """
    def __init__(self):
        """
        attributes:
        _guesses_left: int which keeps track of how many wrong guesses the player has until they lose.
        """
        self._guesses_left = 4
    
    def _show_jumper(self):
        """
        prints various amounts of parachute visuals depending on the player's guesses left.
        """
        if self._guesses_left >= 4:
            print('  ___')
        if self._guesses_left >= 3:
            print(' /___\\')
        if self._guesses_left >= 2:
            print(' \\   /')
        if self._guesses_left >= 1:
            print('  \\ /')
        if self._guesses_left >= 1:
            print('   O')
        else:
            print('   X')
        print('  /|\\')
        print('  / \\')

    def _calculate_misses(self, guess_correct):
        """
        subtracts a wrong guess from _guesses_left.
        """
        if not guess_correct:
            self._guesses_left -= 1

    def _jumper_loss(self):
        """
        returns the guesses left.
        """
        return self._guesses_left