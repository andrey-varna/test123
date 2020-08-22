from model.address import Address


def test_del_kontakt(app):
    if app.kontakt.count() == 0:
        app.kontakt.create_address(Address(firstname="test"))
    app.kontakt.del_kontakt()
