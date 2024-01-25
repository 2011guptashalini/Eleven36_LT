from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import utils as utils


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver

        # Locator of the elements on the page
        self.username_xpath = "//input[@type='email']"
        self.submit_btn_xpath = "//button[@type='submit']"
        self.forgot_email_sent = "//span[text()='An email has been sent to you with information on how to reset your password.']"

    def enter_user_name(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def click_submit_btn(self):
        self.driver.find_element(By.XPATH, self.submit_btn_xpath).click()

    def reset_email_success_message_displayed(self):
        match = self.driver.find_element(By.XPATH, self.forgot_email_sent).is_displayed()
        return match
