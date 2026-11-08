import random

HANGMAN_STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def get_random_word():
    """Return a random word read from wordlist.txt."""
    with open("wordlist.txt", "r", encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]
    return random.choice(words)


def draw_hangman(errors):
    """Print the hangman drawing that matches the number of errors."""
    stage = min(errors, len(HANGMAN_STAGES) - 1)
    print(HANGMAN_STAGES[stage].strip("\n"))


def show_status(game):
    """Show the drawing, the guessed letters, the progress and the attempts."""
    draw_hangman(game.errors)
    if game.guessed_letters:
        guessed = ", ".join(game.guessed_letters)
    else:
        guessed = "ninguna"
    remaining = game.max_errors - game.errors
    print(f"Letras adivinadas: {guessed}")
    print("Palabra: ", end="")
    game.display_progress()
    print(f"Intentos restantes: {remaining}")