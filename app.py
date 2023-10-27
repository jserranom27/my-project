import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('datasets/vehicles_us.csv') # leer los datos
st.header("Bienvendio a mi app")
hist_button = st.button('Construir histograma') # crear un botón de creacion de histograma
dist_button = st.button('contruir grafico de dispersion')
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
        fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True) 
elif dist_button: # hacer click en este boton
        # escribe el siguente mensaje
        st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de ventas de coches')

        #Crear grafico de dispersion
        fig1 = px.scatter(car_data, x="odometer", y="price")

        #mostrar grafico de dispersion
        st.plotly_chart(fig1, use_container_width=True)

# %%
# 