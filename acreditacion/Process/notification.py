import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
 

def SendMail():
    remitente = 'acreditacionrubricassistemas@gmail.com'
    destinatarios = ['bragean123@gmail.com','bissetgl@gmail.com','mpacompiam@unsa.edu.pe','acahuina05@gmail.com','henrys4hgb@gmail.com']
    destinatarios1 = ['bragean123@gmail.com']
    asunto = '[RPI] Reporte Cierre de Fase'
    cuerpo = 'Informe General de la Fase de Acreditacion'

    FileName = '/home/ubuntu/backend/acreditacion/media/phase_status.pdf'
    pdf_data = open(FileName,'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = ", ".join(destinatarios)

    text = MIMEText(cuerpo)
    msg.attach(text)
    doc = MIMEApplication(pdf_data, _subtype = "pdf")
    msg.attach(doc)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('acreditacionrubricassistemas@gmail.com','Acr3d1t4c10n')
    texto = msg.as_string()
    s.sendmail(remitente, destinatarios, texto)
    s.quit()
    return "succes"