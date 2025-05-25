import math
import random

import numpy as np

from subcipher.analysis import calculate_plausibility
from subcipher.cipher import substitute_decrypt
from subcipher.constants import ALPHABET


def metropolis_hastings(ciphertext: str, tm_ref: np.ndarray, iterations: int = 20000, initial_temp: float = 1.0) -> tuple[str, float]:
    """
    Implements the Metropolis-Hastings algorithm with simulated annealing.

    Args:
        ciphertext: The encrypted text to decrypt
        tm_ref: Reference transition matrix
        iterations: Number of iterations to perform
        initial_temp: Initial temperature for simulated annealing

    Returns:
        tuple containing the best key found and its score
    """
    current_key = list(ALPHABET)
    random.shuffle(current_key)
    current_key = ''.join(current_key)

    current_text = substitute_decrypt(ciphertext, current_key)
    current_score = calculate_plausibility(current_text, tm_ref)

    best_key = current_key
    best_score = current_score

    min_temp = 1e-10  # Minimum temperature to prevent division by zero

    for i in range(iterations):
        temperature = max(initial_temp * (1 - i / iterations), min_temp)

        new_key = list(current_key)
        idx1, idx2 = random.sample(range(len(ALPHABET)), 2)
        new_key[idx1], new_key[idx2] = new_key[idx2], new_key[idx1]
        new_key = ''.join(new_key)

        new_text = substitute_decrypt(ciphertext, new_key)
        new_score = calculate_plausibility(new_text, tm_ref)

        score_diff = 0.0
        try:
            score_diff = new_score - current_score
            acceptance_probability = math.exp(min(score_diff / temperature, 700))  # Limit exponent to prevent overflow
        except (OverflowError, ZeroDivisionError):
            acceptance_probability = 1.0 if score_diff and score_diff  > 0 else 0.0

        if new_score > current_score or random.random() < acceptance_probability:
            current_key = new_key
            current_score = new_score

            if current_score > best_score:
                best_key = current_key
                best_score = current_score

        if (i + 1) % 500 == 0:
            print(f"\rIteration {i + 1:5d} | current score: {current_score:.4f} | best score: {best_score:.4f}", end="\033[K")

    return best_key, best_score