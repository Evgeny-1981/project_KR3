import json
from datetime import datetime


def sort_operations(file):
    """Функция сортирует json файл"""

    with open(file, "r", encoding='utf8') as file_json:
        operations = json.load(file_json)
    operations_sort = [item for item in operations if item.get('state') == "EXECUTED" and item.get('from') is not None]
    operations_sort.sort(key=lambda x: x.get('date'), reverse=True)

    return operations_sort


def return_last_operations(operations_sort):
    """Функция возвращает список последних 5 операций"""

    result_operations = [item for item in operations_sort[0:5]]

    return result_operations


def format_output_date(item):
    """Функция преобразует доту в формат %d.%m.%Y и возвращает полуенное значение"""

    output_data = datetime.strftime(datetime.strptime(item.split('T')[0], '%Y-%m-%d'), '%d.%m.%Y')

    return output_data


def format_account_number(item):
    """Функция возвращает номер карты/счета в приватном виде"""

    account_number = item.split()[-1]
    name = ' '.join(item.split()[:-1])
    if len(account_number) == 16:
        account_number = name + ' ' + account_number[0:4] + ' ' + account_number[5:7] + '** **** ' + account_number[-4:]
    elif len(account_number) == 20:
         account_number = name + ' ' + '**' + account_number[-4:]
    else:
        account_number = 'Неверный или отсутствует номер/счет'

    return account_number
