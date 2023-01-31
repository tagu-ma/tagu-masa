import streamlit as st
# データ/csvファイルの読み込み
import pandas as pd

# resource_add_path('E:\平原小・唐津市\R4年・パイソン・Python\⑳アプリ公開\supu_app\data')
# Excelファイルの読込
'''
## １年間の平均気温
'''

# resource_add_path('E:\平原小・唐津市\R4年・パイソン・Python\⑳アプリ公開\supu_app\data')

#df=pd.read_csv('./data/平均気温.csv',index_col='月')
#st.subheader('１年間の平均気温')
#st.dataframe(df)
# st.table(df)
#st.subheader('折れ線グラフ')
#st.line_chart(df)
#st.subheader('2021年\棒グラフ')
#st.bar_chart(df['2021年'])

btn1 = st.button('平均気温')
btn2 = st.button('折れ線グラフ')
btn3 = st.button('棒グラフ')
btn4 = st.button('消去')

#ボタンが押されたら処理を実行する
df=pd.read_csv('./data/平均気温.csv',index_col='月')
if btn1:
    # 一覧表
    st.dataframe(df)
elif btn2:
    # 折れ線グラフ
    st.line_chart(df)
elif btn3:
    # 棒グラフ
    st.bar_chart(df['2021年'])


# マットプロットリブ
#import matplotlib.pyplot as plt
#fig,ax = plt.subplots()
#ax.plot(df.index,df['2021年'])
#ax.set_title('2021nen matplotlib graph')
#st.pyplot(fig)
