
import pytest
from selene import browser

DOMAIN_URL = 'https://demowebshop.tricentis.com/'
LOGIN = "example1200@example.com"
PASSWORD = "123456"

@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = DOMAIN_URL
    browser.config.window_width = '1900'
    browser.config.window_height = '1080'
    yield browser
    browser.quit()