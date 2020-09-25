import config
import requests

class ApiConnect:


    def __init__(self, username):
        self.__username = username
        self.__authSuccess = False
        headers = self.__create_headers(config.bearer_token)
        url = self.__create_url(self.__username)
        self.__jsonResponse = self.__connect_to_endpoint(url, headers)


    def __create_headers(self, bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers


    def __create_url(self, username):
        numTweets = 3200
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}&exclude_replies=true&include_rts=false".format(
            username, numTweets
        )
        return url
    

    def __connect_to_endpoint(self, url, headers):
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            return False
        else:
            self.__authSuccess = True
            return response.json()
    

    def getUsername(self):
        return self.__username
    

    def getAuthSuccess(self):
        return self.__authSuccess
    

    def getTweetList(self):
        return self.__jsonResponse