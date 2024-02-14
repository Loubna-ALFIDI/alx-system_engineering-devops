#!/usr/bin/python3
"""
100-count
"""

import requests


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0\
        Safari/537.36'}


def count_words(subreddit, word_list):
    """Method doc"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        count = {}
        for post in data["data"]["children"]:
            for word in word_list:
                # print(word)
                if word in post["data"]["title"].lower():
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
        return count
    else:
        return None
