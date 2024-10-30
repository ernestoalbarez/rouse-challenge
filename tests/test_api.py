import unittest
import requests

class DuckDuckGoApiTests(unittest.TestCase):
    def test_handle_json_response(self):
        """
            Test Case 3:
                Handle JSON response from the DuckDuckGo API and print the Icon URL if it's not null.
        """
        url = "https://api.duckduckgo.com/?q=simpsons&format=json"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, "API request was not successful")

        data = response.json()
        icon = data.get("Icon")
        if icon and icon.get("URL"):
            icon_url = icon["URL"]
            print(f"Icon URL: {icon_url}")
        else:
            print("No Icon URL available.")
            self.assertIsNone(icon, "Expected an icon but found none.")

if __name__ == "__main__":
    unittest.main()