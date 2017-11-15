# XerlokAI python api

Python wrapper to XerlokAI services

    pip install xerlok_api

# XerlokVoice


        from xerlok_api.voice import XerlokVoice

        api = "Xerfrherhrg547457gshNOTREAL"
        client = XerlokVoice(api)


Gender Recognition


        male = "/home/user/voice_analisys/voice_gender/test_data/male/0.wav"
        female = "/home/user/voice_analisys/voice_gender/test_data/female/1.wav"

        print client.recognize_gender(male)[0][0]
        print client.recognize_gender(female)[0][0]

output

        male
        female


Emotion Recognition

        bored = "/home/user/voice_analisys/voice_emotion/test/male/boredom/01.wav"
        angry = "/home/user/voice_analisys/voice_emotion/test/male/angry/03.wav"

        print client.recognize_emotion(bored)[0]
        print client.recognize_emotion(angry)[0]

output

        [u'boredom', u'neutral']
        [u'angry', u'happy']


Speaker Recognition


        from os.path import join, dirname
        from os import listdir

        # train some users
        train = join(dirname(__file__), "users")
        for user in listdir(train):
            folder = join(train, user)
            for wav in listdir(folder):
                wav_path = join(folder, wav)
                print client.train_speaker(user, wav_path)


        # test some users
        test = join(dirname(__file__), "test_users")
        for user in listdir(test):
            folder = join(test, user)
            for wav in listdir(folder):
                wav_path = join(folder, wav)
                # i usually consider everything < -0.15 == unknown
                print user, client.recognize_speaker(wav_path)


output

        {u'success': True}
        {u'success': True}
        {u'success': True}
        {u'success': True}
        {u'success': True}

        ....

        squeaquy {u'squeaquy': -0.12640729187186814}
        squeaquy {u'squeaquy': -0.0790981900828033}
        norgana {u'norgana': -0.03304280852454339}
        norgana {u'norgana': -0.02475794011334732}
        joe {u'joe': -0.006175866552867105}
        joe {u'joe': -0.024581769656383767}
        darr {u'darr': -0.21119228425166967}
        darr {u'darr': -0.04415006639190857}
        caustic {u'caustic': -0.04638510373900819}
        caustic {u'caustic': -0.03891786653429505}
        caustic {u'caustic': -0.06570048514842998}
        mikemol {u'mikemol': -0.037603488675553784}
        mikemol {u'mikemol': -0.03507009118392558}
        peter {u'peter': -0.569725930428256}
        peter {u'peter': -0.4676792220583058}
        jon do {u'jon do': 0.03949657042696746}
        jon do {u'jon do': 0.017270347448979376}
        zormion {u'zormion': -0.3627105809393483}
        zormion {u'zormion': -0.1258990355206519}
        primus {u'primus': -0.04296183037834485}
        primus {u'primus': -0.11054956099655187}
        primus {u'primus': -0.045206148526180476}
        unknown {u'caustic': -0.17651453919429627}
        unknown {u'caustic': -0.24115465388416285}
        unknown {u'mikemol': -0.2241161976179749}
        unknown {u'mikemol': -0.6808782770323537}
        unknown {u'mikemol': -1.1813306124260483}
        unknown {u'caustic': -0.16445464562596535}
        unknown {u'mikemol': -0.7741156293361684}
        unknown {u'caustic': -0.2513589395292375}

# XerlokFace


        from xerlok_api.face import XerlokFace

        api = "Xer89765467_FAKE_XXYYYTEST"
        client = XerlokFace(api)

        sasha = "/home/user/image_analisys/Sasha Grey (4).jpg"
        arnold = "/home/user/image_analisys/arnold.jpg"
        arnold2 = "/home/user/image_analisys/old_arnold.jpg"

        print client.recognize_face(sasha)
        print client.recognize_face(arnold)

        print client.train_face("arnold", arnold)
        print client.recognize_face(arnold)
        print client.recognize_face(arnold2)

        print client.recognize_emotion(arnold)

output

        {u'person': u'sasha', u'face_found_in_image': True, u'recognized': True, u'predictions': {u'sasha': 0.7284347839299168}}
        {u'person': u'unknown', u'face_found_in_image': True, u'recognized': False, u'predictions': {u'sasha': 0.018726233880226317}}
        {u'user': u'arnold', u'success': True}
        {u'person': u'arnold', u'face_found_in_image': True, u'recognized': True, u'predictions': {u'arnold': 1.0}}
        {u'person': u'arnold', u'face_found_in_image': True, u'recognized': True, u'predictions': {u'arnold': 0.6423831403398297}}
        {u'Anger': 0.15}
