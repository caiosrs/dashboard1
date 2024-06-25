import streamlit as st
import pandas as pd

st.title('Dashboard Automático')

file = st.file_uploader(
    'Suba seu arquivo aqui!',
    type=['xlsx']
)

if file:
    if file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        df = pd.read_excel(file)
        st.line_chart(df.set_index('Mês'))
        st.bar_chart(df.set_index('Mês'))
    else:
        st.error('Formato de arquivo não suportado.')
else:
    st.warning('Arquivo ainda não localizado!')
