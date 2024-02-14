#!/usr/bin/python3
"""
2-recurse
"""
import requests


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0\
        Safari/537.36'}


def recurse(subreddit, after=None):
    """method doc"""
    params = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, allow_redirects=False,
                            headers=headers, params=params)
    all_posts = []
    if response.status_code == 200:
        data = response.json()
        after = data["data"]["after"]
        if after is None:
            return all_posts
        for post in data["data"]["children"]:
            all_posts.append(post["data"]["title"])
        next = recurse(subreddit, after)
        all_posts.extend(next)
        return all_posts
    return None
