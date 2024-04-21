import logging
import time

from allure_commons._allure import step

from resource.utils import post_reqres
from tests.conftest import LOGIN,PASSWORD,DOMAIN_URL
import requests
import allure
from selene import browser, have

def test_login():
    with step("Authorization with API"):
        response = post_reqres("/login", json={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    logging.info(cookie)
    assert response.status_code == 302
    with step("Open main page with authorized user"):
        browser.open(DOMAIN_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.element('.ico-login').click()
        browser.element(".page-title").should(have.text('Welcome, Please Sign In!'))


def test_add_product():
    response = post_reqres("/login", json={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    logging.info(cookie)
    browser.open(DOMAIN_URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    with step("Add product in card API"):
        post_reqres("/addproducttocart/details/74/1",
                    data={
                        "addtocart_74.EnteredQuantity": 1})
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    logging.info(cookie)
    assert response.status_code == 302
    with step("Add product in card UI"):
        browser.open(f"{DOMAIN_URL}/desktops")
        browser.element('.product-box-add-to-cart-button').click()
        browser.element(".product-name").should(have.text('Build your own cheap computer'))


def test_add_product_with_verification():
    response = post_reqres("/login", json={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    logging.info(cookie)
    browser.open(DOMAIN_URL)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    with step("Add product in card API"):
        post_reqres("/addproducttocart/details/31/1",
                    data={"addtocart_31.EnteredQuantity": 1})
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    logging.info(cookie)
    assert response.status_code == 302
    with step("Check product in card"):
        browser.open(f"{DOMAIN_URL}/cart")
        time.sleep(3)
        browser.element('.product-name').should(have.text("Computing and Internet"))
