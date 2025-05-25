import math

from PyPDF2 import PdfReader

from subcipher.constants import ALPHABET


def load_pdf(file_path: str) -> str:
    with open(file_path, 'rb') as file:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text


def load_text(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_text(text: str, output_path: str) -> None:
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)


def normalize_text(text: str) -> str:
    replacements = {
        'Á': 'A', 'Č': 'C', 'Ď': 'D', 'É': 'E', 'Ě': 'E',
        'Í': 'I', 'Ň': 'N', 'Ó': 'O', 'Ř': 'R', 'Š': 'S',
        'Ť': 'T', 'Ú': 'U', 'Ů': 'U', 'Ý': 'Y', 'Ž': 'Z'
    }

    normalized = text
    for char, replacement in replacements.items():
        normalized = normalized.replace(char, replacement)

    normalized = ''.join('_' if char not in ALPHABET else char for char in normalized)
    while '__' in normalized:
        normalized = normalized.replace('__', '_')

    return normalized

def convert_pdf_to_text(input_pdf: str, output_txt: str) -> None:
    text = load_pdf(input_pdf)
    save_text(text, output_txt)


def log_to_percentage(log_value: float) -> float:
    if math.isinf(log_value) and log_value < 0:
        return 100.0
    elif log_value >= 1:
        return 0.0

    return 100 * (1 / (1 + math.exp(log_value)))
