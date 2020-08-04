# -*- coding: utf-8 -*-
import pytest
from model1.address import Address
from fixture1.application1 import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.newsession.login(username="admin", password="secret")
    app.kontakt.create_address(Address("Viktor", "Prihodko", "08998899854"))
    app.newsession.logout()
