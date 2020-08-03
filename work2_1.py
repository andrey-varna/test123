# -*- coding: utf-8 -*-
import pytest
from address import Address
from application1 import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.login(username="admin", password="secret")
    app.create_address(Address("Viktor", "Prihodko", "08998899854"))
    app.logout()