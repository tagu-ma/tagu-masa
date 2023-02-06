import streamlit as st
import pandas as pd
import subprocess

# Excelファイルの読込➀
'''
## L-gate おおすすめサイト
'''

# st.title('L-gate')
btn1 = st.button('タイピング')
df_1 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 0)
btn2 = st.button('プログラミング')
df_2 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 2)
#wb_1=openpyxl.load_workbook('./data/L-gate.xlsx',data_only=True,sheet_name= 2)
btn3 = st.button('学習サイト')
df_3 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 3)
btn4 = st.button('情報モラル')
df_4 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 4)
btn5 = st.button('マウス・タッチ練習')
df_5 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 5)
btn6 = st.button('文科省サイト')
df_6 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 6)
btn7 = st.button('消去')

#ボタンが押されたら処理を実行する
if btn1:
    st.dataframe(df_1)
elif btn2:
    st.dataframe(df_2)
elif btn3:   
    st.dataframe(df_3)
elif btn4:    
    st.dataframe(df_4)
elif btn5:   
    st.dataframe(df_5)
elif btn5:    
    st.dataframe(df_5)
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
#ボタンが押されたら処理を実行する
if btn_pptx:
    subprocess.Popen(['powershell', 'start', file_pptx], shell=True) 
