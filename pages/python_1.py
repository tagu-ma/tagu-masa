import streamlit as st

'''
# 田口先生、サッカー強すぎ
# さいこう
# いつも勝ってばかり
'''
#st.text('花火')
#uploaded_files_pptx = st.file_uploader('./data/花火', type='pptx')

#submit_btn_pptx = st.button('pptx処理実行')

#ボタンが押されたら処理を実行する
#if submit_btn_pptx:
#_df_pptx = pd.read_pptx(uploaded_files_pptx)
#_df_pptx

st.file_uploader('./data/花火 a pptx')
st.download_button('./data/花火 a pptx')


code='''

import stream as st

st.title('アプリ')
'''
st.code(code,language='python')
