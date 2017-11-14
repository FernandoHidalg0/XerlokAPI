import requests
from requests.exceptions import ConnectionError


class XerlokText(object):
    SENTIMENT_URL = "http://159.203.78.247:5678/"

    def __init__(self, api):
        self.api = api
        self.headers = {"Authorization": str(self.api)}

    def get_sentiment(self, sentence):
        try:
            url = XerlokText.SENTIMENT_URL + "sentiment/" + sentence
            r = requests.get(url, headers=self.headers)
        except ConnectionError:
            raise ConnectionError("The Sentiment Analysis service is "
                                  "unavailable.")

        try:
            return r.json()
        except:
            return r.text

    def get_disambiguation(self, word):
        try:
            url = XerlokText.SENTIMENT_URL + "disambiguation/" + word
            r = requests.get(url, headers=self.headers)
        except requests.exceptions.ConnectionError:
            raise ConnectionError("The Disambiguation service is "
                                  "unavailable.")

        try:
            return r.json()
        except:
            return r.text
