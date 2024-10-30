from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SearchPageLocators


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://start.duckduckgo.com/"

    def open(self):
        self.driver.get(self.url)

    def search(self, query):
        search_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SearchPageLocators.SEARCH_INPUT)
        )
        search_field.clear()
        search_field.send_keys(query)
        search_field.send_keys(Keys.RETURN)

    def get_result_titles(self):
        articles = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(SearchPageLocators.RESULT_TITLES)
        )
        spans = [article.find_element(By.XPATH, ".//div/h2/a/span") for article in articles]
        return spans

    def click_region_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SearchPageLocators.REGION_BUTTON)
        ).click()