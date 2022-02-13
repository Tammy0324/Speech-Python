import azure.cognitiveservices.speech as speechsdk
import requests
from bs4 import BeautifulSoup

speech_config = speechsdk.SpeechConfig(subscription="b751009eb5f545f8a4d0ce3cab8d7c71", region="eastasia")

speech_config.speech_synthesis_language = "en-US"

r=requests.get("https://www.eslfast.com/kidsenglish/ke/ke001.htm")
soup=BeautifulSoup(r.text, "html.parser")
sel=soup.select('div p.read_text font')

string = ""

for s in sel:
  string = s.text
  
print(string)

audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
synthesizer.speak_text_async(string)