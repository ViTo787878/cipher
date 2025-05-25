from subcipher.constants import ALPHABET


def substitute_encrypt(text: str, key: str) -> str:
    if len(key) != 27 or sorted(key) != sorted(ALPHABET):
        raise ValueError("Klíč musí být permutace znaků A-Z a _")

    text = text.upper()
    trans_table = str.maketrans(ALPHABET, key)

    return text.translate(trans_table)

def substitute_decrypt(text: str, key: str) -> str:

    if len(key) != 27 or sorted(key) != sorted(ALPHABET):
        raise ValueError("Klíč musí být permutace znaků A-Z a _")

    text = text.upper()
    trans_table = str.maketrans(key, ALPHABET)

    return text.translate(trans_table)