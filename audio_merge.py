 # encoding:utf-8
from pydub import AudioSegment

#enPath = "%s%s/%s"%(enDir,file,enfile) #英文文件的路径
#cnPath = "%s%s/%s"%(cnDir,file,enfile.replace("en_w","cn_w"))#中文文件的路径
#targetPath = "%s%s/%s"%(toDir,file,enfile.replace("en_w","all")) #合并文件的路径

file1_name = "./audio/1.mp3"
file2_name = "./audio/2.mp3"
file3_name = "./audio/3.mp3"
#加载MP3文件
song1 = AudioSegment.from_mp3(file1_name)
song2 = AudioSegment.from_mp3(file2_name)
 
#取得两个MP3文件的声音分贝
db1 = song1.dBFS
db2 = song2.dBFS
 
song1 = song1[300:] #从300ms开始截取英文MP3
 
#调整两个MP3的声音大小，防止出现一个声音大一个声音小的情况
dbplus = db1 - db2
if dbplus < 0: # song1的声音更小
    song1+=abs(dbplus)
elif dbplus > 0: #song2的声音更小
    song2+=abs(dbplus)
 
#拼接两个音频文件
song = song1 + song2
 
#导出音频文件
song.export(file3_name, format="mp3") #导出为MP3格式