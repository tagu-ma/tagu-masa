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
btn7 = st.button('消去')

#ボタンが押されたら処理を実行する
if btn1:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 0)
    st.dataframe(df)
elif btn2:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 1)
    st.dataframe(df)
elif btn3:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 2)
    st.dataframe(df)
elif btn4:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 3)
    st.dataframe(df)
elif btn5:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 4)
    st.dataframe(df)
elif btn6:
    df = pd.read_excel('./data/L-gate.xlsx',sheet_name= 5)
    st.dataframe(df)
    #st.table(df)
      
    
# マクロの起動➁
'''
## jamboard/Excelマクロ
'''
file_xlsm = './data/マクロ.xlsm'
btn_xlsm = st.button('マクロ処理実行')
#ボタンが押されたら処理を実行する
if btn_xlsm:
    subprocess.Popen(['powershell', 'start', file_xlsm], shell=True)

# 花火の起動➁
'''
## PowerPoint/花火
# '''
file_pptx = './data/花火.pptx'
btn_pptx = st.button('pptx処理実行')
# ボタンが押されたら処理を実行する
if btn_pptx:
    subprocess.Popen(['powershell', 'start', file_pptx], shell=True) 
