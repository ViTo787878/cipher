import math

import numpy as np

from subcipher.constants import ALPHABET


def get_bigrams(text: str) -> list[str]:
    """
    Generate a list of bigrams from the provided string.

    :param text: The input string from which bigrams are generated.
    :type text: str
    :return: A list of bigrams, where each bigram is a two-character string.
    :rtype: List[str]
    """
    return [text[i:i + 2] for i in range(len(text) - 1)]


def transition_matrix(bigrams: list[str], alphabet: str) -> np.ndarray:
    """
    Compute the transition matrix for a given list of bigrams and an alphabet.

    :param bigrams: A list of character bigrams to compute the transition frequencies.
    :param alphabet: A string representing all acceptable characters for the matrix. The order
                     of characters defines the indices used in the resulting matrix.
    :return: A 2D numpy array representing the normalized transition matrix.
    """
    n = len(alphabet)
    index = {char: i for i, char in enumerate(alphabet)}
    matrix = np.ones((n, n))

    for bigram in bigrams:
        if len(bigram) != 2:
            continue
        a, b = bigram
        if a in index and b in index:
            matrix[index[a]][index[b]] += 1

    matrix = matrix / matrix.sum()
    return matrix

def calculate_plausibility(text: str, tm_ref: np.ndarray) -> float:
    """
    Calculates the plausibility of a given text based on a transition matrix.

    This function evaluates the likelihood of a given text by analyzing its
    bigrams and using a reference transition matrix. It calculates the
    logarithmic plausibility score by summing the log probabilities of each
    bigram transition in the text. A small epsilon value is added to prevent
    logarithmic errors due to zero probabilities in the transition matrix.

    :param text: Input string for which the plausibility needs to be calculated.
    :type text: str
    :param tm_ref: A 2D numpy array representing the transition matrix, where
        each entry at row i and column j represents the transition probability
        for character i transitioning to character j.
    :type tm_ref: np.ndarray
    :return: The calculated logarithmic plausibility score of the input text.
    :rtype: float
    """
    bigrams = get_bigrams(text)

    log_plausibility = 0.0
    epsilon = 1e-10

    for bg in bigrams:
        i, j = map(lambda x: ALPHABET.index(x), bg)
        prob = tm_ref[i, j]
        log_plausibility += math.log(prob + epsilon)

    return log_plausibility