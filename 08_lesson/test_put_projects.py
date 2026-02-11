from yougile_api import YougileApi


def test_update_project_positive(api: YougileApi):
    project_id = api.create_project("Old Title").json()["id"]

    response = api.update_project(project_id, "New Title")
    assert response.status_code == 200

    check = api.get_project(project_id).json()
    assert check["title"] == "New Title"


def test_update_project_negative_wrong_id(api: YougileApi):
    response = api.update_project("not-a-valid-id", "New Title")
    assert response.status_code == 404
