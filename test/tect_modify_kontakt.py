from model.address import Address


def test_modify_kontakt_name(app):
    app.session.login(username="admin", password="secret")
    app.kontakt.modify_first_kontakt(Address(firstname="New kontakt"))
    app.session.logout()


def test_modify_group_lastname(app):
    app.session.login(username="admin", password="secret")
    app.kontakt.modify_first_kontakt(Address(lastname="New lastname"))
    app.session.logout()


def test_modify_group_phonenumber(app):
    app.session.login(username="admin", password="secret")
    app.kontakt.modify_first_kontakt(Address(mobile="New phonenumber"))
    app.session.logout()
