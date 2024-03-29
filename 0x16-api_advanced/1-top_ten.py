#!/usr/bin/python3
"""
The script prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    user_agent = "MyRedditBolt/1.0"
    headers = {
        "User-Agent": user_agent
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        """Raise an exception for status codes"""
        response.raise_for_status()
        data = response.json()

        if "data" in data and "children" in data["data"]:
            """Take the first 10 posts"""
            posts = data["data"]["children"][:10]

            for post in posts:
                print(post["data"]["title"])
        else:
            print("No posts found")

    except (requests.RequestException, KeyError, ValueError):
        print("None")
