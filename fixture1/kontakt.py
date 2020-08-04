
class KontaktHelper:

    def __init__(self, app):
        self.app = app

    def create_address(self, Address):
        wd = self.app.wd
        self.create_new_address()
        # add address
        wd.find_element_by_name("firstname").clear()
        # fill address firm
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

    def create_new_address(self):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()

    def retern_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
