import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from pages.LoginPage import LoginPage
from pages.ForgotPasswordPage import ForgotPasswordPage
from utils import utils as utils


@pytest.mark.usefixtures("driver")
class TestForgotPassword:

    @pytest.mark.order(1)
    def test_forgot_password(self, driver):
        try:
            # driver = self.driver
            login = LoginPage(driver)
            login.navigate_to()
            login.click_forgot_password_link()
            time.sleep(3)
            forgot_password = ForgotPasswordPage(driver)
            forgot_password.enter_user_name(utils.USERNAME)
            forgot_password.click_submit_btn()
            time.sleep(4)
            assert forgot_password.reset_email_success_message_displayed()
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            raise

        except NoSuchElementException as error:
            print("No Such Element Found")
            print(error)
            raise
