import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

def test_valid_login(setup):
    login = LoginPage(setup)
    login.load()
    login.login("standard_user", "secret_sauce")
    products = ProductsPage(setup)
    assert products.get_title() == "Products"

def test_invalid_login(setup):
    login = LoginPage(setup)
    login.load()
    login.login("wrong_user", "wrong_pass")
    assert "Username and password" in login.get_error_message()
