import streamlit as st
# 音楽曲の取込
import numpy as np

'''
# 作曲:ＡＩと田口作成
'''
audio_file = open('./data/AI曲・田口作成.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)

# 動画
'''
# 電子ピアノ演奏
'''
import streamlit as st
video_file=open('./data/動画mp4.mp4','rb')
video_bvtes=video_file.read()
st.video(video_bvtes)





