import random


def get_random_word():
    """Return a random word read from wordlist.txt."""
    with open("wordlist.txt", "r", encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]
    return random.choice(words)

def show_status(game):
    """Show the guessed letters, the word progress and the remaining attempts."""
    if game.guessed_letters:
        guessed = ", ".join(game.guessed_letters)
    else:
        guessed = "ninguna"
    remaining = game.max_errors - game.errors
    print(f"Letras adivinadas: {guessed}")
    print("Palabra: ", end="")
    game.display_progress()
    print(f"Intentos restantes: {remaining}")