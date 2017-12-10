from xerlok_api.text import XerlokText

api_key = "XerGET_A_KEY"

engine = XerlokText(api_key)

# get sentiment
sentence = "i love pizza"
result = engine.get_sentiment(sentence)
print "sentence", result["utterance"]
print "emotion", result["emotion"]
print "sentiment", result["sentiment"]
print "subjectivity", result["subjectivity"]

word = "dog"
result = engine.get_disambiguation(word)
print "\ndisambiguation for word:", word
for meaning in result["disambiguation"]:
    print meaning["definition"]

print "other fields", result.keys()

# other language
engine = XerlokText(api_key, lang="es-es")
print engine.get_sentiment("amo la pizza")

