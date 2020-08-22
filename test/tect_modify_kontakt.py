from model.address import Address


def test_modify_kontakt_name(app):
    if app.kontakt.count() == 0:
        app.kontakt.create_address(Address(firstname="test"))
    app.kontakt.modify_first_kontakt(Address(firstname="New kontakt"))


def test_modify_kontakt_lastname(app):
    if app.kontakt.count() == 0:
        app.kontakt.create_address(Address(firstname="test"))
    app.kontakt.modify_first_kontakt(Address(lastname="New lastname"))


def test_modify_kontakt_phonenumber(app):
    if app.kontakt.count() == 0:
        app.kontakt.create_address(Address(firstname="test"))
    app.kontakt.modify_first_kontakt(Address(mobile="New phonenumber"))

