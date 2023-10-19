import time

from testpage import OperationsHelper
import logging, yaml

with open("testdata.yaml", 'r') as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_login_button()
    testpage.click_contact_link()
    testpage.enter_name(testdata["name"])
    testpage.enter_email(testdata["email"])
    testpage.enter_content(testdata["content"])
    testpage.click_contact_us_button()
    time.sleep(3)
    assert testpage.get_text_in_alert() == "Form successfully submitted"

# def step_1(browser):
#     logging.info("Test1 Starting")
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login("test")
#     testpage.enter_pass("test")
#     testpage.click_login_button()
#     assert testpage.get_error_text() == "401"
