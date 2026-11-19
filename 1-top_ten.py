#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    url = "https://old.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) '
                      'Gecko/20100101 Firefox/115.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
