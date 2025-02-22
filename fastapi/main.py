from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel

app= FastAPI(
    title="Mi primer FastAPI",
    description="Alfredo Danel Rolón Salazar",
    version="1.0.1"
)

class modelUsuario(BaseModel):
    id: int
    nombre: str
    edad: int
    correo: str

usuarios=[
    {"id":1, "nombre": "danel", "edad": 21, "correo":"main1@gmail.com"},
    {"id":2, "nombre": "juan", "edad": 20, "correo":"main2@gmail.com"},
    {"id":3, "nombre": "adan", "edad": 22, "correo":"main3@gmail.com"},
    {"id":4, "nombre": "brayan", "edad": 23, "correo":"main4@gmail.com"},
    {"id":5, "nombre": "jose", "edad": 22, "correo":"main5@gmail.com"},
    {"id":6, "nombre": "carlos", "edad": 24, "correo":"main6@gmail.com"},
    ]

@app.get("/", tags=["Inicio"])
def main():
    return {'Hello World from FastAPI':'Danel Rolon Salazar'}

@app.get("/usuarios", response_model= List[modelUsuario], tags=["Operaciones CRUD"])
def ConstultarUsuarios():
    return usuarios

@app.post("/usuario/", response_model=modelUsuario, tags=["Operaciones CRUD"])
def AgregarUsuario(UsuarioNuevo: modelUsuario):
    for usr in usuarios:
        if usr["id"]==UsuarioNuevo.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    
    usuarios.append(UsuarioNuevo)
    return UsuarioNuevo

@app.put("/usuario/{id}", response_model=modelUsuario,tags=["Operaciones CRUD"])
def ActualizarUsuario(id: int, UsuarioActualizar: modelUsuario):
    for usr in usuarios:
        if usr["id"]==id:
            usr["nombre"]=UsuarioActualizar.nombre
            usr["edad"]=UsuarioActualizar.edad
            usr["correo"]=UsuarioActualizar.correo
            return usr
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UsuarioActualizar

@app.delete("/usuario/{id}", tags=["Operaciones CRUD"])
def EliminarUsuario(id: int):
    for usr in usuarios:
        if usr["id"]==id:
            usuarios.remove(usr)
            return {"Usuario Eliminado": usr}
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"Usuario Eliminado": usr}   

