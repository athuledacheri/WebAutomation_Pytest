from selenium.webdriver.common.by import By

class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
        self.btnFinish = (By.XPATH, "// button[ @ id = 'finish']")
        self.OrderMessage = (By.XPATH, "//h2[normalize-space()='Thank you for your order!']")

    def clickFinish(self):
        self.driver.find_element(*self.btnFinish).click()

    def VerifyOrder(self):
        textMatch = self.driver.find_element(*self.OrderMessage).text
        assert ("Thank you for your order!" in textMatch)



