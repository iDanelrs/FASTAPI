from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="Examen 2do Parcial",
    description="Api de Envios",
    version="1.0.1"
)

envios= [
    {
        "CodigoPostal": "12345",
        "Destino": "Mexico",
        "Peso": 5
    },
    {
        "CodigoPostal": "123456",
        "Destino": "Guadalajara",
        "Peso": 6
    },
    {
        "CodigoPostal": "1234567",
        "Destino": "Queretaro",
        "Peso": 7
    },
    {
        "CodigoPostal": "12345678",
        "Destino": "Monterrey",
        "Peso": 8
    },
]


class Envio(BaseModel):
    CodigoPostal: str = Field(...,min_length=5)
    Destino: str = Field(...,min_length=6)
    Peso: int = Field(...,gt=1, mt=500)
    
@app.get("/envios", response_model = List[Envio], tags=["Envios"])
def getEnvios():
    return envios

@app.post("/envios", response_model = List[Envio],tags=["Envios"])
def crearEnvio(envio: Envio):
    envios.append(envio)
    return envios

@app.delete("/envios/{CodigoPostal}", tags=["Envios"])
def eliminarEnvio(CodigoPostal: str):
    for env in envios:
        if env["CodigoPostal"] == CodigoPostal:
            envios.remove(env)
            return env
        else:
            return {"Envio no encontrado"}
