from flask import Flask
from flask import render_template

import random
import glob
import json

application = Flask(__name__)

BLOCKED_LIST = set({"Movies.json"})
BLOCKED_LIST_WITH_PATH = {f"./data/{blockedFile}" for blockedFile in BLOCKED_LIST}


@application.route("/")
def index():
    return render_template("index.html", words=words)


def loadChoices():
    global choices

    for wordFile in glob.glob("./data/*.json"):
        if wordFile in BLOCKED_LIST_WITH_PATH:
            continue
        fin = open(wordFile, "r")
        data = json.load(fin)
        fin.close()
        choices.extend(data)


def selectWords():
    global words
    global choices

    words = random.sample(choices, 5)


@application.route("/newWords", methods=["POST"])
def newWords():
    selectWords()

    return "1"


choices = []
words = []

loadChoices()
selectWords()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5000)