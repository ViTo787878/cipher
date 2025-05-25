import pytest
from subcipher.utils import normalize_text

class TestNormalizeText:
    def test_basic_normalization(self):
        """Test basic text normalization functionality."""
        input_text = "Hello World!"
        expected = "HELLO_WORLD_"
        assert normalize_text(input_text) == expected

    def test_czech_diacritics(self):
        """Test normalization of Czech diacritics."""
        input_text = "Příliš žluťoučký kůň úpěl ďábelské ódy"
        expected = "PRILIS_ZLUTOUCKY_KUN_UPEL_DABELSKE_ODY"
        assert normalize_text(input_text) == expected

    def test_multiple_spaces(self):
        """Test collapsing of multiple spaces."""
        input_text = "Hello   World"
        expected = "HELLO_WORLD"
        assert normalize_text(input_text) == expected

    def test_empty_string(self):
        """Test normalization of an empty string."""
        assert normalize_text("") == ""
