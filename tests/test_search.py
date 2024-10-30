import unittest
import os

from selenium import webdriver
from pages.search_page import SearchPage
from pages.region_modal import RegionModal
from selenium.webdriver.chrome.service import Service


class DuckDuckGoSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        project_dir = os.path.dirname(os.path.dirname(__file__))
        driver_path = os.path.join(project_dir, "drivers", "chromedriver")

        # Set up ChromeDriver using Service
        service = Service(driver_path)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)
        cls.search_page = SearchPage(cls.driver)
        cls.region_modal = RegionModal(cls.driver)

    def test_search_android_results_contain_android(self):
        """
            Test Case 1:
                Verify 'android' appears in each result title.
        """
        self.search_page.open()
        self.search_page.search("android")
        result_spans = self.search_page.get_result_titles()

        for span in result_spans:
            span_text = span.text.lower()
            self.assertIn("android", span_text, f"'android' not in title: {span_text}")

    def test_region_modal_elements_count(self):
        """
            Test Case 2:
                Verify region modal element count is greater than 10.
        """
        self.search_page.open()
        self.search_page.search("android")
        self.search_page.click_region_button()
        
        elements_count = self.region_modal.get_elements_count()
        self.assertGreater(elements_count, 10, f"Expected more than 10 elements, found {elements_count}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()