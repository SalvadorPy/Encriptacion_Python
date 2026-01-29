
def encriptar(texto):
    print("\r\t\t----Encriptación----\n")
    print("El texto a encriptar es:  " + texto)
    textoFinal = ""
    for letra in texto:
        numero= ord(letra)
        numeroNuevo = numero + 2
        nuevaLetra = chr(numeroNuevo)
        textoFinal += nuevaLetra
    print("El texto ya encriptado es:  " + textoFinal)
    return textoFinal


def desencriptar(texto):
    print("\r\t\t----Desencriptación----\n")
    print("El texto a desencriptar es:  " + texto)
    textoFinal = ""
    for letra in texto:
        numero = ord(letra)
        numeroNuevo = numero - 2
        nuevaLetra = chr(numeroNuevo)
        textoFinal += nuevaLetra


    print("El texto ya desencriptado es:   " + textoFinal)
    return textoFinal

# Encriptar archivo
def encriptarArchivo(ruta):
    archivo = open(ruta, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(ruta, 'w')
    archivo.write(textoEncriptado)
    archivo.close()




# DESencriptar archivo
def desencriptarArchivo(ruta):
    archivo = open(ruta, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(ruta, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()



respuestaEoD = str(input("Ingrese 'E', para encriptar y 'D' para desencriptar:\n"))
if respuestaEoD == 'E':
    rutaArchivo = str(input("Ingresa la ruta del archivo a encriptar:\n"))
    encriptarArchivo(rutaArchivo)

if respuestaEoD == 'D':
    rutaArchivo = str(input("Ingresa la ruta del archivo a desencriptar:\n "))
    desencriptarArchivo(rutaArchivo)



