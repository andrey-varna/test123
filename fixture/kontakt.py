
class KontaktHelper:

    def __init__(self, app):
        self.app = app

    def create_address(self, address):
        wd = self.app.wd
        self.create_new_address()
        # fill address firm
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(address.name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(address.lastname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(address.phonenumber)
        # submit address creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.retern_home_page()

    def del_kontakt(self):
        wd = self.app.wd
        self.select_first_kontakt()
        # submit deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def rename_kontakt(self, rename):
        wd = self.app.wd
        self.select_first_kontakt()
         # edit kontakt
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Sasha")
        wd.find_element_by_name("update").click()
        self.retern_home_page()

    def create_new_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def retern_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def select_first_kontakt(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
