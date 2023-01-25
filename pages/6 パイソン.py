import streamlit as st

# Pythonアプリの読込み
st.title('日にち')
st.file_uploader('./data/test1.exe')
btn_exe1 = st.button('exe1処理実行')
#ボタンが押されたら処理を実行する
if btn_exe1:
     st.file_uploader('./data/test1.exe')

st.title('名前')
st.file_uploader('./data/test2.exe')
btn_exe2 = st.button('exe2処理実行')
#ボタンが押されたら処理を実行する
if btn_exe2:
     st.file_uploader('./data/test2.exe')
     
st.title('猫の写真')
st.file_uploader('./data/cat.exe')
btn_cat = st.button('cat処理実行')
#ボタンが押されたら処理を実行する
if btn_cat:
     st.file_uploader('./data/cat.exe')    