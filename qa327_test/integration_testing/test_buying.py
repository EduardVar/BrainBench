import pytest
import requests
import time
from seleniumbase import BaseCase

from qa327_test.conftest import base_url


@pytest.mark.usefixtures('server')
def test_server_is_live():
	r = requests.get(base_url)
	assert r.status_code == 200

@pytest.mark.usefixtures('server')
class testBuying(BaseCase):

    def sleep(self, seconds):
        time.sleep(seconds)

    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "pytest@test.com")
        self.type("#name", "pytest")
        self.type("#password", "PYTESTpassword!")
        self.type("#password2", "PYTESTpassword!")
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.type("#password", "PYTESTpassword!")
        self.click('input[type="submit"]')

    def sell_ticket(self):
        self.click('#btn-add-ticket')
        self.sleep(1)
        self.type("#sell-ticket-name", "test buy ticket")
        self.type("#sell-ticket-quantity", "90")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", "20990101")
        self.click('#sell-ticket-button')

    def buy_ticket(self):
        self.click('#btn-buy-test-buy-ticket')
        self.type("#buy-ticket-quantity", "5")
        self.click('#buy-ticket-button')

    def test_posting(self):
        """ This test checks standard login for the Swag Labs store. """
        self.register()
        self.login()
        self.open(base_url + '/')
        self.sell_ticket()
        self.assert_element("#test-buy-ticket")

        initBalance = int(self.get_element("#user-balance").text)

        self.buy_ticket()
        self.sleep(3)
        self.assertTrue(int(self.get_element("#user-balance").text) < initBalance)
        self.open(base_url + '/logout')