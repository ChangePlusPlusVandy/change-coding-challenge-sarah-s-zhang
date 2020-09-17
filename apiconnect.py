import config
import requests

class ApiConnect:

    def __init__(self, username):
        self.username = username

    def __create_headers(self, bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers

    def __create_url(self, username):
        numTweets = 3200
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}&exclude_replies=true".format(
            username, numTweets
        )
        return url
    
    def __connect_to_endpoint(self, url, headers):
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()
    
    def getTweetList(self):
        headers = self.__create_headers(config.bearer_token)
        url = self.__create_url(self.username)
        jsonTweets = self.__connect_to_endpoint(url, headers)
        return jsonTweets