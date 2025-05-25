import math
import os

from subcipher.constants import ALPHABET


def load_textfile(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_textfile(text: str, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)


def normalize_text(text: str) -> str:
    text = text.upper()

    # Replace Czech diacritics
    replacements = {
        'Á': 'A', 'Č': 'C', 'Ď': 'D', 'É': 'E', 'Ě': 'E',
        'Í': 'I', 'Ň': 'N', 'Ó': 'O', 'Ř': 'R', 'Š': 'S',
        'Ť': 'T', 'Ú': 'U', 'Ů': 'U', 'Ý': 'Y', 'Ž': 'Z'
    }

    normalized = text
    for char, replacement in replacements.items():
        normalized = normalized.replace(char, replacement)

    normalized = ''.join(char if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' else '_'
                         for char in normalized)

    while '__' in normalized:
        normalized = normalized.replace('__', '_')

    return normalized


def log_to_percentage(log_value: float) -> float:
    if math.isinf(log_value) and log_value < 0:
        return 100.0
    elif log_value >= 1:
        return 0.0

    return 100 * (1 / (1 + math.exp(log_value)))
