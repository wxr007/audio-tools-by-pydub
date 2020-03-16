# audio-tools-by-pydub
基于pydub库对音频进行剪辑操作

## 安装pydub
```bash
pip install pydub
```
或者
```bash
python -m pip install pydub
```
安装完pydub之后，就可以处理wav格式的音频文件。需要更多的格式支持还需要安装ffmpeg。ffmpeg是一个命令行工具，可以用于一些音频格式的转换，比如mp3转wav啊之类的，然后就可以处理其他类型的多媒体文件了。

## 读取音频文件
mp3：
```python
AudioSegment.from_mp3("sound.mp3")
```
其他格式文件：
```python
AudioSegment.from_file("sound.mp4", format="mp4")
```
具体可以参考API手册：[API](https://github.com/jiaaro/pydub/blob/master/API.markdown)

## 音频分词
```python
split_on_silence(sound,min_silence_len=700,silence_thresh=-70)
```
关键要确定好min_silence_len和silence_thresh的值。这里silence_thresh是认定小于-70dBFS以下的为silence，然后需要保持小于-70dBFS超过 700毫秒。这样子分割成一段一段的。
### 参考
这里需要我们用到foobar的一个功能：视图——可视化———音量计
可以观察一段音频的dBFS大小，正常的音量差不多都是在-25dBFS到-10dBFS。这个单位是从-96dBFS到0dBFS的，越靠近0，音量越大。
我们这里取-70dBFS以下的，认为是静音。然后可以用foobar估算每个单词中间的间隙时间，大概是在900ms也就是0.9s。我们还是取小一些 0.7s分割。

生成一个乱序的序列，然后把单词对应进去，然后中间插入空白静音1s。
```python
silence = AudioSegment.silent(duration=1000)
```