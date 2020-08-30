from model.address import Address


def test_del_kontakt(app):
    if app.kontakt.count() == 0:
        app.kontakt.create_address(Address(firstname="test"))
    old_kontakts = app.kontakt.get_kontakt_list()
    app.kontakt.del_kontakt()
    new_kontakts = app.kontakt.get_kontakt_list()
    assert len(old_kontakts) - 1 == len(new_kontakts)
    old_kontakts [0:1] = []
    assert old_kontakts == new_kontakts
