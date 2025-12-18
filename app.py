# Importar librerías

import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # Cargar los datos

st.header('Estadísticas De Automoviles Usados En Venta') # Título de la aplicación

build_histogram = st.checkbox('Construir un histograma') # crear una casilla de verificación

if build_histogram: # si la casilla está marcada
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
  
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir gráfico de dispersión') # crear una casilla de verificación
if build_scatter: # si la casilla está marcada
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
  
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

