from selenium.webdriver.common.by import By


class PersonalDetails:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_css_selector("button[id='insuredSalutation']")
    salutation = (By.CSS_SELECTOR, "button[id='insuredSalutation']")

    def getSalutation(self):
        return self.driver.find_element(*PersonalDetails.salutation)