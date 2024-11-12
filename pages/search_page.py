from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import SearchPageLocators
import config

class SearchPage:
    """
    Page Object for Search Page. Handles interactions with the DuckDuckGo search page.
    """
    def __init__(self, driver):
        self.driver = driver
        self.url = config.BASE_URL

    def open(self):
        """
        Open the DuckDuckGo search page.
        """
        self.driver.get(self.url)

    def search(self, query):
        """
        Perform a search on DuckDuckGo with the given query.
        """
        search_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SearchPageLocators.SEARCH_INPUT)
        )
        search_field.clear()
        search_field.send_keys(query)
        search_field.send_keys(Keys.RETURN)

    def get_result_titles(self):
        """
        Return the list of result titles from the search results.
        """
        articles = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(SearchPageLocators.RESULT_TITLES)
        )
        spans = [article.find_element(By.XPATH, ".//div/h2/a/span") for article in articles]
        return spans

    def click_region_button(self):
        """
        Click the Region button to open the region selection modal.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SearchPageLocators.REGION_BUTTON)
        ).click()

    def click_more_results_button(self):
        """
        Click the 'More Results' button to load more search results.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SearchPageLocators.MORE_RESULTS_BUTTON)
        ).click()

    def is_article_present(self, language):
        """
        Check if an article in the selected language is present.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SearchPageLocators.WIKI_PAGE[language])
            )
            return True
        except TimeoutException:
            return False