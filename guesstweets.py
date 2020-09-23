# @author Sarah Zhang

import json
import random

# class GuessTweets
#   Chooses a random tweet, verifies the user's guess as to who wrote the tweet,
#       and generates statistics for the guessing game
class GuessTweets:

    # Constructor
    def __init__(self, userOne, userTwo):
        self.userOne = userOne
        self.userTwo = userTwo
        self.totalTweetsGuessed = 0
        self.totalUserOneCorrect = 0
        self.totalUserOneIncorrect = 0
        self.totalUserTwoCorrect = 0
        self.totalUserTwoIncorrect = 0

    # __randomTweetGenerator(userNumber, userOneTweets, userTwoTweets)
    #   Returns a random tweet from the given username
    def __randomTweetGenerator(self, userNumber, userOneTweets, userTwoTweets):
        if userNumber == 1:
            return random.choice(userOneTweets)
        else:
            return random.choice(userTwoTweets)

    # __verifyGuess(userNumber, guess)
    #   Verifies the user's guess as to who wrote the tweet
    def __verifyGuess(self, userNumber, guess):
        while guess != "1" and guess != "2":
            guess = input("Error. Please enter '1' or '2': ")

        self.totalTweetsGuessed += 1
        if userNumber == int(guess):
            if userNumber == 1:
                self.totalUserOneCorrect += 1
            else:
                self.totalUserTwoCorrect += 1
            print("\nCorrect!")
        else:
            if userNumber == 1:
                self.totalUserOneIncorrect += 1
            else:
                self.totalUserTwoIncorrect += 1
            print("\nIncorrect!")

    # getRandomTweet(userOneTweetList, userTwoTweetList)
    # - Chooses a random username and prints a random tweet
    # - Prompts the user to guess who wrote the tweet, and verifies the guess
    def getRandomTweet(self, userOneTweetList, userTwoTweetList):
        randomUser = random.randint(1, 2)
        jsonTweet = self.__randomTweetGenerator(randomUser, userOneTweetList, userTwoTweetList)
        print(jsonTweet['text'])
        guess = input("\nWho wrote this tweet? Enter '1' for @" + self.userOne + " OR '2' for @" + self.userTwo + ": ")
        self.__verifyGuess(randomUser, guess)
    
    # getStatistics()
    #   Prints the guessing game statistics throughout the whole game
    def getStatistics(self):
        print("\n****GUESSING GAME STATISTICS****")
        print("Total tweets guessed: ", self.totalTweetsGuessed)
        print("- Total correct: ", self.totalUserOneCorrect + self.totalUserTwoCorrect)
        print("- Total incorrect: ", self.totalUserOneIncorrect + self.totalUserTwoIncorrect)
        print("Total @" + self.userOne, "tweets guessed:", self.totalUserOneCorrect + self.totalUserOneIncorrect)
        print(" - Total @" + self.userOne, "correct:", self.totalUserOneCorrect)
        print(" - Total @" + self.userOne, "incorrect:", self.totalUserOneIncorrect)
        print("Total @" + self.userTwo, "tweets guessed:", self.totalUserTwoCorrect + self.totalUserTwoIncorrect)
        print(" - Total @" + self.userTwo, "correct:", self.totalUserTwoCorrect)
        print(" - Total @" + self.userTwo, "incorrect:", self.totalUserTwoIncorrect)