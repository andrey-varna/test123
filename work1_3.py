# -*- coding: utf-8 -*-
import unittest
from address import Address
from application1 import Application


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_untitled_test_case(self):
        self.app.login(username="admin", password="secret")
        self.app.create_address(Address("Viktor", "Prihodko", "08998899854"))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
