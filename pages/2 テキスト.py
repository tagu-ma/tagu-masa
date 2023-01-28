import streamlit as st


with st.form(key = 'profile_form'):
    st.write('あなたについて答えて下さい')
    # テキストボックスをサイドバーに
    name=st.text_input('名前は？')
    # print(name)
    adress=st.text_input('住所は？')
    
    # セレクトボックス
    # age_category=st.selectbox(
    # ラジオボタン
    age_category=st.radio(  
        '年齢は？',
        ('子ども(18才未満)','大人(18才以上)')
        )
    
    # 複数選択
    hobby=st.multiselect(
        '趣味は？',
        ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理')
        )
    
    # チェックボックス
    mail_subscribe=st.checkbox('メールマガジンを購読する')
    
    # スライダー
    #height=st.slider('身長は？',min_value=110,max_value=210)
    height=st.slider('身長は？',110,180,130)
    '身長:', height # ←ならない？
 
    # 日付
    import datetime
    start_date = st.date_input(
        '開始日',
        datetime.date(2023,1,1))
    
    # カラーピッカー
    color=st.color_picker('テーマカラー','#00f900')
    
    # セレクトボックス
    option =st.selectbox(
        'あなたの好きな数字を教えて下さい',
        list(range(1,11))
    )
    
    # ボタン
    submit_btn=st.form_submit_button('送信')
    cancel_btn=st.form_submit_button('キャンセル')
    # print(f'submit_btn: {submit_btn}')
    # print(f'cancel_btn: {cancel_btn}')
    if submit_btn:
        # ディクショナリ形式で
        st.text(f'ようこそ、{name}さん! {adress}にステキな本を送りました!')
        st.text(f'年齢:{age_category}です。')
        st.text(f'身長は、だいたい{height}Cmです。')
        #st.text(f'趣味:{",".join(hobby)}')
        'あなたの趣味は','と'.join(hobby),'です。'
        'あなたの好きな数字は、',option,'です。'

        # expanderの追加
        expader1 = st.beta_expander('問い合わせ➀')
        expader1.text('問い合わせ➀の回答')
        expader2 = st.beta_expander('問い合わせ➁')
        expader2.text('問い合わせ➁の回答')

        