import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import booking.constants as const
import time

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
        wait = WebDriverWait(self.driver, 15)
        currency_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]'))
        )
        currency_element.click()
        selected_currency_element = self.driver.find_element(
            By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        try:
            # Wait for the search field to be clickable
            wait = WebDriverWait(self.driver, 15)
            search_field = wait.until(EC.element_to_be_clickable((By.ID, ':rh:')))
            print("Found and clickable search field")

            # Clear the search field
            search_field.clear()
            print("Cleared search field")

            #Adding a small delay
            time.sleep(2)

            # Enter the place name
            for char in place_to_go:
                search_field.send_keys(char)
                time.sleep(0.2)
            print(f"Entered place to go: {place_to_go}")

            time.sleep(2)

            # Wait for the autocomplete results to appear
            first_result = wait.until(EC.presence_of_element_located((By.ID, 'autocomplete-result-0')))
            print("Found first result")

            # Click the first result
            first_result.click()
            print("Clicked first result")
        except Exception as e:
            print(f"An error occurred: {e}")

    def select_dates(self, check_in_date, check_out_date):
        try:
            #Waiting for the check-in date to be available
            wait = WebDriverWait(self.driver, 15)
            check_in_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]'))
            )
            check_in_element.click()
            print(f"Selected check-in date: {check_in_date}")

            #Waiting for the check-out date to be available
            check_out_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]'))
            )
            check_out_element.click()
            print(f"Selected check-out date: {check_out_date}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def select_adults(self, count=1):
        try:
            #Waiting for the guests field to be available
            wait = WebDriverWait(self.driver, 15)
            guests_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]'))
            )
            guests_button.click()
            print("Clicked guests button")
        except Exception as e:
            print(f"An error occurred: {e}")
