from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import utils as utils


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Locator of the elements on the page
        self.select_category_xpath = "//select[@formcontrolname='industryCode']"
        self.select_option_xpath = "//option[@value='Restaurant_Chain_or_Group']"
        self.firstname_xpath = "//input[@name='firstname']"
        self.lastname_xpath = "//input[@name='lastname']"
        self.email_xpath = "//input[@name='email']"
        self.password_xpath = "//input[@name='password']"
        self.marketing_offer_xpath = "//input[@name='marketingoffers']"
        self.terms_condition_xpath = "//input[@name='termsandconditions']"
        self.submit_btn_xpath = "//button[@type='submit']"
        self.account_created_xpath = "//span[text()='Account successfully created!']"
        self.error_occured_xpath = "//span[text()='Error creating account. Please contact support.']"

    def select_category_option(self):
        self.driver.find_element(By.XPATH, self.select_category_xpath).click()
        self.driver.find_element(By.XPATH, self.select_option_xpath).click()

    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.firstname_xpath).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.lastname_xpath).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_marketing_offer(self):
        self.driver.find_element(By.XPATH, self.marketing_offer_xpath).click()

    def click_terms_condition(self):
        self.driver.find_element(By.XPATH, self.terms_condition_xpath).click()

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_btn_xpath).click()

    def account_creation_success(self):
        match = self.driver.find_element(By.XPATH, self.account_created_xpath).is_displayed()
        return match

    def error_occured_displayed(self):
        match = self.driver.find_element(By.XPATH, self.error_occured_xpath).is_displayed()
        return match
