import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--userType", action="store", default="lo302")


@pytest.fixture(scope="class")
def setup(request):
    userType = request.config.getoption("userType")
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="E:\\python selenium\\chromedriver_win32\\chromedriver",
                              options=chromeOptions)

    driver.get("https://genieuat.mykotaklife.com/genie-web/index.html#/login")
    driver.implicitly_wait(120)

    # login
    if userType == "apc":
        driver.find_element_by_xpath("//input[@ng-model='username']").send_keys("lo302")
        driver.find_element_by_css_selector("input[id='pwd']").send_keys("Genie@1234")
        driver.find_element_by_id("floatlabelUserType").click()
        employeeID = driver.find_elements_by_css_selector("span[class*= 'dropdown'] ul li a")
        for employeeType in employeeID:
            # print(employeeType.text)
            if employeeType.text == "KLI Employee":
                employeeType.click()
        driver.find_element_by_xpath("//div[@class='form-group']/button[1]").click()

    elif userType == "tied":
        driver.find_element_by_xpath("//input[@ng-model='username']").send_keys("lo777")
        driver.find_element_by_css_selector("input[id='pwd']").send_keys("Genie@1234")
        driver.find_element_by_id("floatlabelUserType").click()
        employeeID = driver.find_elements_by_css_selector("span[class*= 'dropdown'] ul li a")
        for employeeType in employeeID:
            # print(employeeType.text)
            if employeeType.text == "KLI Employee":
                employeeType.click()
        driver.find_element_by_xpath("//div[@class='form-group']/button[1]").click()

    elif userType == "advisor":
        driver.find_element_by_xpath("//input[@ng-model='username']").send_keys("60106311")
        driver.find_element_by_css_selector("input[id='pwd']").send_keys("Genie@1234")
        driver.find_element_by_id("floatlabelUserType").click()
        employeeID = driver.find_elements_by_css_selector("span[class*= 'dropdown'] ul li a")
        for employeeType in employeeID:
            # print(employeeType.text)
            if employeeType.text == "Advisor":
                employeeType.click()
        driver.find_element_by_xpath("//div[@class='form-group']/button[1]").click()

    request.cls.driver = driver
    yield
    driver.close()
