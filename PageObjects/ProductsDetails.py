from selenium.webdriver.common.by import By


class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_elements_by_xpath("//*[contains(@ng-repeat,'productList')]/div")

    product = (By.XPATH, "//*[contains(@ng-repeat,'productList')]/div")

    def getProduct(self):
        return self.driver.find_elements(*ProductDetailsPage.product)
