import streamlit as st

'''
# 田口先生、サッカー強すぎ
# さいこう
# いつも勝ってばかり
'''
st.text('花火_xls')
uploaded_files_xlsx = st.file_uploader('ファイルアップロード', type='xlsx')

submit_btn_xlsx = st.button('xlsx処理実行')

#ボタンが押されたら処理を実行する
if submit_btn_xlsx:
_df_xlsx = pd.read_excel(uploaded_files_xlsx)
_df_xlsx

code='''
import stream as st

st.title('アプリ')
'''
st.code(code,language='python')
