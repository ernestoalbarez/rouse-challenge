import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.search_page import SearchPage
from pages.region_modal import RegionModal


@pytest.fixture(scope="class")
def setup_driver(request):
    """
    Setup WebDriver and page objects for testing. Run before each test.
    """
    project_dir = os.path.dirname(os.path.dirname(__file__))
    driver_path = os.path.join(project_dir, "drivers", "chromedriver")
    logging.basicConfig(level=logging.INFO)

    # Set up ChromeDriver using Service
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)

    # Set up page objects
    request.cls.driver = driver
    request.cls.search_page = SearchPage(driver)
    request.cls.region_modal = RegionModal(driver)

    yield

    driver.quit()


@pytest.mark.usefixtures("setup_driver")
class TestDuckDuckGoSearch:
    """
    Test Cases:
        1. Verify 'android' appears in each result title.
        2. Verify the count of elements in the region modal is greater than 10.
        3. Verify that selecting a region (e.g., Korea) loads articles in that language.
    """
    
    def test_search_android_results_contain_android(self):
        """
        Test Case 1:
            Verify 'android' appears in each result title.
        """
        logging.info("Test Case 1: Searching for 'android' on DuckDuckGo page")
        self.search_page.open()
        self.search_page.search("android")
        result_spans = self.search_page.get_result_titles()

        for span in result_spans:
            span_text = span.text.lower()
            assert "android" in span_text, f"'android' not in title: {span_text}"

    def test_region_modal_elements_count(self):
        """
        Test Case 2:
            Verify region modal element count is greater than 10.
        """
        logging.info("Test Case 2: Clicking on the Region button")
        self.search_page.open()
        self.search_page.search("android")
        self.search_page.click_region_button()
        
        elements_count = self.region_modal.get_elements_count()
        assert elements_count > 10, f"Expected more than 10 elements, found {elements_count}"

    def test_switch_to_korea(self):
        """
        Test Case 3:
            Verify page changes to Korean after selecting Korea from the region dropdown.
        """
        logging.info("Test Case 3: Selecting Korea region")
        self.search_page.open()
        self.search_page.search("android")
        self.search_page.click_region_button()
        self.region_modal.search_language('korea')
        self.region_modal.select_language('zh')
        self.search_page.click_more_results_button()
        assert self.search_page.is_article_present('zh'), "Expected Korean article not found on the page"