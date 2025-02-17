from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def apply_star_rating(self, *star_values):
        try:
            wait = WebDriverWait(self.driver, 15)
            star_filteration_box = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-filters-group="class"][data-testid="filters-group"]')
            ))
            star_child_elements = star_filteration_box.find_elements(
                By.CSS_SELECTOR, '*'
            )
            print(len(star_child_elements))

            for star in star_values:
                target = None
            #searching through child elements to find the star rating
                for child in star_child_elements:
                    if child.tag_name.lower() == "input":
                        name_attr = child.get_attribute("name")
                        if name_attr == f"class={star}":
                            target = child
                            break
                if target:
                    #scrolling to the element
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
                    self.driver.execute_script("window.scrollBy(0, -150);")
                    #waiting until the target is clickable
                    wait.until(lambda d: target.is_enabled())
                    target.click()
                    print(f"Clicked on star rating: {star}")
                else:
                    print(f"Star rating {star} not found")
        except Exception as e:
            print(f" Error: {e}")
