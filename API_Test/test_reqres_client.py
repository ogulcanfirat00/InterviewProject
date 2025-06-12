def test_reqres_client(api_client):
    # CREATE
    payload = {"name": "ogulcan", "job": "qa engineer"}
    res = api_client.create_user(payload)
    assert res.status_code == 201
    user_id = res.json().get("id")
    assert user_id is not None

    # READ
    res = api_client.get_user(user_id)
    assert res.status_code in [200, 404]

    # UPDATE
    updated_payload = {"name": "neo", "job": "the one"}
    res = api_client.update_user(user_id, updated_payload)
    assert res.status_code == 200

    # DELETE
    res = api_client.delete_user(user_id)
    assert res.status_code == 204
