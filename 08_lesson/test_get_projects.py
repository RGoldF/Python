from yougile_api import YougileApi


def test_get_project_positive(api: YougileApi):
    project_id = api.create_project("Another project").json()["id"]

    response = api.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["title"] == "Another project"


def test_get_project_negative_invalid_id(api: YougileApi):
    # Несуществующий ID
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(fake_id)
    assert response.status_code == 404
