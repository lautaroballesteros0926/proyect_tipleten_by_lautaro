import pandas as pd 
import plotly.express as px 
import streamlit as st 

vehicles_data=pd.read_csv('vehicles_us.csv')
st.header('Aplicacion web')
st.subheader('Hecho por Lautaro, estudiante de tripleten. ')
#Mostramos el dataframe
st.text('100 primeras filas de nuestros datos:')
st.dataframe(vehicles_data.head(100)) 

# Histograma 

st.markdown('### Histograma: ')
fig=px.histogram(vehicles_data,x="odometer")
st.plotly_chart(fig, use_container_width=True)

# Grafico de dispersion 
st.markdown('### Grafico de dispersion')
fig=px.scatter(vehicles_data,x='odometer',y='price')
st.plotly_chart(fig,use_container_width=True)

#Casilla de verificacion
st.markdown('### Casilla de verificacion')
pie_charts=st.checkbox('Construir un grafico circular')

if pie_charts: 
    st.write('Grafico circular para los modelos de carros')
    #Contamos la cantidad de modelos 
    df_filtered=vehicles_data['model'].value_counts().reset_index()
    df_filtered.columns=['model','cantidad']
    # por terminos de simplicidad solo mostraremos los 20 primeros modelos 
    df_filtered=df_filtered.head(20)
    # Crear el gráfico de pastel
    fig = px.pie(df_filtered, names='model', values='cantidad', title='Distribución de Modelos de Carros')
    # Mostrar el gráfico de pastel en Streamlit
    st.plotly_chart(fig, use_container_width=True)
