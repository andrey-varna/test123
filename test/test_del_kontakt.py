from model.address import Address
from  random import randrange


def test_del_some_kontakt(app):
    if app.kontakt.count() == 0:
        app.kontakt.create_address(Address(firstname="test"))
    old_kontakts = app.kontakt.get_kontakt_list()
    index = randrange(len(old_kontakts))
    app.kontakt.del_kontakt_by_index(index)
    new_kontakts = app.kontakt.get_kontakt_list()
    assert len(old_kontakts) - 1 == len(new_kontakts)
    old_kontakts [index:index+1] = []
    assert old_kontakts == new_kontakts
