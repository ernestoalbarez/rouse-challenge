from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegionModalLocators

class RegionModal:
    """
    Page Object for Region Modal. Handles interactions with the region selection modal.
    """
    def __init__(self, driver):
        self.driver = driver

    def get_elements_count(self):
        """
        Return the number of elements displayed in the region modal.
        """
        elements = self.driver.find_elements(*RegionModalLocators.REGION_MODAL_ELEMENTS)
        return len(elements)

    def search_language(self, language):
        """
        Search for a specific language in the region modal's search input.
        """
        language_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RegionModalLocators.REGION_SEARCH)
        )
        language_input.clear()
        language_input.send_keys(language)

    def select_language(self, language):
        """
        Select a language from the region modal by clicking on the corresponding region.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RegionModalLocators.REGION[language])
        ).click()