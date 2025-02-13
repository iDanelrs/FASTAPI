from fastapi import FastAPI, HTTPException
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

@app.get("/", tags=["Inicio"])
def main():
    return {'Hello World from FastAPI':'Danel Rolon Salazar'}

@app.get("/usuarios", tags=["Operaciones CRUD"])
def ConstultarUsuarios():
    return ["Usuarios Registrados", usuarios]

@app.post("/usuario/", tags=["Operaciones CRUD"])
def AgregarUsuario(UsuarioNuevo: dict):
    for usr in usuarios:
        if usr["id"]==UsuarioNuevo.get("id"):
            raise HTTPException(status_code=400, detail="El ID ya existe")
    
    usuarios.append(UsuarioNuevo)
    return {"Usuario Agregado": UsuarioNuevo}

@app.put("/usuario/{id}", tags=["Operaciones CRUD"])
def ActualizarUsuario(id: int, UsuarioActualizar: dict):
    for usr in usuarios:
        if usr["id"]==id:
            usr["nombre"]=UsuarioActualizar.get("nombre")
            usr["edad"]=UsuarioActualizar.get("edad")
            return {"Usuario Actualizado": usr}
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"Usuario Actualizado": UsuarioActualizar}

@app.delete("/usuario/{id}", tags=["Operaciones CRUD"])
def EliminarUsuario(id: int):
    for usr in usuarios:
        if usr["id"]==id:
            usuarios.remove(usr)
            return {"Usuario Eliminado": usr}
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"Usuario Eliminado": usr}   

