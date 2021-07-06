import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--userType", action="store", default="lo302")
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser")
    userType = request.config.getoption("userType")
    if browser == "chrome":
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--start-maximized")
        chromeOptions.add_argument("--disable-gpu")
        driver = webdriver.Chrome(executable_path="E:\\python selenium\\chromedriver_win32\\chromedriver",
                                  options=chromeOptions)

        driver.get("https://genieuat.mykotaklife.com/genie-web/index.html#/login")
        # driver.maximize_window()
        driver.implicitly_wait(120)
        driver.find_element_by_css_selector("button[id='dropdownMenu2']").click()
        if userType == "apc" or "tied":
            driver.find_element_by_css_selector("a[domain='Employee']").click()
            if userType == "tied":
                driver.find_element_by_css_selector("input[ng-model='username']").send_keys("lo302")
                driver.find_element_by_css_selector("input[ng-model='password']").send_keys("Genie@1234")
                driver.find_element_by_css_selector("button[ng-click='login()']").click()

    if browser == "firefox":
        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.add_argument("--start-maximized")
        firefoxOptions.add_argument("--disable-gpu")
        driver = webdriver.Chrome(executable_path="E:\\python selenium\\geckodriver-v0.29.1-win64\\geckodriver",
                                  options=firefoxOptions)

        driver.get("https://genieuat.mykotaklife.com/genie-web/index.html#/login")
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("button[id='dropdownMenu2']").click()
        if userType == "apc" or "tied":
            driver.find_element_by_css_selector("a[domain='Employee']").click()
            if userType == "tied":
                driver.find_element_by_css_selector("input[ng-model='username']").send_keys("lo302")
                driver.find_element_by_css_selector("input[ng-model='password']").send_keys("Genie@1234")
                driver.find_element_by_css_selector("button[ng-click='login()']").click()

    request.cls.driver = driver
    yield
    driver.close()
