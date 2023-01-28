import streamlit as st
import pandas as pd
import subprocess

# Excelファイルの読込➀
'''
## L-gate おおすすめサイト
'''
# st.title('L-gate')
btn1 = st.button('タイピング')
btn2 = st.button('プログラミング')
btn3 = st.button('学習サイト')
btn4 = st.button('情報モラル')
btn5 = st.button('マウス・タッチ練習')
btn6 = st.button('文科省サイト')

#ボタンが押されたら処理を実行する
if btn1:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 1)
    st.dataframe(df)
elif btn2:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 2)
    st.dataframe(df)
elif btn3:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 3)
    st.dataframe(df)
elif btn4:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 4)
    st.dataframe(df)
elif btn5:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 5)
    st.dataframe(df)
elif btn6:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 6)
    st.dataframe(df)
    #st.table(df)
      
    
# マクロの起動➁
'''
## jamboard/Excelマクロ
'''
file2 = './data/マクロ.xlsm'
btn_xlsm2 = st.button('マクロ処理実行')
#ボタンが押されたら処理を実行する
if btn_xlsm2:
    subprocess.Popen(['powershell', 'start', file2], shell=True)
     
# パワーポイントの起動➂
'''
## 花火
'''
file3 = './data/花火.pptx'
btn_xlsm3 = st.button('pptx処理実行')
#ボタンが押されたら処理を実行する
if btn_xlsm3:
# スライドショーを開始
    subprocess.Popen(['powershell', 'start', file3], shell=True)

