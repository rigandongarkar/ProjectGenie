import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.PersonalDetailsPage import PersonalDetails
from PageObjects.ProductsDetails import ProductDetailsPage
from test_Framework.BaseClass import BaseClass


class TestGenie(BaseClass):

    def test_QuoteGenerate(self):
        # time.sleep(5)
        # alert = driver.switch_to.alert
        # alert.accept()

        # plan selection
        log = self.getLogger()

        productDetails = ProductDetailsPage(self.driver)
        products = productDetails.getProduct()

        for product in products:
            plan = product.find_element_by_xpath("div[2]")
            log.info(plan.text)
            if plan.text == "Kotak Assured Savings Plan":
                log.info(plan.text)
                product.find_element_by_xpath("button").click()
                break
        # Personal details
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[id='insuredSalutation']")))

        self.waiting()
        personalDetails_Obj = PersonalDetails(self.driver)
        personalDetails_Obj.getSalutation().click()

        salut = self.driver.find_elements_by_css_selector("a[ng-click*='insuredSalutation']")
        for salutation in salut:
            # print(salutation.text)
            if salutation.text == 'Mr':
                salutation.click()
                break

        self.driver.find_element_by_id("insuredFirstName").send_keys("Serverus")
        self.driver.find_element_by_id("insuredLastName").send_keys("Snipe")
        self.driver.find_element_by_id("insuredDOB").send_keys("16/01/1976")

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
            # log.info(proposerState.text)
            if proposerState.text == 'Maharashtra':
                proposerState.click()
                break

        self.driver.find_element_by_id("proposerEmail").send_keys("abcd@gmail.com")
        self.driver.find_element_by_id("proposerMobileNumber").send_keys("8899009988")
        self.driver.find_element_by_xpath("//button[@translate='Next']").click()
        self.driver.find_element_by_css_selector("button[id= 'pef_yes']").click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.ID, "premium")))
        self.driver.find_element_by_id("premium").send_keys("50000")
        self.driver.find_element_by_id("floatlabelpolicyTerminyrs").click()
        policyTerm = self.driver.find_elements_by_css_selector("a[ng-click*='policyTerminyrs']")
        random.choice(policyTerm).click()

        self.driver.find_element_by_id("floatlabelpremiumPayingTerminyrs").click()
        policyPayingTerm = self.driver.find_elements_by_css_selector("a[ng-click*='premiumPayingTerminyrs']")
        random.choice(policyPayingTerm).click()

        self.driver.find_element_by_id("floatlabelfrequencyofpremiumpayment").click()
        frequency = self.driver.find_elements_by_css_selector("a[ng-click*='frequencyofpremiumpayment']")
        random.choice(frequency).click()

        self.driver.find_element_by_xpath("//button[text()='Generate Quote']").click()
        log.info("----------------------------------------")
        planName = self.driver.find_element_by_css_selector(
            "div[class='summary-body-header-text'] div:nth-child(1) span").text
        log.info("Plan Name: " + planName)

        quote = self.driver.find_element_by_css_selector(
            "div[class='summary-body-header-text'] div:nth-child(2) span").text
        log.info("Quote ID: " + quote)
        log.info("----------------------------------------")

        self.driver.find_element_by_xpath("//button[text()='View PDF']").click()
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        # self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.F4)
        self.driver.find_element_by_xpath("//button[text()='Next']").click()

    def test_DEDUPE(self):
        # EApp Journey
        time.sleep(20)
        self.driver.find_element_by_xpath("//div[text()='New Customer']").click()
        self.driver.find_element_by_id("hasPanNo").click()
        self.driver.find_element_by_id("pef_ok").click()
        self.driver.find_element_by_id("dedup-addl-pin").send_keys("401107")
        self.driver.find_element_by_css_selector("button[ng-click='additionalInfoNextHandler()']").click()

    def test_EYC(self):
        time.sleep(20)
        self.driver.find_element_by_xpath("//input[@ng-model='isOptForEkyc' and @value='No']").click()
        self.driver.find_element_by_css_selector("button[ng-click='ekycNextHandler()']").click()

    def test_PSM(self):
        time.sleep(10)
        self.driver.find_element_by_css_selector("button[id='insuredOccupation']").click()
        InsuredOccupation = self.driver.find_elements_by_css_selector("ul[float-label-id='floatlabelinsuredOccupation'] li a")
        random.choice(InsuredOccupation).click()
        Objective = self.driver.find_element_by_id("objective")
        Objective.click()