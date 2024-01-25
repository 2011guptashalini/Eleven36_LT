from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import utils as utils


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Locator of the elements on the page
        self.username_xpath = "//input[@type='email']"
        self.password_xpath = "//input[@type='password']"
        self.signIn_btn_xpath = "//button[@type='submit']"
        self.signup_btn_xpath = "//button[text()=' Sign Up ']"
        self.forgot_password_link = "//a[text()='Forgot password?']"

    def enter_user_name(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.signIn_btn_xpath).click()

    def click_sign_up(self):
        self.driver.find_element(By.XPATH, self.signup_btn_xpath).click()

    def click_forgot_password_link(self):
        self.driver.find_element(By.XPATH, self.forgot_password_link).click()

    def navigate_to(self):
        self.driver.get(utils.URL)
