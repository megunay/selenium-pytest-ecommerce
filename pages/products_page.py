from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.CLASS_NAME, "title")
        self.add_to_cart = (By.CSS_SELECTOR, "button.btn_inventory")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def get_title(self):
        return self.driver.find_element(*self.title).text

    def add_first_product_to_cart(self):
        self.driver.find_elements(*self.add_to_cart)[0].click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
