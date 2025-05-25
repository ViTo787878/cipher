import pytest
from subcipher.utils import normalize_text, load_textfile, save_textfile


class TestTextProcessing:
    @pytest.mark.parametrize("input_text,expected", [
        ("ÁČÉĚŤ", "ACEET"),
        ("HELLO@WORLD!", "HELLO_WORLD"),
        ("HELLO__WORLD", "HELLO_WORLD"),
        ("ÁBCD123!@#", "ABCD"),
        ("HELLO_WORLD", "HELLO_WORLD")
    ])
    def test_text_normalization(self, input_text, expected):
        assert normalize_text(input_text) == expected

    def test_consecutive_underscores(self):
        assert normalize_text("A___B") == "A_B"

    def test_mixed_case_input(self):
        assert normalize_text("Hello World") == "HELLO_WORLD"

    def test_empty_input(self):
        assert normalize_text("") == ""


class TestFileOperations:
    def test_save_load_cycle(self, tmp_path):
        test_file = tmp_path / "test.txt"
        original_text = "TEST_TEXT"

        save_textfile(original_text, str(test_file))
        loaded_text = load_textfile(str(test_file))

        assert loaded_text == original_text

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            load_textfile("nonexistent_file.txt")