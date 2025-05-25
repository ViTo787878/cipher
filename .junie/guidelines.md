# Development Guidelines for Subcrypto

This document provides guidelines and instructions for developing and maintaining the Subcrypto project, a library for substitution cipher and its breaking.

## Build/Configuration Instructions

### Environment Setup

1. **Python Version**: This project requires Python 3.13 or higher.

2. **Virtual Environment**: It's recommended to use a virtual environment for development:
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Dependencies Installation**:
   - For basic usage:
     ```powershell
     pip install -e .
     ```
   - For development (includes testing tools):
     ```powershell
     pip install -e ".[dev]"
     ```
   - Alternatively, install from requirements.txt:
     ```powershell
     pip install -r requirements.txt
     ```

### Project Structure

- `subcipher/`: Main package containing the library code
  - `cipher.py`: Core encryption/decryption functionality
  - `analysis.py`: Text analysis tools
  - `mh_solver.py`: Solver implementation
  - `utils.py`: Utility functions
  - `constants.py`: Constants used throughout the project
- `subcipher_tests/`: Test directory
- `data_samples/`: Sample data for testing and examples
- `notebooks/`: Jupyter notebooks for demonstrations

## Testing Information

### Running Tests

1. **Run all tests**:
   ```powershell
   python -m pytest
   ```

2. **Run specific test file**:
   ```powershell
   python -m pytest subcipher_tests\test_normalize.py
   ```

3. **Run tests with verbosity**:
   ```powershell
   python -m pytest -v
   ```

4. **Run tests with coverage** (requires pytest-cov):
   ```powershell
   pip install pytest-cov
   python -m pytest --cov=subcipher
   ```

### Adding New Tests

1. Create a new test file in the `subcipher_tests` directory following the naming convention `test_*.py`.

2. Structure tests in classes following the pattern in existing tests:
   ```python
   import pytest
   from subcipher.module import function_to_test

   class TestClassName:
       def test_function_name(self):
           """Test description."""
           # Arrange
           input_data = "example"
           expected = "EXAMPLE"

           # Act & Assert
           assert function_to_test(input_data) == expected
   ```

3. Use pytest fixtures for common test data (defined in `conftest.py`).

4. Use parametrized tests for testing multiple inputs:
   ```python
   @pytest.mark.parametrize("input_text,expected", [
       ("example1", "RESULT1"),
       ("example2", "RESULT2"),
   ])
   def test_parametrized(self, input_text, expected):
       assert function_to_test(input_text) == expected
   ```

### Example Test

Here's a simple test for the `normalize_text` function:

```python
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
```

## Additional Development Information

### Code Style

1. **Type Hints**: Use type hints for function parameters and return values.
   ```python
   def function_name(parameter: str) -> str:
       return parameter.upper()
   ```

2. **Docstrings**: Use descriptive docstrings for all functions and classes, following the format in existing code.
   ```python
   def function_name(parameter: str) -> str:
       """
       Short description of what the function does.

       :param parameter: Description of the parameter
       :type parameter: str
       :return: Description of the return value
       :rtype: str
       :raises ValueError: When the function might raise an exception
       """
       return parameter.upper()
   ```

3. **Code Formatting**: The project uses black and isort for code formatting. Run them before committing:
   ```powershell
   black subcipher subcipher_tests
   isort subcipher subcipher_tests
   ```

4. **Type Checking**: Use mypy for static type checking:
   ```powershell
   mypy subcipher
   ```

### Working with Text Data

1. **Text Normalization**: Use the `normalize_text` function from `utils.py` to normalize text before processing.

2. **Character Set**: The project uses a 27-character alphabet defined in `constants.py` as `ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"`, where underscore represents space.

3. **File I/O**: Use the `load_textfile` and `save_textfile` functions from `utils.py` for consistent file handling.

### Debugging Tips

1. Use the Jupyter notebooks in the `notebooks` directory for interactive debugging and experimentation.

2. For complex algorithms, add logging statements to track the execution flow.

3. When working with large texts, use smaller samples from the `data_samples` directory during development.
