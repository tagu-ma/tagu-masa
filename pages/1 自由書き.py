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

# テキストボックスをサイドバーに
st.sidebar.write('あなたについて答えて下さい')
st.sidebar.text_input('名前は？')
st.sidebar.text_input('住所は？')

