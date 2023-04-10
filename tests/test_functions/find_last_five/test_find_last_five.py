from coursepaper3.functions import find_last_five
import json


def test_find_last_five():
    with open('tests/test_functions/result.json', encoding='utf8') as file:
        result_json = json.load(file)

    with open('operations/operations.json', encoding='utf8') as file:
        json_content = json.load(file)

    assert find_last_five(json_content) == result_json
