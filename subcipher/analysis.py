import math

import numpy as np

from subcipher.constants import ALPHABET


def get_bigrams(text: str) -> list[str]:
    """
    Vytvoří seznam bigramů (dvou po sobě jdoucích znaků) z textu.

    Args:
        text: Vstupní text (velká písmena + _)

    Returns:
        Seznam bigramů jako dvouznakových řetězců
    """
    return [text[i:i + 2] for i in range(len(text) - 1)]


def transition_matrix(bigrams: list[str], alphabet: str) -> np.ndarray:
    """
    Vytvoří matici přechodů (bigramová matice) ze seznamu bigramů.

    Args:
        bigrams: Seznam bigramů
        alphabet: Abeceda (např. 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_')

    Returns:
        2D numpy pole velikosti 27x27 s relativní četností výskytu bigramů
    """
    n = len(alphabet)
    index = {char: i for i, char in enumerate(alphabet)}
    matrix = np.ones((n, n))  # Inicializace s 1 kvůli log(0)

    for bigram in bigrams:
        if len(bigram) != 2:
            continue
        a, b = bigram
        if a in index and b in index:
            matrix[index[a]][index[b]] += 1

    matrix = matrix / matrix.sum()  # Normalizace na relativní četnosti
    return matrix

def calculate_plausibility(text: str, tm_ref: np.ndarray) -> float:
    bigrams = get_bigrams(text)

    log_plausibility = 0.0
    epsilon = 1e-10

    for bg in bigrams:
        i, j = map(lambda x: ALPHABET.index(x), bg)
        prob = tm_ref[i, j]
        log_plausibility += math.log(prob + epsilon)

    return log_plausibility