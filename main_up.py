import streamlit as st
from PIL import Image

# テキスト➀
st.title('田口サイトで～す')
st.caption('もっと内容を充実していきます。ご安心を！')

# 画像
image=Image.open('./data/000001.jpg')
st.image(image,width=400)
image=Image.open('./data/平原小.jpg')
st.image(image,width=400)
# 動画
import streamlit as st
video_file=open('.\data\douga.MTS','rb')
video_bvtes=video_file.read()
st.video(video_bvtes)
