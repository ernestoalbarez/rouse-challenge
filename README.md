# DuckDuckGo Search and API Test Automation

## Overview

This project is a Python-based test automation framework that tests both the DuckDuckGo search engine UI and the DuckDuckGo API. It leverages the `unittest` framework and `Selenium` for UI testing, along with `requests` for API testing. The framework consists of several test cases that validate the functionality of DuckDuckGo's search features and its API response handling.

## Project Structure

```
rouse-challenge/
├── drivers/
│   └── chromedriver
├── pages/
│   ├── region_modal.py
│   └── search_page.py
├── tests/
│   ├── test_api.py
│   └── test_search.py
├── locators.py
├── testrunner.py
├── requirements.txt
└── README.md
```

## Features
- **UI Testing:** Validates the search functionality and region selection in DuckDuckGo’s web interface.
- **API Testing:** Handles and validates JSON responses from DuckDuckGo’s API.
- **Extensible Framework:** The architecture allows for easy addition of new tests and enhancements.
- **Clear Output:** Test results are clearly printed to the console, making it easy to identify any issues.

## Installation

1. **Clone the Repository**
   ```
   git clone <your-repository-url>
   cd rouse-challenge
   ```

2. **Set Up a Virtual Environment**
    ```
    python -m venv venv  
    source venv/bin/activate
    ```
    On Windows use `venv\Scripts\activate`

3. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Download ChromeDriver**

    Ensure that the version of ChromeDriver matches your installed Chrome browser version. Place the chromedriver executable in the drivers/ directory.

## Running Tests
You can run all tests using the following command:
```
python run_tests.py
```

Alternatively, you can run individual test files:
```
python -m unittest tests.test_search.py
python -m unittest tests.test_api.py
```

## Test Cases

### Test Search
1.	Verify ‘android’ appears in each result title.
2.	Verify region modal element count is greater than 10.

### Test API
1.	Handle JSON response from the DuckDuckGo API and print the Icon URL if it’s not null.