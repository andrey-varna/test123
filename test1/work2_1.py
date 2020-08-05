# -*- coding: utf-8 -*-
from model1.address import Address


def test_untitled_test_case(app):
    app.newsession.login(username="admin", password="secret")
    app.kontakt.create_address(Address("Viktor", "Prihodko", "08998899854"))
    app.newsession.logout()
