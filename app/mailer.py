import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

RECEPTORES = ["luisfernando3chr@gmail.com", "202051@unamba.edu.pe"]

def enviar_notificacion(datos_dict):
    email_emisor = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")

    if not email_emisor or not email_password:
        print("Error: No se configuraron las credenciales.")
        return

    mensaje = MIMEMultipart()
    mensaje["From"] = email_emisor
    mensaje["To"] = ", ".join(RECEPTORES)
    mensaje["Subject"] = f"Nueva Consulta: {datos_dict.get('tematica')}"

    cuerpo = f"""
    Se ha recibido una nueva consulta de: {datos_dict.get('nombres')} {datos_dict.get('apellidos')}
    
    Detalles:
    - Área: {datos_dict.get('area')}
    - Correo: {datos_dict.get('correo')}
    - Descripción: {datos_dict.get('descripcion')}
    """
    mensaje.attach(MIMEText(cuerpo, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as servidor:
            servidor.starttls() 
            servidor.login(email_emisor, email_password)
            servidor.sendmail(email_emisor, RECEPTORES, mensaje.as_string())
        print("¡LOGRO!: Correo enviado exitosamente.")
    except Exception as e:
        print(f"ERROR CRÍTICO AL ENVIAR CORREO: {e}")