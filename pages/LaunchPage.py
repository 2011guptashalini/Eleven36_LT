from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import utils as utils


class LaunchPage:
    def __init__(self, driver):
        self.driver = driver

        # Locator of the elements on the page
        self.logout_success_xpath = "//span[text()='You have successfully signed out.']"

    def logout_success_message_displayed(self):
        match = self.driver.find_element(By.XPATH, self.logout_success_xpath).is_displayed()
        return match
