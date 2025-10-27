import streamlit as st
import pandas as pd

df = pd.read_csv('Dados_Artistas.csv')
st.title('DJ Mateus 🎧 - As mais tocadas no Spotify e YouTube')
st.subheader('Bem vindos a rádio do DJ Mateuszão! Aqui você encontra as músicas mais tocadas nas plataformas Spotify e YouTube.')
st.sidebar.image('logo.png')
artistas = st.sidebar.selectbox('Selecione o Artista', df['Artist'].unique())
df_artista = df[df['Artist'] == artistas]

st.subheader(f'Playlist do Artista: {artistas}')
st.write('Aqui estão as músicas mais tocadas:')
for index, row in df_artista.iterrows():
        with st.container():
            st.markdown(f"### 🎵 **{row['Track']}**")
            
            col1, col2 = st.columns(2)
            col1.metric("🎵 Spotify Streams", f"{row['Stream']:,.0f}")
            col2.metric("📺 YouTube Views", f"{row['Views']:,.0f}")
            
            st.video(row['Url_youtube'])
            st.markdown("---")
st.link_button('Ouça no Spotify', url=row['Url_spotify'], type='primary')