#!/usr/bin/python3
"""
Query Reddit API to determine subreddit subscribers count
"""

from requests import get


def number_of_subscribers(subreddit):
    """ Request the numbers of subreddit subscribers from
    Reddit API
    """
    # sets custom user-agent
    user_agent = '0x16-api_advanced-UnfazedAy'
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    # custom user agent avoids request-limit
    headers = {'User-Agent': user_agent}

    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    # load response unit from json
    data = response.json()['data']
    # extract list of pages
    pages = data['children']
    # extract data from first page
    page_data = pages[0]['data']
    # return number of subreddit subs
    return page_data['subreddit_subscribers']
