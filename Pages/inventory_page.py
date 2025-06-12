from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class InventoryPage(BasePage):
    def is_loaded(self):
        return "inventory" in self.driver.current_url

    def sort_by(self, value):
        dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        dropdown.click()
        dropdown.find_element(By.XPATH, f"//option[@value='{value}']").click()

    def get_product_names(self):
        return [el.text for el in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]

    def add_product_to_cart(self, product_id):
        self.click(By.ID, f"add-to-cart-{product_id}")
