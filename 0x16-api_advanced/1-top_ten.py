#!/usr/bin/python3

"""
This module provides a function to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Reddit Top Ten Posts Viewer by /u/yourusername"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print("None")

if __name__ == "__main__":
    subreddit_name = input("Enter the name of the subreddit: ")
    print(f"Top 10 hot posts in /r/{subreddit_name}:")
    top_ten(subreddit_name)
