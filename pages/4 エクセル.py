import streamlit as st
import pandas as pd
import subprocess
import openpyxl

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
