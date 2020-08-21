from model.address import Address


def test_modify_kontakt_name(app):
    app.kontakt.modify_first_kontakt(Address(firstname="New kontakt"))


def test_modify_group_lastname(app):
    app.kontakt.modify_first_kontakt(Address(lastname="New lastname"))


def test_modify_group_phonenumber(app):
    app.kontakt.modify_first_kontakt(Address(mobile="New phonenumber"))

