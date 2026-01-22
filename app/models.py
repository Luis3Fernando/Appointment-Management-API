from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from .database import Base

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String)
    apellidos = Column(String)
    correo = Column(String)
    edad = Column(Integer)
    genero = Column(String)
    area = Column(String)
    entidad = Column(String)
    tipoConsulta = Column(String)
    tematica = Column(String)
    descripcion = Column(Text)
    fechaCreacion = Column(DateTime, default=datetime.utcnow)