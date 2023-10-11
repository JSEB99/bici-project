from fastapi import FastAPI, Path
from sklearn.ensemble import RandomForestRegressor
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pydantic import BaseModel
from typing import Annotated
from pickle import load

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # Puedes ajustar esto según tus necesidades (GET, POST, etc.)
    allow_headers=["*"],  # Puedes ajustar esto según tus necesidades
)

estaciones = {34: 'Parque Centenario',4: 'Billinghurst',6: 'Constitución',15: 'Godoy Cruz y Libertador',5: 'Carlos Gardel',
              11: 'Facultad de Medicina',20: 'INSTITUTO LELOIR',3: 'Acuña de Figueroa',44: 'RETIRO II',10: 'FACULTAD DE DERECHO',
              19: 'Humahuaca',49: 'YATAY',13: 'Fitz Roy & Gorriti',0: 'ARAOZ',48: 'Velasco',
              40: 'Plaza Italia',2: 'Acevedo',14: 'General Urquiza',36: 'Peña',16: 'Guatemala',
              29: 'PLAZA BOLIVIA',41: 'Plaza Palermo Viejo',32: 'PUEYRREDÓN',35: 'Pasteur',23: 'MARCELO T. DE ALVEAR',
              33: 'Paraná',24: 'MINISTERIO DE EDUCACION',39: 'Plaza Irlanda',1: 'AUSTRIA Y FRENCH',8: 'ESTADOS UNIDOS Y BOEDO',
              21: 'Julián Álvarez',47: 'VIRREY CEVALLOS',18: 'HOSPITAL ITALIANO',37: 'Plaza Alemania',17: 'HOSPITAL ALEMÁN',
              30: 'PLAZA MONSEÑOR MIGUEL DE ANDREA',31: 'PRIMERA JUNTA',26: 'ONCE II',25: 'Malabia',9: 'F.J.Santamaria de Oro',
              7: 'Coronel Diaz',28: 'PLAZA ALBERTI',45: 'RODRIGO BUENO',42: 'Plaza Primero de Mayo',27: 'PARQUE DEL BAJO',
              46: 'San Jose de Flores',43: 'Plaza Vicente Lopez',38: 'Plaza Bruno Giordano',12: 'Federico Lacroze',22: 'MACACHA GUEMES'}

class Ecobici(BaseModel):
    mes_origen:Annotated[int, Path(title='Mes',description="Meses del año (númericos)",ge=1,le=12)]
    dia_semana_origen:Annotated[int, Path(title='Día de la semana',description="Dia de la semana lunes=0,...,domingo=6",ge=0,le=6)]
    quincena:Annotated[int, Path(title="Primer o Seguna Quincena",description="Primer quincena=1,Segunda=2", ge=1,le=2)]
    bici_model:Annotated[int, Path(title="Modelo de bicicleta",description="Fit=2,ICONIC=1", ge=1,le=2)]
    categoria_edad:Annotated[int, Path(title="Categoría de edad",description="<15=1,<20=2,<40=3,<56=4,<70=5",ge=1,le=5)]
    cat_tiempo_recorrido:Annotated[int, Path(title="Categoría de tiempo recorrido,minutos",description="<30=1,<60=2,<180=3,<300=4,<720=5",ge=1,le=5)]
    cat_hora_origen:Annotated[int, Path(title="Categoría hora",description="(1,2,3,4,5,6)=1;(7,8,9,10)=2;(11,12,13)=3;(14,15)=4;(16,17)=5;(18,19)=6;(20,21,22,23,0)=7",ge=1,le=7)]
    codigo_estacion_nombre:Annotated[int, Path(title="Código de la estación",description="de 1 a 50",ge=0,le=49)]

@app.post("/predict/")
async def predecir(ecobici: Ecobici):
    with open("./model/rs_random_forest_model_1.pkl","rb") as file:
        modelo = load(file)
    data = {
    'mes origen': ecobici.mes_origen,
    'día semana origen': ecobici.dia_semana_origen,
    'QUINCENA': ecobici.quincena,
    'BICI_MODEL': ecobici.bici_model,
    'CATEGORIA_EDAD': ecobici.categoria_edad,
    'CAT_TIEMPO_RECORRIDO': ecobici.cat_tiempo_recorrido,
    'CAT_HORA_ORIGEN': ecobici.cat_hora_origen,
    'codigo_estacion_nombre': ecobici.codigo_estacion_nombre
    }

    df = pd.DataFrame([data])

    prediction = round(modelo.predict(df)[0])

    return {"prediction":prediction}
    

    

