#!/usr/bin/python3

"""
This module provides a function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Reddit Subscribers Checker by /u/yourusername"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

if __name__ == "__main__":
    subreddit_name = input("Enter the name of the subreddit: ")
    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
