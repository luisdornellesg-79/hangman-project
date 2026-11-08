class HangmanGame:
    """Models the state of a Hangman game."""

    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Show the word with the unguessed letters hidden as underscores."""
        shown = []
        for letter in self.word:
            if letter.isalpha() and letter.lower() not in self.guessed_letters:
                shown.append("_")
            else:
                shown.append(letter)
        progress = " ".join(shown)
        print(progress)
        return progress
    
    def process_guess(self, letter):
        """Process a guessed letter and return True if it is in the word."""
        letter = letter.lower()
        if letter in self.word.lower():
            self.guessed_letters.append(letter)
            return True
        self.errors += 1
        return False
    
    
    
    def is_won(self):
        """Return True if every letter of the word has been guessed."""
        for letter in self.word:
            if letter.isalpha() and letter.lower() not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        """Return True if the errors have reached the maximum allowed."""
        return self.errors >= self.max_errors