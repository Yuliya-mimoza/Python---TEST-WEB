from REST_API import get
import pytest


def test_step1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el["id"] for el in lst]
    assert 61151 in lst_id


if __name__ == "__main__":
    pytest.main(['-vv'])
