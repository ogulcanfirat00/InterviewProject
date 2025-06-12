import pytest
from reqres_client import ReqresClient

@pytest.fixture(scope="module")
def api_client():
    return ReqresClient()