from model.group import Rename


def test_edit_kontakt(app):
    app.kontakt.rename_kontakt(Rename("Pavel"))
