from model.address import Address


def test_modify_kontakt_name(app):
    if app.kontakt.count() == 0:
        app.kontakt.create_address(Address(firstname="test"))
    old_kontakts = app.kontakt.get_kontakt_list()
    kontakt = Address(firstname="New kontakt")
    kontakt.id = old_kontakts[0].id
    app.kontakt.modify_first_kontakt(kontakt)
    new_kontakts = app.kontakt.get_kontakt_list()
    assert len(old_kontakts) == len(new_kontakts)
    old_kontakts[0] = kontakt
    assert sorted(old_kontakts, key=Address.id_or_max) == sorted(new_kontakts, key=Address.id_or_max)

#def test_modify_kontakt_lastname(app):
#    if app.kontakt.count() == 0:
#        app.kontakt.create_address(Address(firstname="test"))
#    app.kontakt.modify_first_kontakt(Address(lastname="New lastname"))

#def test_modify_kontakt_phonenumber(app):
#    if app.kontakt.count() == 0:
#        app.kontakt.create_address(Address(firstname="test"))
#    app.kontakt.modify_first_kontakt(Address(mobile="New phonenumber"))

