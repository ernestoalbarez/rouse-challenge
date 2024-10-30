from selenium.webdriver.common.by import By

class SearchPageLocators:
    SEARCH_INPUT = (By.ID, "searchbox_input")
    RESULT_TITLES = (By.XPATH, "//ol[@class='react-results--main']//article[@data-testid='result']")
    REGION_BUTTON = (By.XPATH, "//a[@data-testid='region-filter-label']")

class RegionModalLocators:
    REGION_MODAL_ELEMENTS = (By.CSS_SELECTOR, "div.BDI1KtNF8HUPBZ4Cw_nK")