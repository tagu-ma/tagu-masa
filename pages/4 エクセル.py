import streamlit as st
import pandas as pd
import subprocess

# Excelファイルの読込➀
'''
## L-gate おおすすめサイト
'''

# ファイルアップロードウィジェットを作成
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # ファイルアップロードウィジェットから読み込んだExcelファイルを読み込む
    wb = openpyxl.load_workbook(uploaded_file, data_only=True)
    st.write("Excel file uploaded and loaded successfully!")
else:
    st.write("Please upload an Excel file.")


df_0 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 0)
btn1 = st.button('プログラミング')
df_1 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 1)
btn2 = st.button('学習サイト')
df_2 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 2)
btn3 = st.button('情報モラル')
df_3 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 3)
btn4 = st.button('マウス・タッチ練習')
df_4 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 4)
btn5 = st.button('文科省サイト')
df_5 = pd.read_excel('./data/L-gate.xlsx',sheet_name= 5)
btn6 = st.button('消去')

#ボタンが押されたら処理を実行する
if btn0:
    #wb=openpyxl.load_workbook('./data/L-gate.xlsx',data_only=True,sheet_name= 0)
    st.dataframe(df_0)
elif btn1:
    st.dataframe(df_1)
elif btn2:   
    st.dataframe(df_2)
elif btn3:    
    st.dataframe(df_3)
elif btn4:   
    st.dataframe(df_4)
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
# ボタンが押されたら処理を実行する
if btn_pptx:
    subprocess.Popen(['powershell', 'start', file_pptx], shell=True) 
