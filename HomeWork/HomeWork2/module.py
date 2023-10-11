import yaml
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

service = Service(testdata['driver_path'])
options = webdriver.ChromeOptions()
# options = webdriver.FirefoxOptions()


class Site:
    def __init__(self, address):
        self.driver = webdriver.Chrome(service=service, options=options)
        # self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata['sleep_time'])
