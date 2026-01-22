from fastapi import APIRouter, FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Appointment Management API",
    description="API para gestión de citas - Despliegue profesional en AWS",
    version="1.0.0"
)

router = APIRouter(
    prefix="/api/v1/appointments",
    tags=["Appointments"] 
)

class Cita(BaseModel):
    paciente: str
    especialidad: str
    fecha: str
    nota: Optional[str] = None

CITAS_DB = [
    {"id": 1, "paciente": "Luis Fernando", "especialidad": "DevOps", "fecha": "2026-01-25"},
    {"id": 2, "paciente": "Elif", "especialidad": "Gaming", "fecha": "2026-01-26"},
]

@router.get("/")
def home():
    return {
        "status": "online",
        "mensaje": "Bienvenido a la API de Gestión de Citas",
        "docs": "/docs"
    }

@router.get("/list") 
def listar_citas(limit: int = Query(10, description="Número de registros a retornar")):
    return {
        "total": len(CITAS_DB),
        "limit": limit,
        "data": CITAS_DB[:limit]
    }

@router.post("/crear")
def crear_cita(cita: Cita):
    return {
        "mensaje": "Cita recibida correctamente en el servidor AWS",
        "data_recibida": cita
    }

app.include_router(router)