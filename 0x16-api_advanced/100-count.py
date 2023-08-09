#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, 
parses the title of all hot articles
and prints a sorted count of given keyword,
Javascript should count as javascript, but java should not).
"""


import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}

        user_agent = "MyRedditBot/1.0"
        headers = {
                "User-Agent": user_agent
        }
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"

        params = {
            "limit": 100,
            "after": after
        }

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
                    title = post["data"]["title"].lower()
                    for word in word_list:
                        word = word.lower()
                        if word in title and not title.startswith(f"{word}.") and not title.startswith(f"{word}!") and not title.startswith(f"{word}_"):
                            count_dict[word] = count_dict.get(word, 0) +1
                            after = data["data"]["after"]
            if after is not None:
                return count_words(subreddit, word_list, after, count_dict)
            
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")

        except (requests.RequestException, KeyError, ValueError):
            print("Invalid subreddit or request error")
