# -*- coding: utf-8 -*-
from model.address import Address


def test_add_new_kontakt(app):
    app.session.login(username="admin", password="secret")
    app.kontakt.create_address(Address("Viktor", "Prihodko", "08998899854"))
    app.session.logout()
