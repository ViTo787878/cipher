import math
import random
import numpy as np
from subcipher.cipher import substitute_decrypt
from subcipher.analysis import plausibility, calculate_plausibility
from subcipher.constants import ALPHABET


def metropolis_hastings(ciphertext: str, tm_ref: np.ndarray, iterations: int = 20000) -> tuple[str, float]:
    # Počáteční náhodný klíč
    current_key = list(ALPHABET)
    random.shuffle(current_key)
    current_key = ''.join(current_key)

    # Počáteční dekódování a skóre
    current_text = substitute_decrypt(ciphertext, current_key)
    current_score = calculate_plausibility(current_text, tm_ref)

    best_key = current_key
    best_score = current_score

    # Parametry pro simulované žíhání
    initial_temp = 1.0

    for i in range(iterations):
        # Snižování teploty
        temperature = initial_temp * (1 - i / iterations)

        # Generování nového kandidátního řešení
        new_key = list(current_key)
        idx1, idx2 = random.sample(range(len(ALPHABET)), 2)
        new_key[idx1], new_key[idx2] = new_key[idx2], new_key[idx1]
        new_key = ''.join(new_key)

        # Vyhodnocení kandidáta
        new_text = substitute_decrypt(ciphertext, new_key)
        new_score = calculate_plausibility(new_text, tm_ref)

        # Metropolis kritérium s teplotou
        acceptance_probability = math.exp((new_score - current_score) / temperature)

        if new_score > current_score or random.random() < acceptance_probability:
            current_key = new_key
            current_score = new_score

            if current_score > best_score:
                best_key = current_key
                best_score = current_score

        if (i + 1) % 500 == 0:
            print(f"Iterace {i + 1} | aktuální skóre: {current_score:.4f} | nejlepší skóre: {best_score:.4f}")

    return best_key, best_score