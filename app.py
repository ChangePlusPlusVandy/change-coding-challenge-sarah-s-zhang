from flask import Flask, request, redirect, render_template
from apiconnect import ApiConnect
from guesstweets import GuessTweets
import config

app = Flask(__name__)
# app.secret_key = config.secret_key


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/', methods=['POST'])
def processForm():
    username1 = request.form['username1'].lower()
    userOneApi = ApiConnect(username1)
    username2 = request.form['username2'].lower()
    userTwoApi = ApiConnect(username2)
    if userOneApi.getAuthSuccess() == False or userTwoApi.getAuthSuccess() == False:
        return render_template("base.html", error="Error. Please enter a valid username.")
    return guessTweet(userOneApi, userTwoApi)


@app.route('/guess')
def guessTweet(userOneApi, userTwoApi):
    guesser = GuessTweets(userOneApi, userTwoApi)
    tweetText = guesser.getRandomTweet(userOneApi.getTweetList(), userTwoApi.getTweetList())
    return render_template("guess.html", tweetText=tweetText, usernameOne=userOneApi.getUsername(), usernameTwo=userTwoApi.getUsername())