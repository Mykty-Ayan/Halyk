import re

from typing import List

from PyPDF2 import PdfFileReader


def read_pdf(file_name: str):
    with open(file_name, 'rb') as file:
        pdf_reader = PdfFileReader(file)
        scores_sum = 0
        for page in range(pdf_reader.getNumPages()):
            pdf_page = pdf_reader.getPage(page)
            text = pdf_page.extractText().replace('\n', '')
            in_parentheses = re.findall(r'\([^()]*\)', text)
            scores_sum += get_score(in_parentheses)

    print(f'Sum of all tasks score: {scores_sum}')


def get_score(parentheses_list: List[str]):
    score = 0
    for item in parentheses_list:
        if re.match(r'^\([0-9]+ \w+\)$',  item):
            score += int(item[1])

    return score


if __name__ == '__main__':
    read_pdf('Theoretical Part of the Final Exam.pdf')
