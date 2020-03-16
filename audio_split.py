 # encoding:utf-8
from pydub import AudioSegment
from pydub.silence import split_on_silence
import random
import sys

name = sys.argv[1]

file_name = name+".mp3"
sound = AudioSegment.from_mp3(file_name)

chunks = split_on_silence(sound,min_silence_len=700,silence_thresh=-70)#silence time:700ms and silence_dBFS<-70dBFS

words = chunks[2:] #first and second are not words.

len1 = len(words)

new = AudioSegment.empty()
silence = AudioSegment.silent(duration=1000)#1000ms silence


order = range(len1)
random.shuffle(order)
print order
comments = ""

for i in order:
    new += words[i]+silence
    comments += str(i)+","

save_name = file_name.split(".")[0]+"-random{0}.".format(random.randrange(0,9))+file_name.split(".")[1]
new.export(save_name, format="mp3",tags={'artist': 'AppLeU0', 'album': file_name, 'comments': comments[:-1]})