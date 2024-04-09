#!/usr/bin/python3

"""
This module provides a recursive function to query the Reddit API, parse the title of all hot articles, and print a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, count_dict=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.
    
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        count_dict (dict): A dictionary to store the counts of keywords. Default is None.
        
    Returns:
        None
    """
    if count_dict is None:
        count_dict = {}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit Word Counter by /u/yourusername"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    count_dict[word.lower()] = count_dict.get(word.lower(), 0) + title.count(word.lower())
        if data['data']['after'] is not None:
            return count_words(subreddit, word_list, count_dict)
        else:
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Nothing")

if __name__ == "__main__":
    subreddit_name = input("Enter the name of the subreddit: ")
    word_list = input("Enter the keywords separated by spaces: ").split()
    count_words(subreddit_name, word_list)
