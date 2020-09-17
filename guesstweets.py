import json
import random

class GuessTweets:

    def __init__(self, userOne, userTwo):
        self.userOne = userOne
        self.userTwo = userTwo
        self.totalTweetsGuessed = 0
        self.totalUserOneCorrect = 0
        self.totalUserOneIncorrect = 0
        self.totalUserTwoCorrect = 0
        self.totalUserTwoIncorrect = 0

    def __randomTweetGenerator(self, userNumber, userOneTweets, userTwoTweets):
        if userNumber == 1:
            return random.choice(userOneTweets)
        else:
            return random.choice(userTwoTweets)

    def __verifyGuess(self, userNumber, guess):
        while guess != "1" and guess != "2":
            guess = input("Error. Please enter '1' or '2': ")
        guess = int(guess)

        self.totalTweetsGuessed += 1
        if userNumber == guess:
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

    def getRandomTweet(self, userOneTweetList, userTwoTweetList):
        randomUser = random.randint(1, 2)
        jsonTweet = self.__randomTweetGenerator(randomUser, userOneTweetList, userTwoTweetList)
        print(jsonTweet['text'])
        guess = input("\nWho wrote this tweet? Enter '1' for @" + self.userOne + " OR '2' for @" + self.userTwo + ": ")
        self.__verifyGuess(randomUser, guess)
    
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