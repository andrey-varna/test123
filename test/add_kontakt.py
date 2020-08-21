# -*- coding: utf-8 -*-
from model.address import Address


def test_add_new_kontakt(app):
    app.kontakt.create_address(Address("Viktor", "Prihodko", "08998899854"))

