import pytest
from subcipher.cipher import substitute_encrypt, substitute_decrypt
from subcipher.constants import ALPHABET


class TestSubstitutionCipher:
    def test_basic_encryption(self, sample_text, sample_key, sample_encrypted):
        assert substitute_encrypt(sample_text, sample_key) == sample_encrypted

    def test_basic_decryption(self, sample_text, sample_key, sample_encrypted):
        assert substitute_decrypt(sample_encrypted, sample_key) == sample_text

    def test_empty_input(self, sample_key):
        assert substitute_encrypt("", sample_key) == ""
        assert substitute_decrypt("", sample_key) == ""

    @pytest.mark.parametrize("invalid_key", [
        "ABC",  # Too short
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ_1",  # Invalid character
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",  # Missing underscore
    ])
    def test_invalid_keys(self, invalid_key, sample_text):
        with pytest.raises(ValueError):
            substitute_encrypt(sample_text, invalid_key)

    def test_case_insensitivity(self, sample_key, sample_encrypted):
        lower_input = "hello_world"
        assert substitute_encrypt(lower_input, sample_key) == sample_encrypted

    def test_identity_transformation(self):
        # Encryption with ALPHABET as key should return the same text
        text = "TEST_TEXT"
        assert substitute_encrypt(text, ALPHABET) == text

    def test_encryption_decryption_cycle(self, sample_text, sample_key):
        encrypted = substitute_encrypt(sample_text, sample_key)
        decrypted = substitute_decrypt(encrypted, sample_key)
        assert decrypted == sample_text