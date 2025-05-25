import pytest
from subcipher.constants import ALPHABET

@pytest.fixture
def sample_key():
    return "BCDEFGHIJKLMNOPQRSTUVWXYZA_"

@pytest.fixture
def sample_text():
    return "HELLO_WORLD"

@pytest.fixture
def sample_encrypted():
    return "IFMMP_XPSME"

@pytest.fixture
def complex_key():
    return "VLZODTQHUXWSERMCFKNYIBJGP_A"