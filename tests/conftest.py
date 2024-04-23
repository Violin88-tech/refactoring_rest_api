
import pytest
import requests
from selene import browser

from resource.utils import cookie

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

@pytest.fixture(scope="session", autouse=True)
def get_auth_cookie():
    response = requests.post(DOMAIN_URL + '/login', json={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')
    print(cookie)

@pytest.fixture(scope="function", autouse=True)
def add_auth_cookie_to_browser(open_browser):
    browser.open('/')
    print(cookie)
    browser.driver.add_cookie({'name': "NOPCOMMERCE.AUTH", 'value': cookie})
