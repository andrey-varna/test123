# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="123", header="aSFASEDFHG", footer="AFWR"))


def test_add_ampty_group(app):
    app.group.create(Group(name="", header="", footer=""))

