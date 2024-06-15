import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Restaurante")

# Especificar la ruta del archivo CSV
file_path = 'static/datasets/Restaurante.csv'

# Intentar leer el archivo CSV con diferentes encodings
try:
    df = pd.read_csv(file_path, encoding='utf-8', sep=';')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='latin1', sep=';')

df.columns = df.columns.str.strip()

if 'Fecha' in df.columns:
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y', errors='coerce')

df = df.dropna(subset=['Fecha'])

df['Mes'] = df['Fecha'].dt.to_period('M')
df['Año'] = df['Fecha'].dt.to_period('Y')

productosU = sorted(df['Producto'].unique())
usuariosU = sorted(df['Usuario'].unique()) if 'Usuario' in df.columns else []
mesasU = sorted(df['Mesa'].unique())

optionProducto = st.selectbox('Producto', ['Todos'] + productosU)
optionUsuario = st.selectbox('Usuario', ['Todos'] + usuariosU) if usuariosU else None
optionMesa = st.selectbox('Mesa', ['Todos'] + mesasU)

filtered_data = df
if optionProducto != "Todos":
    filtered_data = filtered_data[filtered_data['Producto'] == optionProducto]
if optionUsuario and optionUsuario != "Todos":
    filtered_data = filtered_data[filtered_data['Usuario'] == optionUsuario]
if optionMesa != "Todos":
    filtered_data = filtered_data[filtered_data['Mesa'] == optionMesa]

ventas_por_producto = filtered_data.groupby('Producto')['Total'].sum().reset_index()
fig_bar = px.bar(ventas_por_producto, x='Total', y='Producto', orientation='h', 
                 title='Total de Ventas por Producto', labels={'Total': 'Ventas'})

st.plotly_chart(fig_bar, use_container_width=True)

optionFecha = st.selectbox('Agrupar por', ['Mes', 'Año'])

if optionFecha == 'Mes':
    ventas_por_fecha = filtered_data.groupby(filtered_data['Mes'].astype(str))['Total'].sum().reset_index()
    ventas_por_fecha.columns = ['Fecha', 'Total']
else:
    ventas_por_fecha = filtered_data.groupby(filtered_data['Año'].astype(str))['Total'].sum().reset_index()
    ventas_por_fecha.columns = ['Fecha', 'Total']

fig_line = px.line(ventas_por_fecha, x='Fecha', y='Total', title='Evolución de Ventas a lo Largo del Tiempo')

if optionMesa != "Todos":
    ventas_por_mesa = filtered_data.groupby('Mesa')['Total'].sum().reset_index()
    fig_pie = px.pie(ventas_por_mesa, values='Total', names='Mesa', title='Ventas por Mesa')

fig_bar_producto = px.bar(ventas_por_producto, x='Total', y='Producto', orientation='h',
                          title='Ventas por Producto', labels={'Total': 'Ventas'})

fig_bar_usuario = None

if optionUsuario and optionUsuario != "Todos":
    ventas_por_usuario = filtered_data.groupby('Usuario')['Total'].sum().reset_index()
    fig_bar_usuario = px.bar(ventas_por_usuario, x='Usuario', y='Total', title='Ventas por Usuario')

st.plotly_chart(fig_line, use_container_width=True)
if fig_bar_usuario is not None:
    st.plotly_chart(fig_bar_usuario, use_container_width=True)
if optionMesa != "Todos":
    st.plotly_chart(fig_pie, use_container_width=True)
st.plotly_chart(fig_bar_producto, use_container_width=True)
