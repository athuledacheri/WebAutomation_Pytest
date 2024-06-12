import pytest
from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage
from Utilities.ExcelUtils import get_data_from_excel


@pytest.mark.parametrize("username, password", get_data_from_excel("testData.xlsx", "LoginData"))
class TestSample(BaseClass):
    def test_e2e(self, username, password):
        # Create an instance of the LoginPage
        login_page = LoginPage(self.driver)

        # Enter username and password
        login_page.enter_username(username)
        login_page.enter_password(password)

        # Click the login button
        login_page.click_login_button()

        # You can add assertions here to verify the login was successful
