#!/usr/bin/python3

"""
This module provides a recursive function to query the Reddit API and return a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles. Default is an empty list.
        
    Returns:
        list or None: A list containing the titles of all hot articles for the subreddit, or None if no results are found or the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit Hot Articles Viewer by /u/yourusername"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after'] is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None

if __name__ == "__main__":
    subreddit_name = input("Enter the name of the subreddit: ")
    hot_articles = recurse(subreddit_name)
    if hot_articles is not None:
        print("Hot articles in /r/{}:".format(subreddit_name))
        for article in hot_articles:
            print(article)
    else:
        print("None")
