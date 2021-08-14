# Librerias a utilizar

import smtplib


# Mensaje que enviaremos y el asunto


def Msg():
    Mensaje = input("Ingresa el mensaje que deceas mandar: ")
    Subject = input("Ingresa el asunto del mensaje: ")
    Mensaje = "Subject: {}\n\n{}".format(Subject, Mensaje)

    # Esta funcion retorna el mensaje que se enviara al cliente y el Asundo
    return Mensaje

# Recibimos datos del usuario para hacer el login


def DatosGmail():
    correo = input("Ingresa tu correo electronico: --> ")
    password = input("Ingresa tu contraseña: --> ")
    return correo, password
# Iniciamos el servidor y hacemos el login con las credenciales


def Iservidor_Login(correo, password):
    server = smtplib.SMTP("smtp.gmail.com", )

    server.starttls()

    server.login(correo, password)
    return server
# Peticion del correo del usuario al que se le mandara el gmail


def CorreoCliente():
    usuario = input("Ingresa el correo del cliente en el \
        siguiente formato --> "+("(Ejemplo@gmail.com): "))

    return usuario


# Enviamos mensaje y cerramos el servidor
def EnviarMSG(usuario, Mensaje, server, correo):
    server.sendmail(correo, usuario, Mensaje)

    server.quit()


if __name__ == "__main__":
    correo, password = DatosGmail()
    server = Iservidor_Login(correo, password)
    Mensaje = Msg()
    usuario = CorreoCliente()
    EnviarMSG(usuario, Mensaje, server, correo)

print("Correo se envio con exito: ")

# Este Script Fu creado por Juan Daniel
# Luevano Ruiz Puedes usarlo para imple-
# mentar,Correos automaticos.
'''
// Me puedes contactar a --> Mcdany996@gmail.com
'''