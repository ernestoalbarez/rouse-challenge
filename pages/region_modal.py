from selenium.webdriver.common.by import By
from locators import RegionModalLocators

class RegionModal:
    def __init__(self, driver):
        self.driver = driver

    def get_elements_count(self):
        elements = self.driver.find_elements(*RegionModalLocators.REGION_MODAL_ELEMENTS)
        return len(elements)