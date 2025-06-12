import pytest
from config import driver
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage

@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", True),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True)
])

def test_login(driver, username, password, expected):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory = InventoryPage(driver)
    assert inventory.is_loaded() == expected
