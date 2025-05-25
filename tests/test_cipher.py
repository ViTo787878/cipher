from subcipher import substitute_encrypt, substitute_decrypt


def test_basic_encryption_decryption():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    key = alphabet[::-1]  # reverzní klíč
    text = "HELLO_WORLD"
    encrypted = substitute_encrypt(text, key)
    decrypted = substitute_decrypt(encrypted, key)
    assert decrypted == text
