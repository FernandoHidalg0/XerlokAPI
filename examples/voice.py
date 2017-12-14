from xerlok_api.voice import XerlokVoice
from os.path import dirname, join
from os import listdir

api_key = "XerGET_A_KEY"

api_key = "XerTLMKRkymqkclEW2Z4nwDdsoTfIFCUqz1_Ujh54Rtx78"

engine = XerlokVoice(api_key)

users_dir = join(dirname(__file__), "voice_samples")
wav = join(users_dir, "primus", "b0484.wav")
# recognize emotion

predictions, scores = engine.recognize_emotion(wav)
print "top 2", predictions
print "scores", scores

genders, scores = engine.recognize_gender(wav)
print "name", "primus"
print "gender", genders[0]
print "scores", scores

wav = join(users_dir, "norgana", "e0100.wav")
genders, scores = engine.recognize_gender(wav)
print "name", "norgana"
print "gender", genders[0]
print "scores", scores

# recognize speakers
result = engine.recognize_speaker(wav)
if "error" in result.keys():
    # {u'error': u'no trained model available'}
    print result["error"]
else:
    print result


# split files into train/test
test_set = []
train_set = []
folders = listdir(users_dir)
for speaker in folders:
    path = join(users_dir, speaker)
    wavs = listdir(path)
    i = len(wavs)/2
    for idx, wav in enumerate(wavs):
        wav_path = join(path, wav)
        if speaker == "unknown" or idx >= i:
            test_set.append((speaker, wav_path))
        else:
            train_set.append((speaker, wav_path))

# train speakers
for speaker, wav in train_set:
    result = engine.train_speaker(speaker, wav)
    if result.get("success", False):
        print "trained", wav