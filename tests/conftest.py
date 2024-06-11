import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser name: chrome, Edge, IE")

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "Edge":
        driver = webdriver.Edge()
    elif browser_name == "IE":
        print("IE driver")
        # Initialize IE WebDriver here if needed
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()

class BaseClass:
    @pytest.fixture(autouse=True)
    def setup_class(self, setup):
        self.driver = setup
