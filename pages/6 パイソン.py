import streamlit as st
import subprocess

#audio_file = open('./data/AI曲・田口作成.mp3', 'rb')
#audio_bytes = audio_file.read()
#st.audio(audio_bytes, format='audio/ogg')

# ➀ exe1 ファイルの起動
st.title('日にち')
file_exe1 = './data/test1.exe'
btn_exe1 = st.button('ext1処理実行')
#ボタンが押されたら処理を実行する
if btn_exe1:
    subprocess.Popen(['powershell', 'start', file_exe1], shell=True)

# ➁ exe2 ファイルの起動
st.title('名前')
file_exe2 = './data/test2.exe'
btn_exe2 = st.button('exe2処理実行')
#ボタンが押されたら処理を実行する
if btn_exe2:
    subprocess.Popen(['powershell', 'start', file_exe2], shell=True)

# ➂ exe3 ファイルの起動
st.title('ひらばる')
file_exe3 = './data/2d.exe'
btn_exe3 = st.button('2d.exeの処理実行')
#ボタンが押されたら処理を実行する
if btn_exe3:
    subprocess.Popen(['powershell', 'start', file_exe3], shell=True)    
    
# ➃ cat ファイルの起動
st.title('ネコ写真')
file_cat = './data/cat.exe'
btn_cat = st.button('cat処理実行')
#ボタンが押されたら処理を実行する
if btn_exe2:
    subprocess.Popen(['powershell', 'start', file_cat], shell=True)
        
#uploaded_file = st.file_uploader('./data/test1.exe')
#if uploaded_file:
#    subprocess.run([uploaded_file])
#    st.success('File executed!')
#    subprocess.Popen()
#else:
#    st.warning('Please upload a file first')

# ➁ exe2 ファイルの起動
#st.title('名前')
#st.file_uploader('./data/test2.exe')
#btn_exe2 = st.button('exe2処理実行')
#ボタンが押されたら処理を実行する
#if btn_exe2:
#     subprocess.run('./data/test2.exe')


# ➂ cut.exeファイルの起動    
#st.title('猫の写真')
#st.file_uploader('./data/cat.exe')
#btn_cat = st.button('cat処理実行')
#ボタンが押されたら処理を実行する
#if btn_cat:
#     subprocess.run(['./data/cat.exe'])    

