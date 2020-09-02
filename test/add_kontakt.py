# -*- coding: utf-8 -*-
from model.address import Address


def test_add_new_kontakt(app):
    old_kontakts = app.kontakt.get_kontakt_list()
    kontakt = Address("Viktor", "Prihodko", "08998899854")
    app.kontakt.create_address(kontakt)
    assert len(old_kontakts) + 1 == app.kontakt.count()
    new_kontakts = app.kontakt.get_kontakt_list()
    old_kontakts.append(kontakt)
    assert sorted(old_kontakts, key=Address.id_or_max) == sorted(new_kontakts, key=Address.id_or_max)

