import numpy as np
import pytest
from subcipher.analysis import calculate_plausibility
from subcipher.cipher import substitute_encrypt, substitute_decrypt
from subcipher.constants import ALPHABET
from subcipher.mh_solver import metropolis_hastings


class TestMetropolisHastings:
    @pytest.fixture
    def sample_encrypted(self, sample_text, sample_key):
        return substitute_encrypt(sample_text, sample_key)

    @pytest.fixture
    def sample_transition_matrix(self):
        # Creates a dummy uniform transition matrix for testing
        size = len(ALPHABET)
        tm = np.ones((size, size)) / size
        return tm

    def test_decryption_with_dummy_data(self, sample_encrypted, sample_transition_matrix):
        # Test if a function runs successfully with dummy input values
        result_key, result_score = metropolis_hastings(
            ciphertext=sample_encrypted,
            tm_ref=sample_transition_matrix,
            iterations=1000,
            initial_temp=1.0
        )
        assert isinstance(result_key, str)
        assert len(result_key) == len(ALPHABET)
        assert isinstance(result_score, float)

    def test_output_improves(self, sample_encrypted, sample_transition_matrix):
        # Test if output plausibility score improves during iterations
        iterations = 500
        initial_result_key, initial_score = metropolis_hastings(
            ciphertext=sample_encrypted,
            tm_ref=sample_transition_matrix,
            iterations=iterations // 2,
            initial_temp=1.0
        )
        new_result_key, new_score = metropolis_hastings(
            ciphertext=sample_encrypted,
            tm_ref=sample_transition_matrix,
            iterations=iterations,
            initial_temp=1.0
        )
        assert new_score >= initial_score
