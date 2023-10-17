from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id='login']/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id='login']/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id='app']/main/div/div/div[2]/h2""")
    LOCATOR_CONTACT_LINK = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_BTN[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def click_contact_link(self):
        logging.info("Click contact linck")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_LINK).click()

    def enter_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_contact_us_button(self):
        logging.info("Click contact_us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_text_in_alert(self):
        logging.info("Get text in alert")
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        logging.info(f"alert_text= {alert_text}")
        alert.accept()
        return alert_text

