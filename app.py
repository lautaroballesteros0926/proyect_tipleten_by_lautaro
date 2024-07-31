import pandas as pd 
import plotly.express as px 
import streamlit as st 

vehicles_data=pd.read_csv('vehicles_us.csv')
st.header('Aplicacion web')
st.subheader('Hecha por Lautaro, estudiante de tripleten. ')
hist_button=st.button('Construir Histograma')

if hist_button:
    st.write('Creacion de un histograma')
    fig=px.histogram(vehicles_data,x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)