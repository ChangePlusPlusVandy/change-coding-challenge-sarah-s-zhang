from guesstweets import GuessTweets

def welcome():
    print("Hello! Welcome to the Tweet Guessing Game.")
    print("Given a tweet by one of two individuals, guess who wrote the tweet!\n")

def main():
    welcome()

    userOne = input("Enter a Twitter username: @")
    userTwo = input("Enter another Twitter username: @")

    guesser = GuessTweets(userOne, userTwo)
    repeat = "y"
    while repeat == "y":
        guesser.getRandomTweet()
        repeat = input("\nEnter 'y' to play again: ").lower()

    guesser.getStatistics()


if __name__ == "__main__":
    main()