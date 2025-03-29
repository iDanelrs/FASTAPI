from fastapi import FastAPI, HTTPException, Depends
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

app= FastAPI(
    title='Mi primer API',
    description='Danel Rolon',
    version='1.0.'
)

#Levantamiento de las tablas definidas en los modelos
Base.metadata.create_all(bind=engine)

#Configuracion de la autenticacion
app.include_router(routerUsuario)
app.include_router(routerAuth)

@app.get('/',tags=['Inicio'])
def main():
    return{'hello FastAPI':'Danel Rolon'}

