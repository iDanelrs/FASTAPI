from fastapi import FastAPI

app= FastAPI(
    title="Mi primer FastAPI",
    description="Alfredo Danel Rolón Salazar",
    version="1.0.1"
)

@app.get("/", tags=["Prueba"])
def main():
    return {'Hello World from FastAPI':'Danel Rolon Salazar'}

@app.get("/promedio", tags=["Promedio"])
def promedio():
    return {'Promedio':(10+8.5+9)/3}