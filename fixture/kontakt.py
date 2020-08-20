from model.address import Address


class KontaktHelper:

    def __init__(self, app):
        self.app = app

    def create_address(self, address):
        wd = self.app.wd
        self.create_new_address()
        self.fill_kontakt_form(address)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.retern_home_page()

    def fill_kontakt_form(self, address):
        self.change_field_value_kontakt("firstname", address.firstname)
        self.change_field_value_kontakt("lastname", address.lastname)
        self.change_field_value_kontakt("mobile", address.mobile)

    def change_field_value_kontakt(self, field_name, tekst):
        wd = self.app.wd
        if tekst is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(tekst)

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

    def modify_first_kontakt(self, new_kontakt_date):
        wd = self.app.wd
        self.select_first_kontakt()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill form kontakt
        self.fill_kontakt_form(new_kontakt_date)
        # submit modify
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
