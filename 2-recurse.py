#!/usr/bin/python3
"""Queries the Reddit API and returns a list of all hot articles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns a list of titles of all hot articles."""
    url = "https://old.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) '
                      'Gecko/20100101 Firefox/115.0'
    }
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None if not hot_list else hot_list
    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
