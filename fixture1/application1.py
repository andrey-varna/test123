from selenium import webdriver
from fixture1.newsession import SessionHelper
from fixture1.kontakt import KontaktHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.newsession = SessionHelper(self)
        self.kontakt = KontaktHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")

    def destroy(self):
        self.wd.quit()
