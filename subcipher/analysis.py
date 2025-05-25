import numpy as np

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


def plausibility(text: str, TM_ref: np.ndarray, alphabet: str) -> float:
    """
    Spočítá věrohodnostní skóre textu vůči referenční bigramové matici.

    Args:
        text: Dešifrovaný text
        TM_ref: Referenční relativní bigramová matice
        alphabet: Používaná abeceda

    Returns:
        Log-likelihood skóre (float)
    """
    TM_obs = transition_matrix(get_bigrams(text), alphabet)
    likelihood = np.sum(np.log(TM_ref) * TM_obs)
    return likelihood