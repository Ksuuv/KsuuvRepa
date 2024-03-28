import requests
import pytest

    # Получение полного листа устройств (GET)
def test_get_full_list():
    get_full_list = requests.get('https://api.restful-api.dev/objects').json()
    assert len(get_full_list) == 13

    # Создание своего устройства (POST)
def test_create_obj():
    new_obj = {
        "name": "XIAOMI REDMI NOTE 8 PRO",
        "data": {
            "year": 2019,
            "price": 199.99,
            "CPU model": "Mediatek Helio G90T",
            "Hard disk size": "128 GB"
        }
    }

    create_obj = requests.post('https://api.restful-api.dev/objects', json=new_obj).json()
    print(create_obj)
    id_new_obj = create_obj['id']
    find_new_obj = requests.get(f'https://api.restful-api.dev/objects/{id_new_obj}').json()
    print(find_new_obj)
    assert new_obj['name'] == find_new_obj['name']
    assert new_obj['data'] == find_new_obj['data']
    return id_new_obj

@pytest.fixture(scope="module")
def object_id():
    id_new_obj = test_create_obj()
    return id_new_obj

    # Изменение созданного устройства (PUT)
def test_updated_obj(object_id):
    id_new_obj = object_id

    updated_obj = {
        "name": "XIAOMI REDMI NOTE 13 PRO",
        "data": {
            "year": 2020,
            "price": 555.99,
            "CPU model": "Mediatek Helio G90T",
            "Hard disk size": "512 GB"
        }
    }

    update_obj = requests.put(f'https://api.restful-api.dev/objects/{id_new_obj}', json=updated_obj).json()
    print(update_obj)
    assert updated_obj['name'] == update_obj['name']
    assert updated_obj['data'] == update_obj['data']

    # Удаление созданного устройства (DELETE)
def test_delete_obj(object_id):
    id_new_obj = object_id
    delete_obj = requests.delete(f'https://api.restful-api.dev/objects/{id_new_obj}')
    assert delete_obj.status_code == 200
    get_del_obj = requests.get(f'https://api.restful-api.dev/objects/{id_new_obj}')
    assert get_del_obj.status_code == 404
    print(get_del_obj)
