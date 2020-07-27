# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_new_address(wd)
        self.create_address(wd, "Viktor", "Prihodko", "08998899854")
        self.retern_home_page(wd)
        self.logout(wd)

    def create_address(self, wd, name, lastname, phonenumber):
        # add address
        wd.find_element_by_name("firstname").clear()
        # fill address firm
        wd.find_element_by_name("firstname").send_keys(name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(lastname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(phonenumber)
        # submit address creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def create_new_address(self, wd):
        wd.find_element_by_name("firstname").click()

    def retern_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("content").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
