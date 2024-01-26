import json

from datetime import datetime


def sort_operations():
    """Функция сортирует json файл"""


    with open("operations.json", "r", encoding='utf8') as json_file:
        operations = json.load(json_file)
    operations_sort = [item for item in operations if item.get('state') == "EXECUTED"]
    operations_sort.sort(key=lambda x: x.get('date'), reverse=True)

    return operations_sort


def return_last_operations(operations_sort):
    """Функция возвращает список последних 5 операций"""


    result_operations = []
    for item in operations_sort[0:5]:
        result_operations.append(item)

    return result_operations


def format_output_data(item):
    """Функция преобразует доту в формат %d.%m.%Y и возвращает полуенное значение"""


    output_data = datetime.strftime(datetime.strptime(item.split('T')[0], '%Y-%m-%d'), '%d.%m.%Y')
    return output_data
def format_private_num(item):
    """Функция возвращает номер карты/счета в приватном виде"""

    private_num = item.split()[-1]
    name = ' '.join(item.split()[:-1])
    if len(private_num) == 16:
        private_num = name + ' ' + private_num[0:4] + ' ' + private_num[5:7] + '** **** ' + private_num[-4:]
    else:
        private_num = name + ' ' + '**' + private_num[-4:]

    return private_num
