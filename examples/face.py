from xerlok_api.face import XerlokFace
from os.path import dirname, join

api_key = "XerGET_A_KEY"

engine = XerlokFace(api_key)

# predict emotion
disgust_face = join(dirname(__file__), "disgust.jpg")

# {u'Disgust': 0.15}  - confidence is always 0.15 for now
print "emotion", engine.recognize_emotion(disgust_face)

# predict face
result = engine.recognize_face(disgust_face)
if "error" in result.keys():
    # {u'error': u'no known users available'}
    print result["error"]
else:
    print "person", result["person"]
    print "score", result["score"]
    # if low score you could choose best prediction instead of discarding
    print result["predictions"]

# train a face
arnold = join(dirname(__file__), "arnold.jpg")
result = engine.train_face("arnold", arnold)
if "success" in result.keys():
    print "user trained"
else:
    print "error", result


# predict unknown face
result = engine.recognize_face(disgust_face)
if "error" in result.keys():
    # {u'error': u'no known users available'}
    print result["error"]
else:
    print "person", result["person"]
    print "score", result["score"]
    # if low score you could choose best prediction instead of discarding
    print result["predictions"]


# predict known face
arnold2 = join(dirname(__file__), "arnold2.jpg")
result = engine.recognize_face(arnold2)
if "error" in result.keys():
    # {u'error': u'no known users available'}
    print result["error"]
else:
    print "person", result["person"]
    print "score", result["score"]
