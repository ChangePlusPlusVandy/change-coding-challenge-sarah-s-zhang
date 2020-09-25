# @author Sarah Zhang, Twitter API Sample Code

import config
import requests

# class ApiConnect
#   Accesses the Twitter API to get Tweets from a specific username
class ApiConnect:

    # Constructor
    def __init__(self, username):
        self.__username = username
        self.__authSuccess = False
        headers = self.__create_headers(config.bearer_token)
        url = self.__create_url(self.__username)
        self.__jsonResponse = self.__connect_to_endpoint(url, headers)

    # __create_headers
    #   create headers to access the API
    def __create_headers(self, bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers

    # __create_url
    #   create URL to access the API
    def __create_url(self, username):
        numTweets = 3200
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}&exclude_replies=true&include_rts=false".format(
            username, numTweets
        )
        return url
    
    # __connect_to_endpoint
    #   HTTP GET request to the Twitter API
    def __connect_to_endpoint(self, url, headers):
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print("Failed to connect to Twitter. Please enter a valid username.")
        else:
            self.__authSuccess = True
            return response.json()
    
    # getUsername()
    #   returns the username string
    def getUsername(self):
        return self.__username
    
    # getAuthSuccess()
    #   returns true if Twitter API connection is successful, false if unsuccessful
    def getAuthSuccess(self):
        return self.__authSuccess
    
    # getTweetList()
    #   returns the list of Tweets in JSON format
    def getTweetList(self):
        return self.__jsonResponse