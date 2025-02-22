#In this we're going to parse the data required from the various options/deals. 
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
    def __init__(self, boxes_section_element):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()
        
    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_class_name('sr_property_block')

    def pull_titles(self):
        collection = []
        
        for deal in self.deal_boxes:
            #Pulling the hotel name
            hotel_name = deal.find_element_by_class_name('sr-hotel__name').get_attribute('innerHTML').strip()
            hotel_score = deal.find_element_by_class_name('bui-review-score__badge').get_attribute('innerHTML').strip()
            hotel_price = deal.find_element_by_class_name('bui-price-display__value').get_attribute('innerHTML').strip()

            collection.append({
                'hotel_name': hotel_name,
                'hotel_score': hotel_score,
                'hotel_price': hotel_price
            })

            return collection

