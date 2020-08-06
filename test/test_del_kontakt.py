

def test_del_kontakt(app):
    app.session.login(username="admin", password="secret")
    app.kontakt.del_kontakt()
    app.session.logout()