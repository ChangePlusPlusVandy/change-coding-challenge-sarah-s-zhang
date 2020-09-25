from flask import Flask, render_template
import json
import random

class GuessTweets:

    def __init__(self, userOne, userTwo):
        self.__userOne = userOne
        self.__userTwo = userTwo
        self.__userNum = 0
        self.__totalTweetsGuessed = 0
        self.__totalUserOneCorrect = 0
        self.__totalUserOneIncorrect = 0
        self.__totalUserTwoCorrect = 0
        self.__totalUserTwoIncorrect = 0


    def __randomTweetGenerator(self, userNumber, userOneTweets, userTwoTweets):
        if userNumber == 1:
            return random.choice(userOneTweets)
        else:
            return random.choice(userTwoTweets)


    def verifyGuess(self, userNumber, guess):
        guess = int(guess)

        self.__totalTweetsGuessed += 1
        if self.__userNum == guess:
            if self.__userNum == 1:
                self.__totalUserOneCorrect += 1
            else:
                self.__totalUserTwoCorrect += 1
            return True
        else:
            if self.__userNum == 1:
                self.__totalUserOneIncorrect += 1
                return 1
            else:
                self.__totalUserTwoIncorrect += 1
            return False


    def getRandomTweet(self, userOneTweetList, userTwoTweetList):
        self.__userNum = random.randint(1, 2)
        jsonTweet = self.__randomTweetGenerator(self.__userNum, userOneTweetList, userTwoTweetList)
        return jsonTweet['text']

    
    def getUserNum(self):
        return self.__userNum
    
    
    def getStatistics(self):
        print("\n****GUESSING GAME STATISTICS****")
        print("Total tweets guessed: ", self.__totalTweetsGuessed)
        print("- Total correct: ", self.__totalUserOneCorrect + self.__totalUserTwoCorrect)
        print("- Total incorrect: ", self.__totalUserOneIncorrect + self.__totalUserTwoIncorrect)
        print("Total @" + self.__userOne, "tweets guessed:", self.__totalUserOneCorrect + self.__totalUserOneIncorrect)
        print(" - Total @" + self.__userOne, "correct:", self.__totalUserOneCorrect)
        print(" - Total @" + self.__userOne, "incorrect:", self.__totalUserOneIncorrect)
        print("Total @" + self.__userTwo, "tweets guessed:", self.__totalUserTwoCorrect + self.__totalUserTwoIncorrect)
        print(" - Total @" + self.__userTwo, "correct:", self.__totalUserTwoCorrect)
        print(" - Total @" + self.__userTwo, "incorrect:", self.__totalUserTwoIncorrect)