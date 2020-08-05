from fixture.application import Application
import pytest
from fixture1.application1 import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

