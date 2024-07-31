# Proyect_Tipleten_by_Lautaro
# link de la aplicacion web 
https://proyect-tipleten-by-lautaro.onrender.com
# ¿Qué ofrece este proyecto?
Este proyecto No es un analisis profundo de los datos en cuestión ya que cuenta con otros objetivo que comentare mas adelante. Se realizaron algunos gráficos y se exploraron las herramientas que ofrece Streamlit, que era uno de los objetivos para este proyecto. Streamlit resultó ser fácil de usar y se integra bien con bibliotecas para la creación de gráficos como Plotly.

# Dificultades
El verdadero reto del proyecto surgió con la creación del entorno virtual, lo que me hizo repasar y afianzar conocimientos sobre este tema. Comprendí la importancia del archivo requirements.txt. Al trabajar en Linux, crear el entorno virtual desde la terminal es sencillo, pero cuando se usa VS Code, es crucial asegurarse de que el entorno virtual esté configurado correctamente para todo el proyecto. Además, en Jupyter Notebook, el kernel también debe estar vinculado al entorno virtual creado, lo cual, aunque parece simple, puede pasar desapercibido y hacer que pierdas varios minutos solucionando problemas, como la falta de lectura de las librerías especificadas en el requirements.txt.

En cuanto al archivo app.py, no tuve muchos problemas para crear la aplicación, ya que decidí no profundizar demasiado en el análisis de datos y me enfoqué más en desplegar la aplicación y verificar su funcionamiento.

# Despliegue
El despliegue fue un desafío que me tomó varias horas resolver. El problema surgió porque la aplicación no se desplegaba correctamente. Descubrí que la versión de Python en mi entorno virtual era 3.8.19, mientras que en Render se estaba utilizando la versión 3.11.19. Al principio pensé que era un problema con el archivo requirements.txt, ya que aparecía un error relacionado con la librería 'numpy'. Pasé aproximadamente una hora probando diferentes versiones de 'numpy' hasta que me di cuenta de la discrepancia en las versiones de Python. Una vez que corregí esto, el problema se resolvió y pude desplegar la aplicación con normalidad.

# Cambios
Como se mencionó en las secciones de dificultades y despliegue, el objetivo principal de este proyecto no era tanto realizar un análisis profundo de los datos, sino montar una aplicación web desde cero. Fue una experiencia muy entretenida. En el futuro, sería interesante hacer un análisis más exhaustivo, añadir más gráficos, texto y otros elementos para enriquecer la aplicación. Estos cambios se pueden considerar como próximos retos.