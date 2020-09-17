import json
import random
from apiconnect import ApiConnect


def welcome():
    print("Hello! Welcome to the Tweet Guessing Game.")
    print("Given a tweet by one of two individuals, guess who wrote the tweet!\n")

def randomUserGenerator():
    return random.randint(1, 2)

def randomTweetGenerator(userNumber, userOneTweets, userTwoTweets):
    if userNumber == 1:
        return random.choice(userOneTweets)
    else:
        return random.choice(userTwoTweets)


def verifyGuess(userNumber, guess):
    if userNumber == guess:
        print("\nCorrect!\n")
        return True
    else:
        print("\nIncorrect!\n")
        return False


def main():
    welcome()
    
    userOne = ApiConnect("elonmusk")
    json_tweets_1 = userOne.getTweets()

    userTwo = ApiConnect("kanyewest")
    json_tweets_2 = userTwo.getTweets()

    userNumber = randomUserGenerator()
    jsonTweet = randomTweetGenerator(userNumber, json_tweets_1, json_tweets_2)
    print(jsonTweet['text'])
    guess = input("\nWho wrote this tweet? Enter '1' for Elon Musk, '2' for Kanye West: ")
    verifyGuess(userNumber, int(guess))


if __name__ == "__main__":
    main()