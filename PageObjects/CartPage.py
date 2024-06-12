from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.XPATH, "//span[@class='title']")
        self.addToCart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        self.Cart = (By.XPATH, "//span[@class='shopping_cart_badge']")
        self.CheckOut = (By.XPATH, "//button[@id='checkout']")
        self.firstName = (By.XPATH, "//input[@id='first-name']")
        self.lastName = (By.XPATH, "//input[@id='last-name']")
        self.post = (By.XPATH, "//input[@id='postal-code']")
        self.btnContinue = (By.XPATH, "//input[@id='continue']")

    def VerifyTitle(self):
        textMatch = self.driver.find_element(*self.title).text
        assert ("Products" in textMatch)

    def AddToCart(self):
        self.driver.find_element(*self.addToCart).click()

    def ClickCart(self):
        self.driver.find_element(*self.Cart).click()

    def ClickCheckOUt(self):
        self.driver.find_element(*self.CheckOut).click()

    def enter_Fname(self, fName):
        self.driver.find_element(*self.firstName).send_keys(fName)

    def enter_Lname(self, lName):
        self.driver.find_element(*self.lastName).send_keys(lName)

    def enter_Post(self, pin):
        self.driver.find_element(*self.post).send_keys(pin)

    def ClickContinue(self):
        self.driver.find_element(*self.btnContinue).click()









