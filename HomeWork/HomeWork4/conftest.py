import pytest
import pytest, yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdrivermanager import ChromeDriverManager
from webdrivermanager import GeckoDriverManager


with open("testdata.yaml", 'r') as f:
    testdata = yaml.safe_load(f)

browser = testdata["browser"]


@pytest.fixture(scope="session")
def browser():
    # if browser == "chrome":
    service = Service('chromedriver')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    # else:
    #     service = Service(executable_path=GeckoDriverManager().download_and_install())
    #     options = webdriver.FirefoxOptions()
    #     driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()
