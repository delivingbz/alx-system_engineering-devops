#!/usr/bin/python3
"""
Query Reddit API to determine subreddit subscribers count
"""

from requests import get


def top_ten(subreddit):
    """ Request the numbers of subreddit subscribers from
    Reddit API
    """
    # sets custom user-agent
    user_agent = '0x16-api_advanced-UnfazedAy'
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    # custom user agent avoids request-limit
    headers = {'User-Agent': user_agent}

    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None
    else:
        data = response.json()['data']
        posts = data['children']
        for post in posts:
            print(post.get('data').get('title'))
