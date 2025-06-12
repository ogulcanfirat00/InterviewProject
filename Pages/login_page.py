from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.type(By.ID, "user-name", username)
        self.type(By.ID, "password", password)
        self.click(By.ID, "login-button")
