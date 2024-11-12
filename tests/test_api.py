import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import config

def test_handle_json_response():
    """
    Test Case:
        Verify the DuckDuckGo API returns valid JSON with 'RelatedTopics' containing icon URLs.
    """
    response = requests.get(config.API_URL, headers=config.API_HEADERS)
    assert response.status_code == 200, "API request was not successful"

    # Parse JSON response
    data = response.json()
    related_topics = data.get("RelatedTopics", [])

    # Check if 'RelatedTopics' is present and contains icon URLs
    if related_topics:
        print("RelatedTopics found in response:")
        for topic in related_topics:
            if "Icon" in topic and "URL" in topic["Icon"]:
                print(f"Icon URL: {topic['Icon']['URL']}")
            
            # If the item is a category with a 'Topics' list
            elif "Topics" in topic:
                for sub_topic in topic["Topics"]:
                    if "Icon" in sub_topic and "URL" in sub_topic["Icon"]:
                        print(f"Icon URL: {sub_topic['Icon']['URL']}")
    else:
        print("No RelatedTopics available in the response.")