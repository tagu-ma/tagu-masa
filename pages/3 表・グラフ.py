import streamlit as st
# データ/csvファイルの読み込み
import pandas as pd

# resource_add_path('E:\平原小・唐津市\R4年・パイソン・Python\⑳アプリ公開\supu_app\data')

df=pd.read_csv('./data/平均気温.csv',index_col='月')
st.subheader('１年間の平均気温')
st.dataframe(df)
# st.table(df)
st.subheader('折れ線グラフ')
st.line_chart(df)
st.subheader('2021年\棒グラフ')
st.bar_chart(df['2021年'])
#st.subheader('2021年/折れ線グラフ')
#st.line_chart(df['2021年'])

# マットプロットリブ
#import matplotlib.pyplot as plt
#fig,ax = plt.subplots()
#ax.plot(df.index,df['2021年'])
#ax.set_title('2021nen matplotlib graph')
#st.pyplot(fig)
