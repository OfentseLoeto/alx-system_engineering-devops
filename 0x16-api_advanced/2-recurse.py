#!/usr/bin/python3
"""This script returns a list containing the
   titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    user_agent = ""
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response =  requests.get(url, headers=headers, params=params, allow_redirects=False)
        """Raise an exception for 4xx and 5xx status codes"""
        response.raise_for_status()
        response = data.json()

        if data in "data" and "children" in data["data"]:
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