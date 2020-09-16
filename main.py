import requests
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    return "AAAAAAAAAAAAAAAAAAAAAPX4HgEAAAAAf34E7izTYWADOluGxYpHB4ToKU0%3DvNiWMhi2rToyZJSxjDH2kJKrEzcMTX20ePY3mQdzyHh8gYQKXm"

def welcome():
    print("Hello! Welcome to the Tweet Guessing Game.")
    print("Given a tweet by one of two individuals, you will guess who wrote the tweet.")

def create_url(username):
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count=2".format(
        username
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


def main():
    welcome()
    bearer_token = auth()
    headers = create_headers(bearer_token)

    url = create_url("elonmusk")
    json_response = connect_to_endpoint(url, headers)
    userOneTweets = open("userOneTweets.txt", "w")
    userOneTweets.write(json.dumps(json_response, indent=4, sort_keys=True))

    url = create_url("kanyewest")
    json_response = connect_to_endpoint(url, headers)
    userTwoTweets = open("userTwoTweets.txt", "w")
    userTwoTweets.write(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()