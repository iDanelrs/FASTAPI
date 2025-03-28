from pydantic import BaseModel, Field, EmailStr

class modelUsuario(BaseModel):
    name: str = Field(..., min_length=3, max_length=25, description="Nombre del usuario")
    age: int = Field(..., gt=0, ge=18, le=80, description="Edad del usuario")
    mail: str = Field( min_length=3, max_length=250, pattern=r"^[^@]+@[^@]+$",description="Correo del usuario" , default="example@example.com")

class modelAuth(BaseModel):
    Correo:EmailStr
    pswd: str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña minimo 8 caracteres")