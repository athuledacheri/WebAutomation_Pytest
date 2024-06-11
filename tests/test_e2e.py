import pytest
from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage


class TestSample(BaseClass):
    def test_e2e(self):
        # Create an instance of the LoginPage
        login_page = LoginPage(self.driver)

        # Enter username and password
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")

        # Click the login button
        login_page.click_login_button()

        # You can add assertions here to verify the login was successful
