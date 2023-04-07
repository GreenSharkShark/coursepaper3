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
        dat.append(str(i.get('date'))[:10] + ' ' + str(i.get('date'))[11:19])
    return dat

