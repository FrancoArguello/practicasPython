from pydantic import BaseModel
from typing import Optional #sirve para crear opcionales, para no usar  

class User(BaseModel): #BaseModel nos da la capacidad de crear una ideantidad
    id: Optional[str] #le decimos que puede que no le llegue este valor
    username: str
    email: str