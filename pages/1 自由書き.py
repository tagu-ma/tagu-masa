import streamlit as st


'''
# 自由スペース
## 自分が好きな文章やファイルなどが、自由に挿入できますよ！
'''
'''
# 
'''

'''
# 田口先生、サッカーうますぎ!!
# いつも勝ってばかり
# すごい、ステキ～
'''
code='''
import stream as st

st.title('アプリ')
'''
st.code(code,language='python')  

## 唐津市の地図
## マップをプロット
'''
import pandas as pd
import numpy as np
# lat/緯度、lon/経度…唐津市(E129°58'13" N33°37'48.72")
# 100行の２列
df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[33.43,130.05],
    columns=['lat','lon']
 )
st.map(df)

# テキストボックスをサイドバーに
st.sidebar.write('あなたについて答えて下さい')
st.sidebar.text_input('名前は？')
st.sidebar.text_input('住所は？')
