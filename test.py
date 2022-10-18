import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Configuración de la App:
st.set_page_config(page_title="Ciencia de Datos - SDS", page_icon="📊")

# Bases de datos:


# Temas:
tema = ['Introducción: ¿Qué significan estos conceptos?', 
        '¿Para qué nos sirve la Ciencia de Datos?', 
        '¿Cuáles son las técnicas de la ciencia de datos?',
        '¿Cuál es el proceso de la ciencia de datos?',
        '¿Qué herramientas usa un científico de datos?',
        'Ejercicio 1.',
        'Ejercicio 2.']

procesos = ['Cargar Base de Datos',
            'Análisis Exploratorio de Datos - EDA',
            'Visualización de Datos', 
            'Modelado de Datos', 
            'Conclusiones']

# Textos:
textos = dict()
textos['Introducción: ¿Qué significan estos conceptos?'] = """La **Ciencia de Datos** es el estudio de datos con el fin de extraer información significativa para su análisis. Tiene un enfoque multidisciplinario que combina principios y prácticas del campo de las matemáticas, la estadística, la **Inteligencia Artificial** y la computación para analizar grandes cantidades de datos. Este análisis permite que los científicos de datos planteen y respondan a preguntas como **"qué pasó", "por qué pasó", "qué pasará" y “qué se puede hacer con los resultados"**.  \n  \n La **Inteligencia Artificial** se refiere a sistemas o máquinas que **imitan** la inteligencia humana para realizar tareas, y que mejoran iterativamente a partir de la información que recopilan, los resultados que obtienen y el análisis de los errores que cometen.  \n  \n  Aunque existen concepciones sobre la **Inteligencia Artificial** con imágenes de robots de aspecto humano de alto funcionamiento que se apoderan del mundo, esta no pretende reemplazar a los humanos. Su objetivo es **mejorar significativamente las capacidades y contribuciones humanas**.  \n  \n  En resumen, la **Inteligencia Artificial** se trata sobre el procesamiento y el **análisis de datos aprovechando la memoria y la velocidad de cálculo de las computadoras**. Esto es lo que la convierte en un activo de investigación muy valioso en todas las áreas del conocimiento humano."""
textos['¿Para qué nos sirve la Ciencia de Datos?'] = """La **Ciencia de Datos** se utiliza para estudiar los datos de cuatro maneras principales:  \n  \n  1. **Análisis descriptivo:** El análisis descriptivo examina los datos para obtener información sobre lo que ha ocurrido u ocurre en el entorno de datos. Se caracteriza por las **visualizaciones de datos**, como los gráficos circulares, de barras o líneas, las tablas o las narraciones generadas.  \n  \n  2. **Análisis de diagnóstico:** El análisis de diagnóstico es un examen profundo o detallado de datos para entender por qué ha ocurrido algo. Se caracteriza por técnicas como el análisis detallado, el descubrimiento y la minería de datos o las correlaciones. Se pueden llevar a cabo varias operaciones y transformaciones de datos en un determinado conjunto con el fin de descubrir patrones únicos en cada una de estas técnicas.  \n  \n  3. **Análisis predictivo:** El análisis predictivo utiliza los datos históricos para hacer previsiones precisas sobre los patrones de datos que pueden producirse en el futuro. Se caracteriza por la implementación de algoritmos de **Machine Learning** (Aprendizaje Automático). En cada una de estas técnicas, se entrena a las computadoras para aplicar ingeniería inversa para encontrar las conexiones de causalidad en los datos.  \n  \n  4. **Análisis prescriptivo:** El análisis prescriptivo lleva los datos predictivos al siguiente nivel. No solo predice lo que es probable que ocurra, sino que sugiere una respuesta óptima para ese resultado. Puede analizar las posibles implicaciones de las diferentes alternativas y recomendar el mejor curso de acción. Utiliza el análisis de gráficos, la simulación, el procesamiento de eventos complejos, las redes neuronales y los motores de recomendación del **Machine Learning**."""
textos['¿Cuáles son las técnicas de la ciencia de datos?'] = """La forma habitual de hacer que una computadora haga un trabajo útil es tener un programador humano que escriba las reglas (un programa de computadora) que se deben seguir para convertir los datos de entrada en datos apropiados. En la **Ciencia de Datos**, el **Machine Learning** (o Aprendizaje automático) le da la vuelta a esto: la máquina toma los datos de entrada y las respuestas correspondientes, y descubre cuáles son las reglas que generan esas respuestas.  \n  \n  Un sistema de aprendizaje automático está **entrenado** en lugar de explícitamente programado. El entrenamiento se realiza con muchos ejemplos relevantes para una tarea, y encuentra los patrones en estos ejemplos que eventualmente permite que el sistema proponga reglas para automatizar la tarea.  \n  \n  Las principales técnicas que utilizan los científicos de datos son:  \n  \n  1. **Clasificación:** La clasificación consiste en ordenar los datos en grupos o categorías específicas. Las computadoras se entrenan para identificar y ordenar datos. Los conjuntos de datos conocidos se utilizan para crear algoritmos de decisión para categorizar nuevos datos.  \n  \n  2. **Regresión:** La regresión es el método para encontrar una relación entre una variable dependiente y distintas variables explicativas. Esta conexión se suele modelar en torno a una fórmula matemática, y se representa en forma gráfica con una línea o curva. Cuando se conoce la fórmula matemática, se utiliza la regresión para predecir el valor de la variable dependiente en función de sus variables explicativas.  \n  \n  3. **Clústeres:** El método de clústeres consiste en agrupar datos estrechamente relacionados para buscar patrones y anomalías. El método de clústeres se diferencia del ordenamiento porque los datos no se pueden clasificar con precisión en categorías fijas. De ahí que los datos se agrupen en relaciones más probables. Con los clústeres se pueden descubrir nuevos patrones y relaciones.  \n  \n  Con estos algoritmos, el científico de datos busca encontrar las representaciones útiles sobre los datos que analiza, dentro de un espacio predefinido de posibilidades (definidos por el algoritmo o técnina seleccionada para el estudio). Esta simple idea permite resolver un problema notablemente amplio.  \n  \n  Actualmente estamos comenzando a aplicar la **Inteligencia Artificial** a muchos problemas importantes para los que podría resultar transformador, desde diagnósticos médicos hasta los asistentes digitales. La investigación en **IA** ha estado avanzando sorprendentemente rápido en el últimos diez años. La mayoría de los resultados de la investigación sobre **Inteligencia Artificial** aún no se aplican, o al menos no se aplican a toda la gama de problemas que podrían resolver en todas las industrias."""
textos['¿Cuál es el proceso de la ciencia de datos?'] = """Una vez definido el problema, el científico de datos puede resolverlo con el proceso que consiste en obtener, depurar, explorar y modelar datos e interpretar los resultados.  \n  \n  1. **Obtener datos:** Los datos pueden ser preexistentes, recién adquiridos o un repositorio descargable de Internet. Los científicos de datos pueden extraerlos de las bases de datos internas o externas, del software CRM de la empresa, de los registros del servidor web, de las redes sociales o adquirirlos de terceros de confianza.  \n  \n  2. **Depurar datos:** La depuración o limpieza de datos consiste en el proceso de normalizarlos (estandarizarlos) según un formato determinado. Incluye la gestión de los datos que faltan, la corrección de errores en estos y la eliminación de datos atípicos. Algunos ejemplos de la depuración de datos son:  \n>> * Cambiar todos los valores de fecha a un formato estándar común.  \n>> * Corregir las faltas de ortografía o los espacios adicionales.  \n>> * Corregir inexactitudes matemáticas o eliminar comas y puntos de números, definiendo correctamente la notación de decimales, etc.  \n  \n  3. **Explorar datos:** La exploración de datos es un análisis preliminar de estos que se utiliza para planificar otras estrategias para su modelado. Los científicos de datos obtienen una comprensión inicial de los datos mediante estadísticas descriptivas y herramientas de visualización de los mismos. A continuación, exploran los datos para identificar patrones interesantes que se puedan estudiar o utilizar.  \n  \n  4. **Modelar datos:** El software y los algoritmos de machine learning se utilizan para obtener información más profunda, predecir resultados y prescribir el mejor curso de acción. Las técnicas de machine learning, como la asociación, clasificación y agrupación, se aplican al conjunto de datos de entrenamiento. El modelo podría probarse con datos de prueba predeterminados para evaluar la precisión de los resultados. El modelo de datos se puede ajustar muchas veces para mejorar los resultados.  \n  \n  5. **Interpretar los resultados:** Los científicos de datos trabajan junto a los analistas y las empresas para convertir la información de datos en acción. Hacen diagramas, gráficos y tablas para representar tendencias y predicciones. La síntesis de datos ayuda a las partes interesadas a comprender y aplicar con eficacia los resultados."""
textos['¿Qué herramientas usa un científico de datos?'] = """**Lenguajes de Programación:** Dentro del trabajo de la **Ciencia de Datos** relacionado con la construcción de modelos para el análisis de los datos, se destacan dos herramientas: **R y Python**. Se trata de lenguajes de programación relativamente recientes y fáciles de asimilar por personas que se desempeñen en cualquier área, es decir que no son lenguajes diseñados estrictamente para personas con experiencia en programación.  \n  \n> **R:** Considerado el estándar entre los lenguajes de programación estadística. **R** es un entorno de software libre dedicado al cálculo estadístico y los gráficos. **R** es de acceso gratuito y cualquiera puede instalar, utilizar y actualizar. Es un lenguaje de alto rendimiento, que ayuda a manejar grandes paquetes de datos, lo que lo convierte en una gran herramienta para el manejo de Big Data. También es ideal para simulaciones intensas, que consumen muchos recursos.   \n  \n>  **Python:** Es otro lenguaje de programación open source, flexible y sencillo. Un programador trabajando con **Python** debe escribir menos código gracias a sus características “amigables” para principiantes, como la legibilidad del código, una sintaxis simplificada y la facilidad de implementación. Al igual que con R, la programación en Python encuentra acomodo en una gran variedad de industrias y aplicaciones. **Python** está detrás del buscador de Google, así como de YouTube, entre otros. Instituciones como la NASA, IBM y Mozilla también dependen en gran medida de **Python**. Esta herramienta también es de uso gratuito, lo que beneficia a startups, empresas y entidades públicas.   \n  \n  **Herramientas de Visualización de Datos:**    \n  \n>  **Power BI:** es una aplicación de visualización de Microsoft. Puede tomar datos de diversas fuentes, como archivos de texto, bases de datos, hojas de cálculo y muchos servicios de datos en línea, incluidos Facebook y Twitter, y usarlos para generar cuadros de mando llenos de gráficos, tablas, mapas y muchos otros objetos de visualización. Los objetos del tablero son interactivos, lo que significa que puede hacer clic en una serie de datos en un gráfico para seleccionarla y usarla como filtro para los otros objetos en el tablero.    \n  \n>  **Tableau:** es otra opción para crear gráficos interactivos a partir de una combinación de múltiples fuentes de datos. También ofrece una versión de escritorio, una versión web y un servicio en línea para compartir los paneles que cree. Es fácil de usar para personas sin conocimientos técnicos, lo que se mejora a través de muchos tutoriales y videos en línea.   \n  \n  **Herramientas para Desarrollar Proyectos:**    \n  \n>  **Jupyter Notebooks:** Proporcionan un entorno donde puede registrar código, ejecutar código, ver resultados, visualizar datos y ver resultados de los modelos. Estas características lo convierten en una herramienta conveniente para realizar flujos de trabajo de ciencia de datos de extremo a extremo, que se pueden utilizar para la limpieza de datos, el modelado estadístico, la creación y capacitación de modelos de aprendizaje automático, la visualización de datos y muchos otros propósitos.    \n  \n>  **Google Colab:** es un producto de Google Research. Permite a cualquier usuario escribir y ejecutar código arbitrario de Python en el navegador de internet.Colab, también conocido como "Colaboratory", se caracteriza por las siguientes ventajas: No requiere configuración, ofrece acceso a GPUs sin costo adicional, y permite compartir contenido fácilmente."""
textos['Ejercicio 1.'] = """Para este ejercicio utilizamos algunas de las bases de datos disponibles en la página de **Datos Abiertos Bogotá:** https://datosabiertos.bogota.gov.co/"""
textos['Ejercicio 2.'] = """Para este ejercicio utilizamos algunas de las bases de datos disponibles en la página de **Datos Abiertos Bogotá:** https://datosabiertos.bogota.gov.co/"""

# Imágenes:
imagenes = dict()
imagenes['Introducción: ¿Qué significan estos conceptos?'] = 'Images//ai.jpeg'
imagenes['¿Para qué nos sirve la Ciencia de Datos?'] = 'Images//graficas.jpg'
imagenes['¿Cuáles son las técnicas de la ciencia de datos?'] = 'Images//algoritmos'
imagenes['¿Cuál es el proceso de la ciencia de datos?'] = 'Images//proceso.jpeg'
imagenes['¿Qué herramientas usa un científico de datos?'] = 'Images//herramientas.png'
imagenes['Ejercicio 1.'] = 'Images//datos_abiertos.png'
imagenes['Ejercicio 2.'] = 'Images//datos_abiertos.png'

# Fuentes:
fuentes = dict()
fuentes['Introducción: ¿Qué significan estos conceptos?'] = """  \n  \n Fuentes:  \n  https://aws.amazon.com/es/what-is/data-science/  \n  https://www.oracle.com/co/artificial-intelligence/what-is-ai/"""
fuentes['¿Para qué nos sirve la Ciencia de Datos?'] = """\n  \n Fuente: https://aws.amazon.com/es/what-is/data-science/"""
fuentes['¿Cuáles son las técnicas de la ciencia de datos?'] = """  \n  \n  Fuentes:  \n  \n  https://aws.amazon.com/es/what-is/data-science/  \n  \n  Chollet, F. (2021). Deep learning with Python. Simon and Schuster."""
fuentes['¿Cuál es el proceso de la ciencia de datos?'] = """  \n  \n  Fuente: https://aws.amazon.com/es/what-is/data-science/"""
fuentes['¿Qué herramientas usa un científico de datos?'] = """  \n  \n  Fuentes:  \n  \n  https://medium.com/@goodrebels/las-herramientas-de-trabajo-del-cient%C3%ADfico-de-datos-6e16c8c71415  \n  \n  https://geekflare.com/es/data-science-tools/  \n  \n  https://www.ceupe.mx/blog/conoces-jupyter-notebook.html  \n  \n  https://colab.research.google.com/"""
fuentes['Ejercicio 1.'] = """  \n  \n  Fuente de los datos: https://datosabiertos.bogota.gov.co/"""
fuentes['Ejercicio 2.'] = """  \n  \n  Fuente de los datos: https://datosabiertos.bogota.gov.co/"""

# Ejercicios:


# Estructura:
## Sidebar:
sidebar = st.sidebar
sidebar.image('Images//logo_sds.png')
sidebar.header('X Jornada Distrital de Epidemiología y Salud Pública')
tema_seleccionado = sidebar.selectbox('Selecciona un tema', tema)

if 'Ejercicio' in tema_seleccionado:
    proceso = sidebar.selectbox('Selecciona un proceso', procesos)

## Principal:
st.header('X Jornada Distrital de Epidemiología y Salud Pública - Secretaría Distrital de Salud de Bogotá.')
st.title('Introducción a la Ciencia de Datos e Inteligencia Artificial') 
st.subheader(tema_seleccionado)
st.image(imagenes[tema_seleccionado])
st.markdown(textos[tema_seleccionado])

try:
    if proceso:
        st.header('La calidad del aire en Bogotá, su impacto en los indicadores de salud y su pronóstico para el 2023.')
        st.subheader(proceso)
        
except:
    pass

st.markdown(fuentes[tema_seleccionado])
