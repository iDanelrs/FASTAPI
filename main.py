from fastapi import FastAPI
from typing import Optional

app= FastAPI(
    title="Mi primer FastAPI",
    description="Alfredo Danel Rolón Salazar",
    version="1.0.1"
)

usuarios=[
    {"id":1, "nombre": "danel", "edad": 21},
    {"id":2, "nombre": "juan", "edad": 20},
    {"id":3, "nombre": "adan", "edad": 22},
    {"id":4, "nombre": "brayan", "edad": 23},
    {"id":5, "nombre": "jose", "edad": 22},
    {"id":6, "nombre": "carlos", "edad": 24},
]

@app.get("/", tags=["Prueba"])
def main():
    return {'Hello World from FastAPI':'Danel Rolon Salazar'}

@app.get("/promedio", tags=["Promedio"])
def promedio():
    return {'Promedio':(10+8.5+9)/3}

@app.get("/usuario/{id}", tags=['Parametro obligatorio'])
def consultaUsuario(id:int):
    return{"Se encontro el usuario": id}

@app.get("/usuariox", tags=["Parametro opcional"])
def consultaUsuario2(id:Optional[int]= None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"]==id:
                return{"mensaje":"Usuario encontrado", "usuario":usuario}
        return{"mensaje":f"No se encontro el id: {id}"}
    else:
        return{"mensaje":"No se proporciono un Id"}
    
#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}