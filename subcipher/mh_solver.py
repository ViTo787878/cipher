import random
import numpy as np
from subcipher.cipher import substitute_decrypt
from subcipher.analysis import plausibility

def generate_random_key(alphabet: str) -> str:
    """
    Vygeneruje náhodnou permutaci klíče.
    """
    key_list = list(alphabet)
    random.shuffle(key_list)
    return ''.join(key_list)

def swap_random(key: str) -> str:
    """
    Vrátí nový klíč s prohozenými dvěma náhodnými znaky.
    """
    key_list = list(key)
    i, j = random.sample(range(len(key_list)), 2)
    key_list[i], key_list[j] = key_list[j], key_list[i]
    return ''.join(key_list)

def prolom_substitute(text: str, TM_ref: np.ndarray, iter: int, alphabet: str, start_key: str = None):
    """
    Metropolis-Hastings algoritmus pro kryptoanalýzu substituční šifry.

    Args:
        text: zašifrovaný text
        TM_ref: referenční matice přechodů (relativní)
        iter: počet iterací
        alphabet: abeceda (např. ABC...Z_)
        start_key: volitelný výchozí klíč (jinak náhodný)

    Returns:
        Tuple (nejlepší_klíč, dešifrovaný_text, skóre)
    """
    if start_key is None:
        current_key = generate_random_key(alphabet)
    else:
        current_key = start_key

    decrypted_current = substitute_decrypt(text, current_key)
    p_current = plausibility(decrypted_current, TM_ref, alphabet)

    best_key = current_key
    best_score = p_current
    best_decryption = decrypted_current

    for i in range(1, iter + 1):
        candidate_key = swap_random(current_key)
        decrypted_candidate = substitute_decrypt(text, candidate_key)
        p_candidate = plausibility(decrypted_candidate, TM_ref, alphabet)

        q = np.exp(p_candidate - p_current)

        if q > 1 or random.random() < q:
            current_key = candidate_key
            p_current = p_candidate

            if p_current > best_score:
                best_key = current_key
                best_score = p_current
                best_decryption = decrypted_candidate

        if i % 500 == 0:
            print(f"Iterace {i} | aktuální skóre: {p_current:.4f} | nejlepší skóre: {best_score:.4f}")

    return best_key, best_decryption, best_score
