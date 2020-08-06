
class KontaktHelper:

    def __init__(self, app):
        self.app = app

    def create_address(self, Address):
        wd = self.app.wd
        self.create_new_address()
        # fill address firm
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Address.name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Address.lastname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Address.phonenumber)
        # submit address creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.retern_home_page()

    def del_kontakt(self):
        wd = self.app.wd
        # select first kontakt
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def rename_kontakt(self, Rename):
        wd = self.app.wd
        # select first kontakt
        wd.find_element_by_name("selected[]").click()
        # edit kontakt
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Pavel")
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.retern_home_page()

    def create_new_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def retern_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
