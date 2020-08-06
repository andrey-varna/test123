from model.group import Rename


def test_edit_kontakt(app):
    app.session.login(username="admin", password="secret")
    app.kontakt.rename_kontakt(Rename("Pavel"))
    app.session.logout()
