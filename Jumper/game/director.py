from terminal import Terminal
from jumper import Jumper
from wordbank import Wordbank

class Director:
    """
    The game director, runs through initialization, and loops through the stages fo the game.
    """
    def __init__(self):
        """
        creates Director and other classes.
        Attributes:
        _is_playing: Boolean keeps track of whether the game should continue or not
        _guess: str holds the palyer's guessed letter

        _terminal: instance of Terminal
        _jumper: instance of Jumper
        _wordbank: instance of Wordbank
        """
        self._terminal = Terminal()
        self._is_playing = True
        self._jumper = Jumper()
        self._wordbank = Wordbank()
        self._guess = str()

    def _run_game(self):
        """
        runs initialize and loops through game steps as long as _is_playing is true
        """
        self._initialize()
        while self._is_playing:
            self._send_outputs()
            self._get_inputs()
            self._do_updates()

    def _initialize(self):
        """
        calls wordbank's initialize, to select and prep the word to guess.
        """
        self._wordbank._initialize()
            
    def _send_outputs(self):
        """
        calls wordbank to write the letters and blank spaces of the word to guess
        calls jumper to print the visual for the jumper
        """
        self._wordbank._write_letters()
        self._jumper._show_jumper()

    def _get_inputs(self):
        """
        gets player inputs
        """
        if self._is_playing == False:
            return
        
        self._guess = self._terminal.read_input('Guess a letter [a-z]: ')

    def _do_updates(self):
        """
        calls jumper and wordbank to calculate misses and if they should reduce jumper's parachute health
        if a game end condition is met, calls send outputs one last time and give player win/loss messages.
        """
        self._jumper._calculate_misses(self._wordbank._compare(self._guess)) 
        self._is_playing = self._wordbank._check_win()
        if not self._is_playing:
            self._send_outputs()
            print('Congradulations! You win!')
        if self._jumper._jumper_loss() == 0:
            self._is_playing = False
            self._send_outputs()
            print('You lose!')
