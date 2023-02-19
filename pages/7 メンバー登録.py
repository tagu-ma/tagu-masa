import streamlit as st

# 名前を保持するリストをキャッシュとして設定
@st.cache(allow_output_mutation=True)
def get_names():
    return []

# Streamlitアプリのタイトルを設定
st.title('ファンクラブメンバー')

# テキスト入力欄を作成し、入力された名前をname_listに追加
name = st.text_input('名前を入力してください')
if st.button('追加'):
    name_list = get_names()
    name_list.append(name)
    st.experimental_set_query_params(names=name_list)

# 名前を取得し、表を表示
name_list = get_names()
st.write('### 入力された名前')
if not name_list:
    st.write('まだ名前はありません')
else:
    for i, name in enumerate(name_list):
        st.write(f'{i+1}. {name}')
        if st.button(f'削除 {name}'):
            name_list.pop(i)
            st.experimental_set_query_params(names=name_list)

# キャッシュをクリア
if st.button('キャッシュをクリア'):
    st.caching.clear_cache()



#with st.form("my_form"):
#    name = st.text_input('名前は？') 
#    st.text_input('住所は？')
#    #st.text_input('性別は？')
#    #st.text_input('電話は？') 
    
#    submitted = st.form_submit_button("登録")
#    cancelled = st.form_submit_button('キャンセル')
    
#    if submitted:
#        st.write("名前: ", name)
#    if cancelled:
#        st.write("キャンセルされました")

# ➀メンバー登録
#file_xlsx = './data/menber.xlsx'
#btn_xlsx = st.button('メンバー登録')
#if btn_xlsx:
#    subprocess.Popen(['powershell', 'start', file_xlsx], shell=True)

# ➁メンバー一覧確認
#btn=st.button('メンバー確認')
#df =pd.read_excel('./data/menber.xlsx')
#if btn:
#    st.dataframe(df)

