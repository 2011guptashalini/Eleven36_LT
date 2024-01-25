from selenium import webdriver
from selenium.webdriver.common.by import By


class GetStartedPage():
    def __init__(self, driver):
        self.driver = driver

        self.loggedInUser_xpath = "//span[@class='cx-login-greet d-none d-md-flex']"
        self.user_icon_xpath = "//img[@class='userIcon']"
        self.logout_xpath = "//a[text()='Logout']"

    def logged_in_user_displayed(self):
        match = self.driver.find_element(By.XPATH, self.loggedInUser_xpath).is_displayed()
        return match

    def click_user_icon(self):
        self.driver.find_element(By.XPATH, self.user_icon_xpath).click()

    def click_logged_in_user(self):
        self.driver.find_element(By.XPATH, self.loggedInUser_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()


