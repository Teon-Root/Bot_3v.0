import os
from PyPDF2 import PdfReader
from config import base_folder


def find_name_in_pdf(file_path):
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if "KLAGANDE" in page_text:
                index_klagande = page_text.index("KLAGANDE")
                name = page_text[index_klagande + 9:].split(',')[0].strip()
                return name

    return None


def find_and_print_names(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                name = find_name_in_pdf(pdf_path)
                if name:
                    print(f"Файл: {pdf_path}, Имя: {name}")


find_and_print_names(base_folder)
