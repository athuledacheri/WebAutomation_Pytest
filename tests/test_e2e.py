import pytest

from PageObjects.CartPage import CartPage
from Utilities.BaseClass import BaseClass
from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.LoginPage import LoginPage
from Utilities.ExcelUtils import get_data_from_excel


@pytest.mark.parametrize("username, password, fName, lName, pin", get_data_from_excel("testData.xlsx", "LoginData"))
class TestSample(BaseClass):
    def test_e2e(self, username, password, fName, lName, pin):
        # LoginPage
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()
        # cartpage
        cartpage = CartPage(self.driver)
        cartpage.VerifyTitle()
        cartpage.AddToCart()
        cartpage.ClickCart()
        cartpage.ClickCheckOUt()
        cartpage.enter_Fname(fName)
        cartpage.enter_Lname(lName)
        cartpage.enter_Post(pin)
        cartpage.ClickContinue()
        #checkoutpage
        checkout = CheckOutPage(self.driver)
        checkout.clickFinish()
        checkout.VerifyOrder()







