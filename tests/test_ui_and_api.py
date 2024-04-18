from tests.conftest import LOGIN,PASSWORD,DOMAIN_URL
import requests
import allure
from selene import browser, have

def test_login():
    with allure.step("Get user cookie"):
        response = requests.post(DOMAIN_URL + "/login",
                                 data={"Email": LOGIN, "Password": PASSWORD},
                                 allow_redirects=False)
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        browser.open('')
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})

    with allure.step('Open login page'):
        browser.open('')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
        browser.open('')
        browser.element('.account').should(have.text(LOGIN))


def test_add_product():
    with allure.step("Get user cookie"):
        response = requests.post(DOMAIN_URL + "/login",
                                 data={"Email": LOGIN, "Password": PASSWORD},
                                 allow_redirects=False)
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        browser.open('')
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})

    with allure.step("Add product to user's cart"):
        response = requests.post(DOMAIN_URL + 'addproducttocart/catalog/31/1/1',
                                     cookies={"NOPCOMMERCE.AUTH": cookie})

    with allure.step("Check items in cart"):
        browser.open('cart')
        browser.element('.product-unit-price').should(have.text('1590.00'))

    with allure.step("Delete items"):
        browser.open('cart')
        browser.element('[name="removefromcart"]').click()
        browser.element('[name="updatecart"]').click()
        browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))













