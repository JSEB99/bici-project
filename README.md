# Proyecto de Bicicletas de la Ciudad de Buenos Aires

Para este proyecto se procede a analizar los años 2019 a 2023 de todos los recorridos que se tienen.

## ETL (Extract-Transform-Load)

Se limpian los datos mediante Python y se suben a Snowflake para trabajar colaborativamente el archivo de gran tamaño (4 Gb aproximadamente).

## EDA (Exploratory Data Analysis)

Se realiza un análisis de los datos conectando SnowFlake con PowerBI.

## Machine Learning

Se realiza un modelo de machine learning de regresión. En este caso modelo de 'RandomForestRegressor' de la libreria Scikit-learn, Se realiza mediante google colab. Debido al gran tamaño de los datos se realizaron unas agrupaciones de los datos para reducir su cantidad. (registros totales para modelo 380k)

- Se obtuvo un 82% de r2 score
- Mean Absolute Error: 1.59
- Mean Square Error: 7.05

## API

Se crea una API REST con FastAPI, de tal manera poder enviar datos mediante formulario e internamente regrese la respuesta del modelo de machine learning

## Dashboard

Se crea una interfaz que muestra los datos de PowerBI y el formulario para la predicción de los datos.
