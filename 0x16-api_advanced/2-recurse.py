#!/usr/bin/python3
"""
This script returns a list containing the
titles of all hot articles for a given subreddit.
"""
#!/usr/bin/python3
"""
The script prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    user_agent = "MyRedditBot/1.0"
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {"limit": 10}
    if after:
        params["after"] = after

    try:
        response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False
        )

        response.raise_for_status()
        data = response.json()

        if "data" in data and "children" in data["data"]:
            posts = data["data"]["children"]
            for post in posts:
                hot_list.append(post["data"]["title"])

            after = data["data"]["after"]
            if after:
                recurse(subreddit, hot_list, after)
            else:
                return hot_list

        else:
            return None

    except (requests.RequestException, KeyError, ValueError):
        return None
