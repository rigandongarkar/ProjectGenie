import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="E:\\python selenium\\chromedriver_win32\\chromedriver", options= chromeOptions)

    driver.get("https://genieuat.mykotaklife.com/genie-web/index.html#/login")
    driver.implicitly_wait(120)

    # login
    driver.find_element_by_xpath("//input[@ng-model='username']").send_keys("lo302")
    driver.find_element_by_css_selector("input[id='pwd']").send_keys("Genie@1234")
    driver.find_element_by_id("floatlabelUserType").click()

    employeeID = driver.find_elements_by_css_selector("span[class*= 'dropdown'] ul li a")
    for employeeType in employeeID:
        # print(employeeType.text)
        if employeeType.text == "KLI Employee":
            employeeType.click()
    driver.find_element_by_xpath("//div[@class='form-group']/button[1]").click()
    request.cls.driver = driver
    yield
    driver.close()
