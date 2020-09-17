from apiconnect import ApiConnect
from guesstweets import GuessTweets

def welcome():
    print("Hello! Welcome to the Tweet Guessing Game.")
    print("Given a tweet by one of two individuals, guess who wrote the tweet!\n")

def checkUsername():
    isValidUsername = False
    while isValidUsername == False:
        username = input("Enter a Twitter username: @")
        userApi = ApiConnect(username)
        if userApi.getAuthSuccess() == True:
            isValidUsername = True
            return userApi

def main():
    welcome()
    userOneApi = checkUsername()
    userTwoApi = checkUsername()

    guesser = GuessTweets(userOneApi.getUsername(), userTwoApi.getUsername())
    repeat = "y"
    while repeat == "y":
        guesser.getRandomTweet(userOneApi.getTweetList(), userTwoApi.getTweetList())
        repeat = input("\nEnter 'y' to play again or any other key to stop: ").lower()

    guesser.getStatistics()


if __name__ == "__main__":
    main()