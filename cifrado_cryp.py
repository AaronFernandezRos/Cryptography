# Instalar la libreía Cryptography
# pip install cryptography
from cryptography.fernet import Fernet
import os
# 1. Generar una clave secreta
clave = Fernet.generate_key()
cipher = Fernet(clave)

texto = input("\nEscribe un texto que quieras cifrar: ")

#Crea la carpeta si no existe
if not os.path.exists("archivos"):
    os.makedirs("archivos")
    
# 2. Cifrar un mensaje
mensaje = texto.encode()
print("-----------------------------------")
print("Mensaje a Cifrar:", texto)
print("-----------------------------------")

mensaje_cifrado = cipher.encrypt(mensaje)
print("Mensaje Cifrado:", mensaje_cifrado)

#Guardar en archivo texto cifrado(binario)
with open("archivos/cifrado.txt", "wb") as file:
    file.write(mensaje_cifrado)

#Leer mensaje cifrado
with open("archivos/cifrado.txt", "rb") as file:
    mensaje_cifrado_leido = file.read()
print("-----------------------------------")
# 3. Descifrar el mensaje
mensaje_descifrado = cipher.decrypt(mensaje_cifrado_leido).decode()
print("Mensaje Descifrado:", mensaje_descifrado)

#Guardar en archivo texto descifrado
with open("archivos/descifrado.txt", "w") as file:
    file.write(mensaje_descifrado)