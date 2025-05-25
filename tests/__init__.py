import pytest
import numpy as np
from subcipher.constants import ALPHABET

@pytest.fixture(scope="session")
def reference_matrix():
    size = len(ALPHABET)
    return np.ones((size, size)) / (size * size)

@pytest.fixture
def test_data_path(tmp_path):
    return tmp_path / "test_data"