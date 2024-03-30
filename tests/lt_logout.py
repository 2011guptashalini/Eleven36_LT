import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from pages.LoginPage import LoginPage
from pages.GetStartedPage import GetStartedPage
from pages.LaunchPage import LaunchPage
from utils import utils as utils



@pytest.mark.usefixtures('driver')
class TestLogout:

    @pytest.mark.order(1)
    def test_logout(self, driver):
        try:
            # driver = self.driver
            login = LoginPage(driver)
            login.navigate_to()
            login.enter_user_name(utils.USERNAME)
            login.enter_password(utils.PASSWORD)
            time.sleep(2)
            login.click_sign_in()
            get_started = GetStartedPage(driver)
            time.sleep(4)
            get_started.click_logged_in_user()
            time.sleep(4)
            get_started.click_logout()
            launch = LaunchPage(driver)
            time.sleep(4)
            assert launch.logout_success_message_displayed()
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            raise

        except NoSuchElementException as error:
            print("No Such Element Found")
            print(error)
            raise

