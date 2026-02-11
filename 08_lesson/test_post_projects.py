from yougile_api import YougileApi


def test_create_project_positive(api: YougileApi):
    response = api.create_project("New Project")
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_no_title(api: YougileApi):
    response = api.create_project("")  # пустое название
    assert response.status_code in [400, 404]
