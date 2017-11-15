import requests
from requests.exceptions import ConnectionError


class XerlokFace(object):
    FACE_URL = "http://159.203.78.247:5666/face_recognition/"
    EMO_FACE_URL = "http://159.203.78.247:5667/face_recognition/emotion/"

    def __init__(self, api):
        self.api = api
        self.headers = {"Authorization": str(self.api)}

    def recognize_emotion(self, jpg_file):
        filepath = jpg_file
        with open(filepath) as fh:
            mydata = fh.read()
        try:
            response = requests.put(
                XerlokFace.EMO_FACE_URL + "recognize",
                data=mydata,
                headers=self.headers
            )
        except ConnectionError:
            raise ConnectionError("The Face Emotion Recognition service is "
                                  "unavailable.")

        try:
            return response.json()
        except:
            return response.text

    def recognize_face(self, jpg_file):
        filepath = jpg_file
        with open(filepath) as fh:
            mydata = fh.read()
        try:
            response = requests.put(
                XerlokFace.FACE_URL + "recognize",
                data=mydata,
                headers=self.headers
            )
        except ConnectionError:
            raise ConnectionError("The Face Recognition service is "
                                  "unavailable.")

        try:
            return response.json()
        except:
            return response.text

    def train_face(self, user, filepath):
        with open(filepath) as fh:
            mydata = fh.read()
        try:
            response = requests.put(
                XerlokFace.FACE_URL + "train/" + user,
                data=mydata,
                headers=self.headers
            )
        except ConnectionError:
            raise ConnectionError("The Face Recognition service is "
                                  "unavailable.")
        try:
            return response.json()
        except:
            return response.text
