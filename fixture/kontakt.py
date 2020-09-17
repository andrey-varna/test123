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
        self.kontakt_cash = None

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
        self.del_kontakt_by_index(0)

    def del_kontakt_by_index(self, index):
        wd = self.app.wd
        self.select_kontakt_by_index(index)
        # submit deletion
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.kontakt_cash = None

    def rename_kontakt(self, rename):
        wd = self.app.wd
        self.select_first_kontakt()
        # edit kontakt
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Sasha")
        wd.find_element_by_name("update").click()
        self.retern_home_page()
        self.kontakt_cash = None

    def modify_first_kontakt(self):
        self.modify_kontakt_by_index(0)

    def modify_kontakt_by_index(self, index, new_kontakt_date):
        wd = self.app.wd
        self.select_kontakt_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill form kontakt
        self.fill_kontakt_form(new_kontakt_date)
        # submit modify
        wd.find_element_by_name("update").click()
        self.retern_home_page()
        self.kontakt_cash = None

    def create_new_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def retern_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def select_first_kontakt(self):
        self.select_kontakt_by_index(0)

    def select_kontakt_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    kontakt_cash = None

    def get_kontakt_list(self):
        if self.kontakt_cash is None:
            wd = self.app.wd
            self.home_page()
            self.kontakt_cash = []
            for tr in wd.find_elements_by_css_selector("table tr"):
                row = tr.find_elements_by_css_selector("td")
                if not len(row):
                    continue
                self.kontakt_cash.append(Address(
                    lastname=row[1].text, firstname=row[2].text, id=row[0].find_element_by_css_selector(
                        "input").get_attribute('value')))
        return list(self.kontakt_cash)
