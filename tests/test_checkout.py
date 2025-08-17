import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import pytest

@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

def test_checkout_flow(setup):
    login = LoginPage(setup)
    login.load()
    login.login("standard_user", "secret_sauce")
    products = ProductsPage(setup)
    products.add_first_product_to_cart()
    products.go_to_cart()
    # Add assertions here to validate cart (extend later)
    assert "cart" in setup.current_url

