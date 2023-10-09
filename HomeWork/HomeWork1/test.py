from REST_API import get, get_new_post
import pytest
import yaml


def test_step1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el["id"] for el in lst]
    assert 82139 in lst_id


def test_step2(get_token):
    with open('config.yaml', 'r') as f:
        conf = yaml.safe_load(f)
    result = get_new_post(get_token)
    lst = result['data']
    lst_description = [el["description"] for el in lst]
    # print(lst_description)
    assert conf["description"] in lst_description


if __name__ == "__main__":
    pytest.main(['-vv'])
