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


all_tables = read_pdf('Lönekollen Östersunds kommun sida 94.pdf', pages='all', output_format='json')

for number_table, table in enumerate(all_tables, start=1):
    for number_row, row in enumerate(table.get('data')[1:], start=1):
        print(row)
        print()
