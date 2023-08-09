#!/usr/bin/python3
"""The script returns the number of subscribers
   (not active users, total subscribers) for a given subreddit.
"""



import requests

def number_of_subscribers(subreddit):
    user_agent = ""
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        except (KeyError, ValueError):
            return 0
    else:
        return 0
