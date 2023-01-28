import streamlit as st
from PIL import Image

# テキスト➀
st.title('田口サイトで～す')
st.caption('もっと内容を充実していきます。ご安心を！')
#'''
# ## もっと内容を充実していきます。
#'''

# 画面分割_1
#left_column,right_column =st.beta_columns(2)
#img1=Image.open('./data/000001.jpg')
#button =st.left_column.image(img1,width=400)

#if button:
#    img2=Image.open('./data/平原小.jpg')
#    st.right_column.image(img2,width=500)

# 画面分割_2
col1, col2= st.columns(2)
with col1:
    # 画像
    '''
    ### かわいいネコ
    '''
    img1=Image.open('./data/000001.jpg')
    st.image(img1,width=200)

with col2:
    #if st.checkbox('押してね!'):
    '''
    ### 田口先生とAI先生・作
    '''
    img2=Image.open('./data/平原小.jpg')
    st.image(img2,width=400)
    #st.image(img2,use_column_width=True)
    
    # プログレスバーの表示
    import time
    #st.write('プログレスバーの表示')
    '60まで、先生の油絵をじっくり見ましょう'
    # 空の要素を用意!
    latest_interation=st.empty()
    bar = st.progress(0)
    for i in range(60):
        latest_interation.text(f'タイム{i+1}')
        bar.progress(i+1)
        time.sleep(1)

        