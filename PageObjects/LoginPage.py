from selenium.webdriver.common.by import By

from PageObjects.CartPage import CartPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        # self.title = (By.XPATH, "//span[@class='title']")
        # self.addToCart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        # self.Cart = (By.XPATH, "//span[@class='shopping_cart_badge']")
        # self.CheckOut = (By.XPATH, "//button[@id='checkout']")
        # self.firstName = (By.XPATH, "//input[@id='first-name']")
        # self.lastName = (By.XPATH, "//input[@id='last-name']")
        # self.post = (By.XPATH, "//input[@id='postal-code']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()



    # def VerifyTitle(self):
    #     textMatch = self.driver.find_element(*self.title).text
    #     assert ("Products" in textMatch)
    #
    # def AddToCart(self):
    #     self.driver.find_element(*self.addToCart).click()
    #
    # def ClickCart(self):
    #     self.driver.find_element(*self.Cart).click()
    #
    # def ClickCheckOUt(self):
    #     self.driver.find_element(*self.CheckOut).click()

    # def enter_Fname(self, fName):
    #     self.driver.find_element(*self.firstName).send_keys(fName)
    #
    # def enter_Lname(self, lName):
    #     self.driver.find_element(*self.lastName).send_keys(lName)
    #
    # def enter_Post(self, pin):
    #     self.driver.find_element(*self.post).send_keys(pin)

