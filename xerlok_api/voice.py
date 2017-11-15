import requests
from requests.exceptions import ConnectionError


class XerlokVoice(object):
    GENDER_URL = "http://159.203.78.247:5680/gender_recognition/"
    SPEAKER_URL = "http://159.203.78.247:5679/speaker_recognition/"
    EMOTION_URL = "http://159.203.78.247:5681/emotion_recognition/"

    def __init__(self, api):
        self.api = api
        self.headers = {"Authorization": str(self.api)}

    def recognize_emotion(self, wav_file):
        filepath = wav_file
        with open(filepath) as fh:
            mydata = fh.read()
        try:
            response = requests.put(
                XerlokVoice.EMOTION_URL + "recognize",
                data=mydata,
                headers=self.headers
            )
        except ConnectionError:
            raise ConnectionError("The Emotion Analysis service is "
                                  "unavailable.")
        try:
            return response.json()
        except:
            return response.text

    def recognize_gender(self, wav_file):
        filepath = wav_file
        with open(filepath) as fh:
            mydata = fh.read()
        try:
            response = requests.put(
                XerlokVoice.GENDER_URL + "recognize",
                data=mydata,
                headers=self.headers
            )
        except ConnectionError:
            raise ConnectionError("The Gender Analysis service is "
                                  "unavailable.")
        try:
            return response.json()
        except:
            return response.text

    def recognize_speaker(self, wav_file):
        filepath = wav_file
        with open(filepath) as fh:
            mydata = fh.read()
        try:
            response = requests.put(
                XerlokVoice.SPEAKER_URL + "recognize",
                data=mydata,
                headers=self.headers
            )
        except ConnectionError:
            raise ConnectionError("The Speaker Recognition service is "
                                  "unavailable.")

        try:
            return response.json()
        except:
            return response.text

    def train_speaker(self, user, wav_file):
        filepath = wav_file
        with open(filepath) as fh:
            mydata = fh.read()
        try:
            response = requests.put(
                XerlokVoice.SPEAKER_URL + "train/" + user,
                data=mydata,
                headers=self.headers
            )
        except ConnectionError:
            raise ConnectionError("The Speaker Recognition service is "
                                  "unavailable.")
        try:
            return response.json()
        except:
            return response.text