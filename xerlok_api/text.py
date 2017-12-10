import requests
from requests.exceptions import ConnectionError


class XerlokText(object):
    SENTIMENT_URL = "http://159.203.78.247:"
    ES_PORT = "7711"
    PT_PORT = "7712"
    IT_PORT = "7713"
    FR_PORT = "7714"
    EN_PORT = "7715"
    DE_PORT = "7716"

    def __init__(self, api, lang="en-us"):
        self.api = api
        self.headers = {"Authorization": str(self.api)}
        lang = lang.lower()
        if "en" in lang:
            self.port = XerlokText.EN_PORT
        elif "es" in lang:
            self.port = XerlokText.ES_PORT
        elif "pt" in lang:
            self.port = XerlokText.PT_PORT
        elif "it" in lang:
            self.port = XerlokText.IT_PORT
        elif "fr" in lang:
            self.port = XerlokText.FR_PORT
        elif "de" in lang:
            self.port = XerlokText.DE_PORT
        else:
            print "invalid language", lang
            raise

    def get_sentiment(self, sentence):
        try:
            url = XerlokText.SENTIMENT_URL + self.port + "/sentiment/" + \
                  sentence
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
            url = XerlokText.SENTIMENT_URL + self.port + "/disambiguation/" + word
            r = requests.get(url, headers=self.headers)
        except requests.exceptions.ConnectionError:
            raise ConnectionError("The Disambiguation service is "
                                  "unavailable.")

        try:
            return r.json()
        except:
            return r.text
