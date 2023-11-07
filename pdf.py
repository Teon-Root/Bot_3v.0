# import re
# from PyPDF2 import PdfReader
#
#
# user = 'Rasooli Abbas'
# user2 = 'Qadar Lubna'
#
# pdf_file = "Lönekollen Östersunds kommun sida 94.pdf"
# pdf = PdfReader(pdf_file)
#
#
# def find_user_in_pdf(pdf, user):
#     for page in pdf.pages:
#         page_text = page.extract_text()
#         lines = page_text.split('\n')
#         for line in lines:
#             print(line)
#             if re.search(user, line, re.I):
#                 #print(line)
#                 return line
#
# print(find_user_in_pdf(pdf, user))
# print(find_user_in_pdf(pdf, user2))
#
# result_name = find_user_in_pdf(pdf, user).split(',')
# print(result_name[0])
from tabula import read_pdf
from config import area1, area2, area3

pdf_file_path = 'Lönekollen Östersunds kommun sida 94.pdf'
user = 'Rasooli Abbas'
user2 = 'Jonsson Mikael'

tables1 = read_pdf(pdf_file_path, pages=2, output_format='json', area=area1)
tables2 = read_pdf(pdf_file_path, pages=2, output_format='json', area=area2)
tables3 = read_pdf(pdf_file_path, pages=2, output_format='json', area=area3)
all_tables = tables1 + tables2 + tables3

# for table in all_tables:
#     for row in table['data']:
#         row_text = ' '.join([entry['text'] for entry in row])
#         if user in row_text:
#             print(row_text)



