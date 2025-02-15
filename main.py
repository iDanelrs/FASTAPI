from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI(
    title="API de Gestión de Tareas",
    description="API para gestionar una lista de tareas (To-Do List)",
    version="1.0.1"
)

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str
    vencimiento: date
    estado: bool 

tareas = [
    {
        "id": 1,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI",
        "vencimiento": "2024-02-14",
        "estado": True
    }
]

@app.get("/", tags=["Inicio"])
def main():
    return {'Hello World from FastAPI': 'API de Gestión de Tareas'}

@app.get("/tareas", tags=["Tareas"])
def obtener_todas_las_tareas():
    return {"tareas": tareas}

@app.get("/tareas/{id}", tags=["Tareas"])
def obtener_tarea_por_id(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return {"tarea": tarea}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.post("/tareas/", tags=["Tareas"])
def crear_tarea(tarea: Tarea):
    for t in tareas:
        if t["id"] == tarea.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    tareas.append(tarea.dict())
    return {"tarea_creada": tarea}

@app.put("/tareas/{id}", tags=["Tareas"])
def actualizar_tarea(id: int, tarea_actualizada: Tarea):
    for tarea in tareas:
        if tarea["id"] == id:
            tarea.update(tarea_actualizada.dict())
            return {"tarea_actualizada": tarea}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/tareas/{id}", tags=["Tareas"])
def eliminar_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            tareas.remove(tarea)
            return {"tarea_eliminada": tarea}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")  