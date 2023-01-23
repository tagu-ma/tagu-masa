import streamlit as st
from PIL import Image

# テキスト➀
st.title('田口サイト')
st.caption('これは内容を充実していきます')

# 画像
image=Image.open('./data/000001.jpg')
st.image(image,width=200)

# 動画
video_file=open('.\data\動画.MTS','rb')
video_bvtes=video_file.read()
st.video(video_bvtes)
