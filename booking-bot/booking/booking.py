import os
from selenium import webdriver
import booking.constants as const

class Booking:
    def __init__(self, driver_path=r'/Users/varun/Documents/se_test/chrome-mac-arm64', teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        self.driver = webdriver.Chrome()
        super(Booking, self).__init__()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        print("Chrome browser opened")

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()
            print("Chrome browser closed")

    def land_first_page(self):
        self.driver.get(const.BASE_URL)
        print("Landed on first page of booking.com")

    def change_currency(self, currency=None):
        