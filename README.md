# XerlokAI python api

Python wrapper to XerlokAI services

# XerlokFace


    from xerlok_api.face import XerlokFace

    api = "Xer897654678675XXXYYYTEST"
    client = XerlokFace(api)

    sasha = "/home/user/XERLOK_core/image_analisys/Sasha Grey (4).jpg"
    arnold = "/home/user/XERLOK_core/image_analisys/arnold.jpg"
    arnold2 = "/home/user/XERLOK_core/image_analisys/old_arnold.jpg"

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
