import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.ProductsDetails import ProductDetailsPage
from test_Framework.BaseClass import BaseClass


class TestGenie(BaseClass):

    def test_GeniePage(self):
        # time.sleep(5)
        # alert = driver.switch_to.alert
        # alert.accept()

        # plan selection
        log = self.getLogger()

        productDetails = ProductDetailsPage(self.driver)
        products = productDetails.getProduct()

        for product in products:
            plan = product.find_element_by_xpath("div[2]")
            if plan.text == "Kotak Assured Savings Plan":
                log.info(plan.text)
                product.find_element_by_xpath("button").click()
                break
        # Personal details
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[id='insuredSalutation']")))
        self.driver.find_element_by_css_selector("button[id='insuredSalutation']").click()

        salut = self.driver.find_elements_by_css_selector("a[ng-click*='insuredSalutation']")
        for salutation in salut:
            # print(salutation.text)
            if salutation.text == 'Mr':
                salutation.click()
                break

        self.driver.find_element_by_id("insuredFirstName").send_keys("Rigan")
        self.driver.find_element_by_id("insuredLastName").send_keys("Dongarkar")
        self.driver.find_element_by_id("insuredDOB").send_keys("16/01/1997")

        self.driver.find_element_by_id("agentLocation").send_keys("Ma")
        aState = self.driver.find_elements_by_css_selector("a[bind-html-unsafe*='match.label']")

        for agentState in aState:
            # print(agentState.text)
            if agentState.text == 'Maharashtra':
                agentState.click()
                break

        self.driver.find_element_by_id("proposerLocation").send_keys("Ma")
        pState = self.driver.find_elements_by_css_selector("a[bind-html-unsafe*='match.label']")

        for proposerState in pState:
            log.info(proposerState.text)
            if proposerState.text == 'Maharashtra':
                proposerState.click()
                break

        self.driver.find_element_by_id("proposerEmail").send_keys("abcd@gmail.com")
        self.driver.find_element_by_id("proposerMobileNumber").send_keys("8899009988")
        self.driver.find_element_by_xpath("//button[@translate='Next']").click()
        self.driver.find_element_by_css_selector("button[id= 'pef_yes']").click()