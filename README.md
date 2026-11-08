# Ahorcado (Hangman)

Juego del ahorcado para la consola, hecho en Python. El programa elige una frase al azar de `wordlist.txt` y el jugador tiene que adivinarla letra por letra.

## Cómo ejecutarlo

```
python main.py
```

## Reglas del juego

- Se elige una frase al azar de `wordlist.txt`.
- El jugador ingresa una letra por turno. Solo se aceptan letras (una sola por vez) y no se puede repetir una letra ya intentada.
- Se pierde al llegar a 6 errores.
- Los espacios y signos de puntuación se muestran automáticamente y no cuentan para ganar ni perder.
- Después de cada intento se muestran las letras adivinadas, el progreso de la frase y los intentos restantes.

## Estructura del proyecto

- `main.py`: punto de entrada. Contiene el bucle del juego y la lectura y validación de la letra.
- `game.py`: clase `HangmanGame`, que guarda el estado del juego (`word`, `guessed_letters`, `max_errors`, `errors`) y su lógica (`display_progress`, `process_guess`, `is_won`, `is_lost`).
- `utils.py`: funciones auxiliares: `get_random_word` (lee `wordlist.txt` y elige una frase) y `show_status` (muestra el estado después de cada intento).
- `wordlist.txt`: lista de frases posibles, una por línea.

## Decisiones técnicas

- El estado del juego vive en una clase, para separarlo de la entrada y la salida por consola.
- El código está dividido en módulos con una responsabilidad cada uno.
- Las letras se comparan en minúscula, así que no importa si el jugador escribe mayúsculas o minúsculas.
- `main.py` lleva su propia lista de letras intentadas, para rechazar también las letras equivocadas que se repiten.