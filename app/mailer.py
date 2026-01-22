import smtplib
from email.mime.text import MIMEText

RECEPTORES = ["admin1@empresa.com", "admin2@empresa.com", "jefe@area.com"]

def enviar_notificacion(datos_consulta):
    mensaje = MIMEText(f"Nueva consulta recibida:\n\n{datos_consulta}")
    mensaje["Subject"] = f"Nueva Consulta: {datos_consulta['tematica']}"
    print(f"Enviando correo a: {RECEPTORES}")