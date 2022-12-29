import re
from fpdf import FPDF

def get_array():
    with open('Список сообщений клиента.txt', 'r', encoding='utf=8') as file:
        text = file.readlines()
    return text


def edit_array():
    new_list = []
    REGEXP1 = re.compile(r'справк[а-яА-Я]?|расторжени[а-яА-Я]?|закрыти[а-яА-Я]?|документ[а-яА-Я]?')
    REGEXP2 = re.compile(r'открыти[а-яА-Я]?|номер[а-яА-Я]')
    for i in get_array():
        result = REGEXP1.search(i)
        result2 = REGEXP2.search(i)
        if result and not result2:
            new_list.append(i)
        else:
            continue
    return new_list


def get_ready_file():
    with open('готовый список.txt', 'w', encoding='utf8') as f:
        f.write(''.join(edit_array()))




