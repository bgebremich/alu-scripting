#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'ALU-Project/1.0'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
        
    data = response.json().get("data", {})
    return data.get("subscribers", 0)
