from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.title = (By.XPATH, "//span[@class='title']")
        self.addToCart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def VerifyTitle(self):
        textMatch = self.driver.find_element(*self.title).text
        assert ("Products" in textMatch)

    def AddToCart(self):
        self.driver.find_element(*self.addToCart).click()
