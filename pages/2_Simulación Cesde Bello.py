import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
# Set the page title and header
st.title("Simulador CESDE Bello")

df = pd.read_csv('static/datasets/cesde.csv')

gruposU = sorted(df['GRUPO'].unique())
nivelesU = sorted(df['NIVEL'].unique())
jornadasU =  sorted(df['JORNADA'].unique())
horarioU =  sorted(df['HORARIO'].unique())
submodulosU =  sorted(df['SUBMODULO'].unique())
docentesU =  sorted(df['DOCENTE'].unique())
momentosU =  sorted(df['MOMENTO'].unique())

# -----------------------------------------------------------------------------------
def filtro1():    
    col1, col2 = st.columns(2)
    with col1:
        grupo = st.selectbox("Grupo",gruposU)
    with col2:
        momento = st.selectbox("Momento",momentosU)
    resultado = df[(df['GRUPO']==grupo)&(df['MOMENTO']==momento)]
   
    resultado= resultado.reset_index(drop=True) 
    # Grafico de barras
    estudiante=resultado['NOMBRE']
    fig = go.Figure(data=[
        go.Bar(name='CONOCIMIENTO', x=estudiante, y=resultado['CONOCIMIENTO']),
        go.Bar(name='DESEMPEÑO', x=estudiante, y=resultado['DESEMPEÑO']),
        go.Bar(name='PRODUCTO', x=estudiante, y=resultado['PRODUCTO'])
    ])   
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    # Tabla
    st.table(resultado[["NOMBRE","CONOCIMIENTO","DESEMPEÑO","PRODUCTO"]])
    
# -----------------------------------------------------------------------------------
def filtro2():
    col1, col2, col3 = st.columns(3)
    with col1:
        grupo = st.selectbox("Grupo",gruposU)
    with col2:
        nombres = df[df['GRUPO']==grupo]
        nombre = st.selectbox("Estudiante",nombres["NOMBRE"])
    with col3:
        momentosU.append("Todos")
        momento = st.selectbox("Momento",momentosU)   

    if momento == "Todos":
        resultado = df[(df['GRUPO']==grupo)&(df['NOMBRE']==nombre)]
        # Grafico de barras
        momentos=sorted(df['MOMENTO'].unique())
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=momentos, y=resultado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=momentos, y=resultado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=momentos, y=resultado['PRODUCTO'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado= resultado.reset_index(drop=True) 
        m1 = resultado.loc[0,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        m2 = resultado.loc[1,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        m3 = resultado.loc[2,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        tm = pd.Series([m1.mean(),m2.mean(),m3.mean()])       
        st.subheader("Promedio")
        st.subheader(round(tm.mean(),1)) 
    else :   
        resultado = df[(df['GRUPO']==grupo)&(df['MOMENTO']==momento)&(df['NOMBRE']==nombre)]
        # Grafico de barras
        estudiante=resultado['NOMBRE']
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=estudiante, y=resultado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=estudiante, y=resultado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=estudiante, y=resultado['PRODUCTO'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado= resultado.reset_index(drop=True) 
        conocimiento = resultado.loc[0,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        st.subheader("Promedio")
        st.subheader(round(conocimiento.mean(),1)) 
<<<<<<< HEAD

 # -----------------------------------------------------------------------------------
def filtro3():
    col1, col2 = st.columns(2)
    with col1:
        submodulo = st.selectbox("Submódulo", submodulosU)
    with col2:
        momento = st.selectbox("Momento", momentosU)
    resultado = df[(df['SUBMODULO'] == submodulo) & (df['MOMENTO'] == momento)]
   
    resultado = resultado.reset_index(drop=True) 
    estudiante = resultado['NOMBRE']
    fig = go.Figure(data=[
        go.Bar(name='CONOCIMIENTO', x=estudiante, y=resultado['CONOCIMIENTO']),
        go.Bar(name='DESEMPEÑO', x=estudiante, y=resultado['DESEMPEÑO']),
        go.Bar(name='PRODUCTO', x=estudiante, y=resultado['PRODUCTO'])
    ])   
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    st.table(resultado[["NOMBRE", "CONOCIMIENTO", "DESEMPEÑO", "PRODUCTO"]])

# -----------------------------------------------------------------------------------
def filtro4():
    col1, col2, col3 = st.columns(3)
    with col1:
        momento = st.selectbox("Momento", momentosU)
    with col2:
        grupo1 = st.selectbox("Grupo 1", gruposU, key='grupo1')
    with col3:
        grupo2 = st.selectbox("Grupo 2", gruposU, key='grupo2')
    
    resultado1 = df[(df['GRUPO'] == grupo1) & (df['MOMENTO'] == momento)]
    resultado2 = df[(df['GRUPO'] == grupo2) & (df['MOMENTO'] == momento)]
   
    resultado1 = resultado1.reset_index(drop=True)
    resultado2 = resultado2.reset_index(drop=True)

    estudiantes1 = resultado1['NOMBRE']
    estudiantes2 = resultado2['NOMBRE']
    
    fig = go.Figure(data=[
        go.Bar(name=f'{grupo1} - CONOCIMIENTO', x=estudiantes1, y=resultado1['CONOCIMIENTO']),
        go.Bar(name=f'{grupo1} - DESEMPEÑO', x=estudiantes1, y=resultado1['DESEMPEÑO']),
        go.Bar(name=f'{grupo1} - PRODUCTO', x=estudiantes1, y=resultado1['PRODUCTO']),
        go.Bar(name=f'{grupo2} - CONOCIMIENTO', x=estudiantes2, y=resultado2['CONOCIMIENTO']),
        go.Bar(name=f'{grupo2} - DESEMPEÑO', x=estudiantes2, y=resultado2['DESEMPEÑO']),
        go.Bar(name=f'{grupo2} - PRODUCTO', x=estudiantes2, y=resultado2['PRODUCTO'])
    ])   
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)

    st.table(resultado1[["NOMBRE", "CONOCIMIENTO", "DESEMPEÑO", "PRODUCTO"]])
    st.table(resultado2[["NOMBRE", "CONOCIMIENTO", "DESEMPEÑO", "PRODUCTO"]])
=======
>>>>>>> 71b03649009678d3c9851bb37149ce8537b4a1c4
  
# -----------------------------------------------------------------------------------
filtros =[
    "Notas por grupo",
<<<<<<< HEAD
    "Notas por estudiante",
    "Notas por submodulo",
    "Comparacion de grupos"
=======
    "Notas por estudiante"
>>>>>>> 71b03649009678d3c9851bb37149ce8537b4a1c4
]

filtro = st.selectbox("Filtros",filtros)

if filtro:
    filtro_index = filtros.index(filtro)

    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()
<<<<<<< HEAD
    elif filtro_index == 2:
        filtro3()
    elif filtro_index == 3:
        filtro4()
=======
>>>>>>> 71b03649009678d3c9851bb37149ce8537b4a1c4
