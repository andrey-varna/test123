from model.address import Address
from  random import randrange


def test_modify_kontakt_name(app):
    if app.kontakt.count() == 0:
        app.kontakt.create_address(Address(firstname="test"))
    old_kontakts = app.kontakt.get_kontakt_list()
    index = randrange(len(old_kontakts))
    kontakt = Address(firstname="New kontakt")
    kontakt.id = old_kontakts[index].id
    app.kontakt.modify_kontakt_by_index(index, kontakt)
    new_kontakts = app.kontakt.get_kontakt_list()
    assert len(old_kontakts) == len(new_kontakts)
    old_kontakts[index] = kontakt
    assert sorted(old_kontakts, key=Address.id_or_max) == sorted(new_kontakts, key=Address.id_or_max)

#def test_modify_kontakt_lastname(app):
#    if app.kontakt.count() == 0:
#        app.kontakt.create_address(Address(firstname="test"))
#    app.kontakt.modify_first_kontakt(Address(lastname="New lastname"))

#def test_modify_kontakt_phonenumber(app):
#    if app.kontakt.count() == 0:
#        app.kontakt.create_address(Address(firstname="test"))
#    app.kontakt.modify_first_kontakt(Address(mobile="New phonenumber"))

