import pytest
from yougile_api import YougileApi


@pytest.fixture
def api() -> YougileApi:
    token = "IsG-1B2xwPXyBbHUwlcyHUUF45AYPFIaYimpaASCOA6f2HDJ-bNs9jFchUkhApeV"
    company_id = "62f6932b-a666-4672-b961-d3d3f4295b22"
    base_url = "https://ru.yougile.com/api-v2"
    return YougileApi(base_url, token, company_id)
