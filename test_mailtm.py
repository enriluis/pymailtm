
from pymailtm import MailTm, Account
mail_tm = MailTm()

"""
Para crear una Cuenta de correo en MailTm
account = mail_tm.get_account()

# Imprimir la información generada en la pantalla
print("Username:", account.address)
print("Password:", account.password)
print("ID:", account.id_)


print("Path del archivo de base de datos:", mail_tm.db_file)


# Crear una instancia de la clase Account
account = mail_tm.Account(id, address, password)"""

"""
    Para leer un mensaje de correo en la cuenta almacenada
"""
# Llamar a la función _load_account() para obtener la cuenta almacenada
account = mail_tm._load_account()

# Obtener la lista de mensajes de la cuenta
messages = account.get_messages()

# Obtener la lista de mensajes de la cuenta
messages = account.get_messages()

# Iterar sobre los mensajes e imprimir su información
for message in messages:
    print("De: ", message.from_)
    print("Para: ", message.to)
    print("Asunto: ", message.subject)
    print("Texto: ", message.text)
    print("HTML: ", message.html)
    print("-----")