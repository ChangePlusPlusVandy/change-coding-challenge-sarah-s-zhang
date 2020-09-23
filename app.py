from flask import Flask, request, render_template
from apiconnect import ApiConnect
from guesstweets import GuessTweets

app = Flask(__name__)
app.config.from_object('config.DevConfig')

@app.route("/")
def home():
    return render_template("app.html")


@app.route('/', methods=['POST'])
def getUsername():
    text = request.form['text']
    username = text.lower()

    error = None
    while error == None:
        userApi = ApiConnect(username)
        if userApi.getAuthSuccess() == True:
            return userApi
        else:
            error = "Error. Please enter a valid username."
            render_template("app.html", error=error)

@app.route('/guess/')
def guessUsername():
    

def main():
    userOneApi = getUsername()
    userTwoApi = getUsername()
    guesser = GuessTweets(userOneApi, userTwoApi)
    repeat = True
    while repeat == True:
        guesser.getRandomTweet(userOneApi.getTweetList(), userTwoApi.getTweetList())
        render_template("app.html", repeat=repeat)

    guesser.getStatistics()


if __name__ == "__main__":
    main()