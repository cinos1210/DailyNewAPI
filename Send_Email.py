import smtplib
import ssl


def Send_email(message):
    host = "smtp.gmail.com"
    port = 465
    email = "rafael.gutierrez4666@alumnos.udg.mx"
    passw = "srlssvmbxshpdldi"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, passw)
        server.sendmail(email, email, message)


