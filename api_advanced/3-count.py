#!/usr/bin/python3
"""Queries the Reddit API and prints a sorted count of given keywords."""
import requests
import string


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Prints a sorted count of given keywords in hot articles."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'ALU-Project/1.0'}
    params = {'after': after} if after else {}
    
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
                            
    if response.status_code != 200:
        return
        
    data = response.json().get("data", {})
    posts = data.get("children", [])
    
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
        
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, hot_list, after)
        
    word_counts = {}
    for word in word_list:
        word_lower = word.lower()
        if word_lower not in word_counts:
            word_counts[word_lower] = 0
            
    for title in hot_list:
        words = title.lower().split()
        for word in words:
            clean_word = word.strip(string.punctuation)
            if clean_word in word_counts:
                word_counts[clean_word] += 1
                
    sorted_counts = sorted(word_counts.items(), 
                           key=lambda item: (-item[1], item[0]))
                           
    for word, count in sorted_counts:
        if count > 0:
            print("{}: {}".format(word, count))
