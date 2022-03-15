import azure.cognitiveservices.speech as speechsdk
import requests
from bs4 import BeautifulSoup
import random

speech_config = speechsdk.SpeechConfig(subscription="b751009eb5f545f8a4d0ce3cab8d7c71", region="eastasia")

speech_config.speech_synthesis_language = "en-US"

audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

url = "https://www.eslfast.com/kidsenglish/ke/ke{}{}{}.htm"

a = random.choice('0')
b = random.choice('1234567890')
c = random.choice('1234567890')

r=requests.get(url.format(a,b,c))
soup=BeautifulSoup(r.text, "html.parser")
sel=soup.select('div p.read_text font')

string = ""
for s in sel:
  string = s.text
sentence = ""
for i in string:
    if (i != '.'):
        sentence +=i
    else:
        print(sentence)
        synthesizer.speak_text_async(sentence)
        sentence = ""
