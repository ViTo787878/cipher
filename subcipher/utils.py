import os
from PyPDF2 import PdfReader

def load_pdf(file_path: str) -> str:
    with open(file_path, 'rb') as file:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_text(text: str, output_path: str) -> None:
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

def convert_pdf_to_text(input_pdf: str, output_txt: str) -> None:
    text = load_pdf(input_pdf)
    save_text(text, output_txt)


if __name__ == "__main__":
    input_file = "../krakatit.pdf"
    output_file = "../data_samples/krakatit.txt"

    try:
        convert_pdf_to_text(input_file, output_file)
    except Exception as e:
        print(f"Error: {str(e)}")
