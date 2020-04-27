from gtts import gTTS
import os

with open("letter_tuan.txt",encoding="utf-8") as f:
	file=f.read().replace("\n"," ")
	
language="zh-cn"

speech=gTTS(text=str(file),lang=language,slow=False)

speech.save("voice.mp3")

#Play the sound using os.system("start voice.mp3")