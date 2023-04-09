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
    sorted_date = sorted(dat, reverse=True)

    last_five_operations = []
    counter = 0
    for a in range(len(sorted_date)):
        for i in content:
            if counter >= 5:
                break
            if datetime.fromisoformat(i['date'][:10] + ' ' + i['date'][11:19]) == datetime.fromisoformat(sorted_date[a]) and i['state'] == 'EXECUTED':
                last_five_operations.append(i)
                counter += 1
    return last_five_operations
