from flask import Flask, request, render_template
from apiconnect import ApiConnect
from guesstweets import GuessTweets

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")


def getUserApi(username):
    error = None
    while error == None:
        userApi = ApiConnect(username)
        if userApi.getAuthSuccess() == True:
            return userApi
        else:
            error = "Error. Please enter a valid username."
            render_template("app.html", error=error)


@app.route('/', methods=['POST'])
def processForm():
    username1 = request.form['username1'].lower()
    userOneApi = getUserApi(username1)
    username2 = request.form['username2'].lower()
    userTwoApi = getUserApi(username2)

    guesser = GuessTweets(userOneApi, userTwoApi)
    tweetText = guesser.getRandomTweet(userOneApi.getTweetList(), userTwoApi.getTweetList())
    return render_template("guess.html", tweetText=tweetText, usernameOne=username1, usernameTwo=username2)

def main():
    repeat = True
    while repeat == True:
        guesser.getRandomTweet(userOneApi.getTweetList(), userTwoApi.getTweetList())
        render_template("base.html", repeat=repeat)

    guesser.getStatistics()


if __name__ == "__main__":
    main()