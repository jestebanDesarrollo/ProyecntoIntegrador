import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")
# Set the page title and header
st.title("Películas de Cine")

df = pd.read_csv('static/datasets/peliculas.csv')

# Convertir columnas a los tipos adecuados
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['critic_score'] = pd.to_numeric(df['critic_score'], errors='coerce')
df['people_score'] = pd.to_numeric(df['people_score'], errors='coerce')

# Eliminar filas con valores NaN
df.dropna(subset=['year', 'type', 'rating', 'critic_score'], inplace=True)

df['decade'] = df['year'] // 10 * 10
# Crear filtros
decadeU = sorted(df['decade'].dropna().unique())
typeU = sorted(df['type'].dropna().unique())

def filtro_peliculas():
    col1, col2, col3 = st.columns(3)
    with col1:
         selected_decade = st.selectbox("Década", ["Todas"] + list(decadeU))
    with col2:
        selected_type = st.selectbox("Tipo", ["Todos"] + list(typeU))
    with col3:
        min_score = st.slider("Puntuación Crítica Mínima", min_value=0, max_value=100, value=0, step=1)
    
    # Filtrar DataFrame
    df_filtrado = df.copy()
    if selected_decade != "Todas":
        df_filtrado = df_filtrado[df_filtrado['decade'] == int(selected_decade)]
    if selected_type != "Todos":
        df_filtrado = df_filtrado[df_filtrado['type'] == selected_type]
    df_filtrado = df_filtrado[df_filtrado['critic_score'] >= min_score]

    if not df_filtrado.empty:
        # Mostrar tabla de resultados filtrados
        st.dataframe(df_filtrado)

        # Graficar puntuaciones de críticos y audiencia
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df_filtrado['title'],
            y=df_filtrado['critic_score'],
            name='Puntuación de Críticos'
        ))
        fig.add_trace(go.Bar(
            x=df_filtrado['title'],
            y=df_filtrado['people_score'],
            name='Puntuación del Público'
        ))
        fig.update_layout(
            barmode='group',
            title='Puntuaciones de Críticos y Público por Película',
            xaxis_title='Película',
            yaxis_title='Puntuación'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No se encontraron resultados para los filtros seleccionados.")

filtro_peliculas()
