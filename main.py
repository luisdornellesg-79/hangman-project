from game import HangmanGame
from utils import get_random_word, show_status


def ask_letter(tried_letters):
    """Ask the player for a letter until a valid one is entered."""
    while True:
        letter = input("Ingresa una letra: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada invalida: ingresa una sola letra.")
        elif letter in tried_letters:
            print("Ya intentaste esa letra. Prueba con otra.")
        else:
            return letter


def main():
    """Play a full game until the player wins or loses."""
    game = HangmanGame(get_random_word())
    tried_letters = []
    show_status(game)
    while not game.is_won() and not game.is_lost():
        letter = ask_letter(tried_letters)
        tried_letters.append(letter)
        if game.process_guess(letter):
            print("Bien! La letra esta en la frase.")
        else:
            print("Esa letra no esta en la frase.")
        show_status(game)
    if game.is_won():
        print("¡Ganaste!")
    else:
        print("Fin del juego")
        print(f"La frase era: {game.word}")


if __name__ == "__main__":
    main()