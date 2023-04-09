import json
from datetime import datetime


def get_json():
    """
    open json file and return content
    :return: json file content
    """
    with open('../operations/operations.json', encoding='utf8') as file:
        content = json.load(file)
    return content


def find_last_five(content):
    "находит все строки с датами и форматирует из чтобы можно было работать с ними с помощью библиотеки"
    dat = []
    for i in content:
        dat.append(i['date'][:10] + ' ' + i['date'][11:19])
    sorted_date = sorted(dat)
    last_five_operations = []
    a = -1
    for i in content:
        while a > -5:
            if i['date'][:10] == sorted_date[a][:10] and i['date'][11:19] == sorted_date[a][11:19] and i['state'] == 'EXECUTED':
                 last_five_operations.append(i)
                 a -= 1

    return last_five_operations
