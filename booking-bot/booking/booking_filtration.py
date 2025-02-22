from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *stars):
        wait = WebDriverWait(self.driver, 15)
        for star in stars:
            try:
                # Re-find the star filter box each time
                star_filter_box = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'div[data-filters-group="class"][data-testid="filters-group"]')
                ))
                children = star_filter_box.find_elements(By.CSS_SELECTOR, '*')

                target = None
                for child in children:
                    if child.tag_name.lower() == "input":
                        if child.get_attribute("name") == f"class={star}":
                            target = child
                            break

                if target:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
                    self.driver.execute_script("window.scrollBy(0, -150);")
                    wait.until(lambda d: target.is_enabled())
                    target.click()
                    print(f"Clicked on star rating: {star}")

                    # Wait for property cards to reload
                    wait.until(EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, 'div[data-testid="property-card"]')
                    ))
                else:
                    print(f"Star rating {star} not found.")
            except Exception as e:
                print(f"Error applying star rating {star}: {e}")

    def apply_meals_filter(self, *meal_values):
        wait = WebDriverWait(self.driver, 15)
        for val in meal_values:
            try:
                # Re-find the meal filter box each time
                meal_box = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'div[data-filters-group="mealplan"][data-testid="filters-group"]')
                ))
                children = meal_box.find_elements(By.CSS_SELECTOR, '*')

                target = None
                for child in children:
                    if child.tag_name.lower() == "input":
                        if child.get_attribute("name") == val:
                            target = child
                            break

                if target:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
                    self.driver.execute_script("window.scrollBy(0, -150);")
                    wait.until(lambda d: target.is_enabled())
                    target.click()
                    print(f"Clicked meals filter: {val}")

                    # Wait for property cards to reload
                    wait.until(EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, 'div[data-testid="property-card"]')
                    ))
                else:
                    print(f"Meals filter {val} not found.")
            except Exception as e:
                print(f"Error applying meal filter {val}: {e}")

    def sort_by_price_lowest_best_review(self):
        wait = WebDriverWait(self.driver, 15)
        try:
            sort_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
            ))
            sort_button.click()
            print("Clicked sort button dropdown")

            best_reviewed = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[data-id="review_score_and_price"]')
            ))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", best_reviewed)
            self.driver.execute_script("window.scrollBy(0, -150);")
            best_reviewed.click()
            print("Clicked best reviewed option")
        except Exception as e:
            print(f"Error while sorting: {e}")
