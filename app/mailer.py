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

    mensaje = MIMEMultipart("alternative")
    mensaje["From"] = f"Sistema de Citas <{email_emisor}>"
    mensaje["To"] = ", ".join(RECEPTORES)
    mensaje["Subject"] = f"🔔 Nueva Consulta: {datos_dict.get('tematica')}"

    html = f"""
    <html>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; padding: 20px;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.1); border-top: 5px solid #00d2ff;">
            <div style="background-color: #1a1a1a; padding: 20px; text-align: center;">
                <h1 style="color: #00d2ff; margin: 0; font-size: 24px;">Nueva Consulta Recibida</h1>
                <p style="color: #ffffff; font-size: 14px; margin-top: 5px;">Gestión de Citas - AWS Lightsail</p>
            </div>
            <div style="padding: 30px;">
                <h2 style="color: #333; border-bottom: 1px solid #eee; padding-bottom: 10px;">Información del Solicitante</h2>
                <p><strong>Nombre:</strong> {datos_dict.get('nombres')} {datos_dict.get('apellidos')}</p>
                <p><strong>Correo:</strong> {datos_dict.get('correo')}</p>
                <p><strong>Edad:</strong> {datos_dict.get('edad')} años</p>
                <p><strong>Entidad:</strong> {datos_dict.get('entidad')}</p>
                
                <h2 style="color: #333; border-bottom: 1px solid #eee; padding-bottom: 10px; margin-top: 20px;">Detalles de la Consulta</h2>
                <p><strong>Área:</strong> <span style="background-color: #e0f7fa; padding: 3px 8px; border-radius: 5px; color: #006064;">{datos_dict.get('area')}</span></p>
                <p><strong>Temática:</strong> {datos_dict.get('tematica')}</p>
                <div style="background-color: #f9f9f9; padding: 15px; border-left: 4px solid #00d2ff; margin-top: 10px; font-style: italic; color: #555;">
                    "{datos_dict.get('descripcion')}"
                </div>
            </div>
            <div style="background-color: #f4f7f6; padding: 15px; text-align: center; color: #888; font-size: 12px;">
                Este es un mensaje automático generado por el sistema desplegado por <strong>Louis3f3</strong>.<br>
                © 2026 Sistema de Gestión de Citas.
            </div>
        </div>
    </body>
    </html>
    """
    
    mensaje.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as servidor:
            servidor.starttls() 
            servidor.login(email_emisor, email_password)
            servidor.sendmail(email_emisor, RECEPTORES, mensaje.as_string())
        print("¡LOGRO!: Correo HTML enviado exitosamente.")
    except Exception as e:
        print(f"ERROR CRÍTICO AL ENVIAR CORREO: {e}")