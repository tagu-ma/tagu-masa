import streamlit as st
from PIL import Image

# テキスト➀
st.title('田口先生ファンクラブサイト')
# st.caption('もっと内容を充実していきますよ！')
'''
## もっと内容を充実していきますよ！
''' 
#画面分割
col1, col2= st.columns(2)
with col1:
    # 画像
    '''
    ## かわいいネコ
    '''
    image=Image.open('./data/000001.jpg')
    st.image(image,width=400)

with col2:
    image=Image.open('./data/平原小.jpg')
    st.image(image,width=400)
    '''
    ## 油絵:田口作
    '''
