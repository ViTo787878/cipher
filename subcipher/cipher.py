from subcipher.constants import ALPHABET


def substitute_encrypt(text: str, key: str) -> str:
    """
    Encrypts the given plaintext using a substitution cipher based on the provided key.
    The key must be a permutation of the defined `ALPHABET`. The function substitutes
    each character of the plaintext with the corresponding character in the given key
    based on the position within the `ALPHABET`. Input text is first converted to uppercase
    before the substitution process.

    :param text: The plaintext string to be encrypted.
    :type text: str
    :param key: A 27-character string that represents a permutation of the defined `ALPHABET`.
                It is used as the substitution cipher key.
    :type key: str
    :return: The encrypted string after substitution based on the key.
    :rtype: str
    :raises ValueError: If the key is not a permutation of the defined `ALPHABET`.
    """
    if len(key) != 27 or sorted(key) != sorted(ALPHABET):
        raise ValueError("Key has to be a permutation of " + ALPHABET)

    text = text.upper()
    trans_table = str.maketrans(ALPHABET, key)

    return text.translate(trans_table)

def substitute_decrypt(text: str, key: str) -> str:
    """
    Decrypts a text encrypted with a substitution cipher using a given key.

    This function decrypts the given `text` using a substitution cipher,
    based on the provided `key`. The key must be a valid permutation of
    the defined alphabet, including space (denoted by `ALPHABET`). The text
    will be converted to uppercase, then characters are mapped back to the
    original alphabet using the translation table generated from the key.

    :param text: The encrypted text to be decrypted.
    :type text: str
    :param key: The substitution cipher key that is a permutation of the
        complete alphabet including a space.
    :type key: str
    :return: The decrypted text where each character in the input
        `text` has been replaced using the provided cipher `key`.
    :rtype: str
    :raises ValueError: If the `key` is not exactly 27 characters long or
        is not a valid permutation of the defined alphabet including space.
    """
    if len(key) != 27 or sorted(key) != sorted(ALPHABET):
        raise ValueError("Key has to be a permutation of " + ALPHABET)

    text = text.upper()
    trans_table = str.maketrans(key, ALPHABET)

    return text.translate(trans_table)