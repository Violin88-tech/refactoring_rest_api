from selene import browser
import requests
from tests.conftest import LOGIN,PASSWORD,DOMAIN_URL


def get_auth_cookie():
    response = requests.post(DOMAIN_URL + '/login', json={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')
    return cookie

def add_auth_cookie_to_browser():
    browser.open('/')
    browser.driver.add_cookie({'name': "NOPCOMMERCE.AUTH", 'value': get_auth_cookie()})
