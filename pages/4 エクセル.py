import streamlit as st
import pandas as pd
# Excelファイルの読込

st.title('L-gate・おすすめサイト一覧')
df = pd.read_excel('./data/L-gate・おすすめサイト一覧.xlsx', sheet_name= 'タイピングサイト')
#st.dataframe(df)
#st.table(df)

# Excelマクロの読込
st.title('マクロExcel・付箋作成・縦配置')
xlsm = st.file_uploader('./data/マクロExcel・付箋作成・縦配置.xlsm')

btn_xlsm = st.button('xlsm処理実行')
#ボタンが押されたら処理を実行する
if btn_xlsm:
     xlsm = pd.read_excel(xlsm)
     xlsm
     
 # PowerPointの読込    
st.title('花火')
pptx = st.file_uploader('./data/花火.pptx')

btn_pptx = st.button('pptx処理実行')
#ボタンが押されたら処理を実行する
if btn_pptx:
     #pptx = pd.read_excel(pptx)
     pptx    
