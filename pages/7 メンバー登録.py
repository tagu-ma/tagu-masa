import streamlit as st

'''
Web⇒Excel保存
'''
with st.form("my_form"):
    name = st.text_input('名前は？') 
    st.text_input('住所は？')
    #st.text_input('性別は？')
    #st.text_input('電話は？') 
    
    submitted = st.form_submit_button("登録")
    cancelled = st.form_submit_button('キャンセル')
    
    if submitted:
        st.write("名前:",name)
    if cancelled:
        st.write("キャンセルされました")

