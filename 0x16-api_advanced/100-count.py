#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, 
parses the title of all hot articles
and prints a sorted count of given keyword,
Javascript should count as javascript, but java should not).
"""


import requests


def count_words(subreddit, word_list, after=None, counter=None):
    if counter is None:
        counter = {}

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
            """Raise an exception for status codes"""
            response.raise_for_status()
            data = response.json()

            if "data" in data and "children" in data["data"]:
                posts = data["data"]["children"]

                for post in posts:
                    title = post["data"]["title"].lower()
                    for word in word_list:
                        if word.lower() in title and title.startswith(word.lower() + " "):
                            if word not in counter:
                                counter[word] = 1
                            else:
                                counter[word] += 1
            if len(posts) > 0:
                after = posts[-1]["data"]["name"]
                return count_words(subreddit, word_list, after, counter)
            else:
                sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counter:
                    print(f"{word.lower()}: {counter}")

        except (requests.RequestException, KeyError, ValueError):
            pass
