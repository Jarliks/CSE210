import random

class Wordbank:
    """
    The word bank will select a word from a list of words, divide that word into a list of letters,
    and handle the calculations for guesses when letters should be revealed, as well as printing the 
    revealed letters and unguessed spaces
    """
    def __init__(self):
        """
        attributes:
        _word_list: predefined list of words to pull from
        _word: stores chosen word
        _letters: stores a list of each letter from the chosen word
        _correct: stores a list of boolean values which indicate whether the corresponding letter has been guessed
        """
        self._word_list = ['cheese', 'steel', 'pumpkin', 'skeleton']
        self._word = str()
        self._letters = []
        self._correct = []

    def _initialize(self):
        """
        Selects a word from _word_list and breaks it into a list of letters
        """
        self._word = self._word_list[random.randint(0, 3)]
        for letter in self._word:
            self._correct.append(False)
            self._letters.append(letter)

    def _compare(self, guess):
        """
        checks if the guessed letter is within the word, and sets the corresponding boolean in _correct
        """
        i = 0
        guess_correct = False
        for letter in self._letters:
            if guess == letter:
                self._correct[i] = True
                guess_correct = True
            i += 1
        return guess_correct

    def _write_letters(self):
        """
        outputs blank spaces for unguessed letters and letters that have been guessed correctly.
        """
        i = 0
        output = []
        for letter in self._letters:
            if self._correct[i]:
                output.append(f'{letter} ')
            else:
                output.append('_ ')
            i += 1
        print(*output)

    def _check_win(self):
        """
        checks if the palyer has guessed all letters.
        """
        keep_playing = False
        for i in self._correct:
            if not i:
                keep_playing = True
        return keep_playing