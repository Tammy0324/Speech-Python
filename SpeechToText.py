import azure.cognitiveservices.speech as speechsdk
import time

speech_config = speechsdk.SpeechConfig(subscription="b751009eb5f545f8a4d0ce3cab8d7c71", region="eastasia")

audio_config = speechsdk.audio.AudioConfig(filename="file.wav")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

done = False
    
def stop_cb(evt):
    #print('CLOSING on {}'.format(evt))
    speech_recognizer.stop_continuous_recognition()
    global done
    done = True

def cutString(evt):
    evt = str(evt)
    arr = evt.split(', ')
    #print(arr[2])
    text = arr[2]
    #print(text)
    arr2 = text.split('"')
    print(arr2[1])

#speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
speech_recognizer.recognized.connect(lambda evt: cutString(evt))
#speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
#speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
#speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

speech_recognizer.session_stopped.connect(stop_cb)
speech_recognizer.canceled.connect(stop_cb)

speech_recognizer.start_continuous_recognition()
while not done:
    time.sleep(.5)