import json
# from unittest import mock
from unittest.mock import Mock, MagicMock
from app import api


def test_hello(client):

    response = client.get()

    assert response.status_code == 200


def test_emp(client):

    response = client.get()
    resp_json = json.loads(response.data)

    assert resp_json['emp'] == {'first_name': 'Vikram', 'last_name': 'Shinde'}


def test_employee_id(client):

    resp = client.get('/1234')

    assert resp.status_code == 200
    assert json.loads(resp.data) == {'emp': '1234'}


def test_empl_mock(client):
    api._get_by_employee_id = MagicMock(return_value=1111)
    resp = client.get('/1234')

    assert resp.status_code == 200
    assert json.loads(resp.data) == {'emp': 1111}



