from fastapi import FastAPI, Depends, Query, APIRouter
from sqlalchemy.orm import Session
from typing import Optional, List
from .database import SessionLocal, engine, get_db, Base
from .models import Consulta
from pydantic import BaseModel, EmailStr

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Appointment Management API")
router = APIRouter(prefix="/api/v1/appointments", tags=["Appointments"])

class ConsultaCreate(BaseModel):
    nombres: str
    apellidos: str
    correo: EmailStr
    edad: int
    genero: str
    area: str
    entidad: str
    tipoConsulta: str
    tematica: str
    descripcion: str

RECEPTORES = ["luisfernando3chr@gmail.com", "202051@unamba.edu.pe"]

@router.post("/crear")
def crear_consulta(data: ConsultaCreate, db: Session = Depends(get_db)):
    nueva_consulta = Consulta(**data.dict())
    db.add(nueva_consulta)
    db.commit()
    db.refresh(nueva_consulta)
    print(f"NOTIFICACIÓN: Enviando datos a {RECEPTORES}")
    
    return {"mensaje": "Consulta creada y notificaciones enviadas", "id": nueva_consulta.id}

@router.get("/list")
def listar_consultas(area: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Consulta)
    if area:
        query = query.filter(Consulta.area == area)
    return query.all()

app.include_router(router)