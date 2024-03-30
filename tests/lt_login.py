import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from pages.LoginPage import LoginPage
from pages.GetStartedPage import GetStartedPage
from utils import utils as utils



@pytest.mark.usefixtures('driver')
class TestLogin:

    def test_login(self, driver):
        try:
            #driver = self.driver
            login = LoginPage(driver)
            login.navigate_to()
            login.enter_user_name(utils.USERNAME)
            login.enter_password(utils.PASSWORD)
            time.sleep(2)
            login.click_sign_in()
            time.sleep(4)
            get_started = GetStartedPage(driver)

            assert get_started.logged_in_user_displayed()
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            raise

        except NoSuchElementException as error:
            print("No Such Element Found")
            print(error)
            raise
