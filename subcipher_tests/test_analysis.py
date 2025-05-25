import numpy as np
import pytest
from subcipher.analysis import calculate_plausibility, get_bigrams
from subcipher.analysis import get_bigrams, transition_matrix
from subcipher.constants import ALPHABET


class TestCalculatePlausibility:
    def test_basic_calculation(self):
        text = "HELLO"
        tm_ref = np.full((len(ALPHABET), len(ALPHABET)), 0.01)  # Simple uniform matrix
        assert calculate_plausibility(text, tm_ref) < 0, "Should calculate negative log plausibility."

    def test_empty_text(self):
        text = ""
        tm_ref = np.full((len(ALPHABET), len(ALPHABET)), 0.01)
        assert calculate_plausibility(text, tm_ref) == 0.0, "Empty text should yield zero plausibility."

    def test_all_invalid_bigrams(self):
        text = "12345!"
        tm_ref = np.full((len(ALPHABET), len(ALPHABET)), 0.01)
        with pytest.raises(ValueError):
            calculate_plausibility(text, tm_ref)

    def test_realistic_transition_matrix(self):
        text = "ABAB"
        tm_ref = np.zeros((len(ALPHABET), len(ALPHABET)))
        tm_ref[ALPHABET.index("A")][ALPHABET.index("B")] = 0.5
        tm_ref[ALPHABET.index("B")][ALPHABET.index("A")] = 0.5
        assert calculate_plausibility(text, tm_ref) < 0, "Should handle realistic matrices correctly."

    def test_repeated_bigrams(self):
        text = "AAAA"
        tm_ref = np.full((len(ALPHABET), len(ALPHABET)), 0.01)
        assert calculate_plausibility(text, tm_ref) < 0, "Repeated bigrams should penalize plausibility score."

    def test_unnormalized_input(self):
        text = "aaa"
        tm_ref = np.full((len(ALPHABET), len(ALPHABET)), 0.01)
        with pytest.raises(ValueError):
            calculate_plausibility(text, tm_ref)

class TestGetBigrams:
    def test_basic_bigrams(self):
        text = "hello"
        expected_bigrams = ["he", "el", "ll", "lo"]
        assert get_bigrams(text) == expected_bigrams

    def test_empty_string(self):
        text = ""
        expected_bigrams = []
        assert get_bigrams(text) == expected_bigrams

    def test_single_character(self):
        text = "a"
        expected_bigrams = []
        assert get_bigrams(text) == expected_bigrams

    def test_non_alpha_characters(self):
        text = "12345!"
        expected_bigrams = ["12", "23", "34", "45", "5!"]
        assert get_bigrams(text) == expected_bigrams

    def test_repeated_characters(self):
        text = "aaa"
        expected_bigrams = ["aa", "aa"]
        assert get_bigrams(text) == expected_bigrams

    def test_whitespace_in_text(self):
        text = "a b c"
        expected_bigrams = ["a ", " b", "b ", " c"]
        assert get_bigrams(text) == expected_bigrams

    def test_unicode_characters(self):
        text = "こんにちは"
        expected_bigrams = ["こん", "んに", "にち", "ちは"]
        assert get_bigrams(text) == expected_bigrams

    def test_mixed_characters(self):
        text = "ab12@#"
        expected_bigrams = ["ab", "b1", "12", "2@", "@#"]
        assert get_bigrams(text) == expected_bigrams

class TestTransitionMatrix:
    def test_basic_bigrams_matrix(self):
        bigrams = ["ab", "bc", "cc"]
        expected_matrix_shape = (len(ALPHABET), len(ALPHABET))
        result_matrix = transition_matrix(bigrams, ALPHABET)
        assert result_matrix.shape == expected_matrix_shape

    def test_empty_bigrams_matrix(self):
        bigrams = []
        expected_matrix = transition_matrix(bigrams, ALPHABET)
        assert (expected_matrix > 0).all(), "Matrix should be initialized with smoothing."

    # FIXME - Add guard statements to the methods pls
    # def test_invalid_bigrams_matrix(self):
    #     bigrams = ["a1", "!", "##"]
    #     expected_matrix = transition_matrix(bigrams, ALPHABET)
    #     assert (expected_matrix.sum() - (
    #                 len(ALPHABET) ** 2)) > 0, "Invalid bigrams should not affect matrix initialization."
    #
    # def test_large_bigrams_input(self):
    #     bigrams = ["ab"] * 1000
    #     result_matrix = transition_matrix(bigrams, ALPHABET)
    #     assert result_matrix[ALPHABET.index("a")][
    #                ALPHABET.index("b")] > 1, "Frequent bigrams should increment correctly."
    #
    # def test_bigrams_with_repeated_letters(self):
    #     bigrams = ["aa", "aa", "bb"]
    #     result_matrix = transition_matrix(bigrams, ALPHABET)
    #     assert result_matrix[ALPHABET.index("a")][ALPHABET.index("a")] > 1, "Matrix should handle repeated bigrams."