import time
import pytest
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
from pages.LoginPage import LoginPage
from pages.GetStartedPage import GetStartedPage
from pages.RegisterPage import RegisterPage
from utils import utils as utils
import allure
import moment



@pytest.mark.usefixtures('driver')
class TestSignup:

    @pytest.mark.order(1)
    def test_in_valid_signup(self, driver):
        # This test case is to test that user is able to signup if they provide all valid information

        try:
            fake = Faker()
            #driver = self.driver
            login = LoginPage(driver)
            login.navigate_to()
            time.sleep(2)
            login.click_sign_up()
            register = RegisterPage(driver)
            register.select_category_option()
            register.enter_firstname(fake.unique.first_name())
            register.enter_lastname(fake.unique.last_name())
            register.enter_email(utils.USERNAME)
            register.enter_password(utils.PASSWORD)

            time.sleep(2)
            register.click_marketing_offer()
            register.click_terms_condition()
            register.click_submit()

            time.sleep(4)
            assert register.error_occured_displayed()
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            raise

        except NoSuchElementException as error:
            print("No Such Element Found")
            print(error)
            raise

    @pytest.mark.order(1)
    def test_valid_signup(self):
        # This test cases is to test that it does not allow user to signup with the existing email
        try:
            fake = Faker()
            driver = self.driver
            login = LoginPage(driver)
            login.navigate_to()
            time.sleep(2)
            login.click_sign_up()
            register = RegisterPage(driver)
            register.select_category_option()  # Categories are displayed and select randomly. We can put an assert. Divide this in differnet
            register.enter_firstname(fake.unique.first_name())  # test with time stamp. e36_test_timestamp
            register.enter_lastname(fake.unique.last_name())  # test
            register.enter_email(fake.unique.email())  # with test domain
            register.enter_password(utils.PASSWORD)

            time.sleep(2)
            register.click_marketing_offer()
            register.click_terms_condition()
            register.click_submit()

            time.sleep(4)

            assert register.account_creation_success()
            get_started = GetStartedPage(driver)
            
            time.sleep(4)
            assert get_started.logged_in_user_displayed()
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            raise

        except NoSuchElementException as error:
            print("No Such Element Found")
            print(error)
            raise
