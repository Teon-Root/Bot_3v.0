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
import json
import codecs

pdf_file_path = 'Lönekollen Östersunds kommun sida 94.pdf'
user = 'Rasooli Abbas'
user2 = 'Jonsson Mikael'

tables1 = read_pdf(pdf_file_path, pages=2, output_format='json', area=area1)
tables2 = read_pdf(pdf_file_path, pages=2, output_format='json', area=area2)
tables3 = read_pdf(pdf_file_path, pages=2, output_format='json', area=area3)
all_tables = tables1 + tables2 + tables3



# if tables3 and 'data' in tables3[0]:
#     first_table = tables3[0]['data']
#     for index, row in enumerate(first_table):
#         print(index)
# if tables3 and 'data' in tables3[0]:
#     first_table = tables3[0]['data']
#     len(first_table)
#     if first_table:
#         first_row = first_table[1]
#         print(codecs.decode(json.dumps(first_row, indent=4),'unicode_escape'))
def pdfup(user):
    if tables3 and 'data' in tables3[0]:
        first_table = tables3[0]['data']
        for index, row in enumerate(first_table):
            for json in row:
                if user in json['text']:
                    #print(row)
                    return row


texts = {}
row = pdfup('Rebello Angelina')
texts["name"] = row[0] ["text"]
texts["empty"] = row[1] ["text"]
texts["IA"] = row[2] ["text"]
texts["LR"] = row[3] ["text"]
texts["BA"] = row[4] ["text"]
texts["Lon"] = row[5] ["text"]
texts["kapital"] = row[6] ["text"]
print(texts["name"])
print(texts["IA"])
print(texts["LR"])
print(texts["BA"])
print(texts["Lon"])
print(texts["kapital"])