import requests
import json
import random

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    return "AAAAAAAAAAAAAAAAAAAAAPX4HgEAAAAAf34E7izTYWADOluGxYpHB4ToKU0%3DvNiWMhi2rToyZJSxjDH2kJKrEzcMTX20ePY3mQdzyHh8gYQKXm"

def welcome():
    print("Hello! Welcome to the Tweet Guessing Game.")
    print("Given a tweet by one of two individuals, guess who wrote the tweet!")


def create_url(username):
    numTweets = 2
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}&exclude_replies=true".format(
        username, numTweets
    )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def randomUserGenerator():
    return random.randint(1, 2)

def randomTweetGenerator(userNumber, userOneTweets, userTwoTweets):
    if userNumber == 1:
        tweetIndex = round(random.random()*len(userOneTweets))
        return userOneTweets[int(tweetIndex)]
    else:
        tweetIndex = round(random.random()*len(userTwoTweets))
        return userTwoTweets[int(tweetIndex)]


def verifyGuess(userNumber, guess):
    if userNumber == guess:
        print("Correct!\n")
    else:
        print("Incorrect!\n")


def main():
    welcome()
    bearer_token = auth()
    headers = create_headers(bearer_token)

    url = create_url("elonmusk")
    json_tweets_1 = connect_to_endpoint(url, headers)

    url = create_url("kanyewest")
    json_tweets_2 = connect_to_endpoint(url, headers)

    userNumber = randomUserGenerator()
    jsonTweet = randomTweetGenerator(userNumber, json_tweets_1, json_tweets_2)
    print(jsonTweet['text'])
    guess = input("Who wrote this tweet? Enter '1' for Elon Musk, '2' for Kanye West:")
    verifyGuess(userNumber, int(guess))


if __name__ == "__main__":
    main()