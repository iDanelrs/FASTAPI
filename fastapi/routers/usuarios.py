from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modelUsuario
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()

#dependencies= [Depends(bearerJWT())]

#endpoint para consultar datos 
@routerUsuario.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    db = Session()
    try:
        consulta= db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500,content={"mensaje":"NO fue posible consultar","Excepcion":str(x)})
    
    finally:
        db.close()
        
@routerUsuario.get('/usuarios/{id}', tags=['Operaciones CRUD'])
def ConsultarUno(id: int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje": "NO fue posible consultar", "Excepcion": str(x)})
    
    finally:
        db.close()

#endpoint para agregar usuarios
@routerUsuario.post('/usuarios/', response_model=modelUsuario, tags=['Operaciones CRUD'])
def AgregarUsuarios(usuarionuevo: modelUsuario):
    db = Session()
    try:
        nuevo_usuario = User(**usuarionuevo.model_dump())
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario) 
        return JSONResponse(status_code=201, content={"mensaje": "Usuario Guardado", "usuario": jsonable_encoder(nuevo_usuario)})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "NO Guardado", "Excepcion": str(e)})

    finally:
        db.close()
        
#endpoint para actualizar usuario
@routerUsuario.put('/usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar_usuario(id: int, usuario_actualizado: modelUsuario):
    db = Session()
    try:
        usuario_db = db.query(User).filter(User.id == id).first()
        if not usuario_db:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        for key, value in usuario_actualizado.model_dump().items():
            setattr(usuario_db, key, value)
        
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario actualizado correctamente", "usuario": jsonable_encoder(usuario_db)})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "No se pudo actualizar el usuario", "Excepcion": str(e)})
    
    finally:
        db.close()

#endpoint para eliminar usuario 
@routerUsuario.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminar_usuario(id: int):
    db = Session()
    try:
        usuario_db = db.query(User).filter(User.id == id).first()
        if not usuario_db:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        db.delete(usuario_db)
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario eliminado correctamente"})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "No se pudo eliminar el usuario", "Excepcion": str(e)})
    
    finally:
        db.close()