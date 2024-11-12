from selenium.webdriver.common.by import By

class SearchPageLocators:
    SEARCH_INPUT = (By.ID, "searchbox_input")
    RESULT_TITLES = (By.XPATH, "//ol[@class='react-results--main']//article[@data-testid='result']")
    REGION_BUTTON = (By.XPATH, "//a[@data-testid='region-filter-label']")
    MORE_RESULTS_BUTTON = (By.ID, "more-results")
    
    WIKI_PAGE = {
        'es': (By.XPATH, "//a[@href='https://es.wikipedia.org/wiki/Android']"),
        'en': (By.XPATH, "//a[@href='https://en.wikipedia.org/wiki/Android']"),
        'de': (By.XPATH, "//a[@href='https://de.wikipedia.org/wiki/Android']"),
        'zh': (By.XPATH, "//a[@href='https://zh.wikipedia.org/wiki/Android']")
    }

class RegionModalLocators:
    REGION_MODAL_ELEMENTS = (By.CSS_SELECTOR, "div.BDI1KtNF8HUPBZ4Cw_nK")    
    REGION_SEARCH = (By.XPATH, "//div[@data-testid='dropdown-options']//input")
    
    REGION = {
        'es': (By.XPATH, "//div[@data-testid='dropdown-options']//span[contains(text(), 'Argentina')]"),
        'en': (By.XPATH, "//div[@data-testid='dropdown-options']//span[contains(text(), 'Estados Unidos')]"),
        'de': (By.XPATH, "//div[@data-testid='dropdown-options']//span[contains(text(), 'Alemania')]"),
        'zh': (By.XPATH, "//div[@data-testid='dropdown-options']//span[contains(text(), 'Korea')]")
    }
    
    # Possible dynamic way to select any region by partial name (you can add more dynamic locators based on text)
    @staticmethod
    def get_region_by_name(region_name):
        return (By.XPATH, f"//div[@data-testid='dropdown-options']//span[contains(text(), '{region_name}')]")