#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = "https://old.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) '
                      'Gecko/20100101 Firefox/115.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data", {})
    return data.get("subscribers", 0)
