# Encriptación de Archivos en Python





### ¿Para que sirve?
Este proyecto es un programa sencillo desarrollado en **Python** que permite **encriptar y desencriptar el contenido de un archivo de texto** a partir de la ruta proporcionada por el usuario.

La encriptación se realiza mediante un **desplazamiento de caracteres (cifrado tipo César)**, sumando o restando 2 al valor ASCII de cada carácter.


### Funcionamiento
- El usuario elige si desea **encriptar (E)** o **desencriptar (D)**.
    
- Introduce la **ruta del archivo de texto**.
    
- El programa:
    
    - Lee el contenido del archivo.
        
    - Aplica la encriptación o desencriptación carácter por carácter.
        
    - Sobrescribe el archivo con el contenido resultante.

### Ejecución del programa

1. Clona el repositorio:
    
``` bash
`git clone https://github.com/SalvadorPy/Encriptacion_Python.git cd Encriptacion_Python`
```

2. Ejecuta el script:
    
``` bash
`python Encriptación.py`
```
--------



## Uso del programa💻 


Al ejecutar el programa, se mostrará el siguiente mensaje:
``` bash
`Ingrese 'E', para encriptar y 'D' para desencriptar:`
```
###  Encriptar un archivo
- Ingresa `E`
- Introduce la **ruta del archivo de texto**

Ejemplo:
```
`Ingrese 'E', para encriptar y 'D' para desencriptar: E
Ingresa la ruta del archivo a encriptar: /home/usuario/archivo.txt`
```
El contenido del archivo será encriptado y sobrescrito.

---

### Desencriptar un archivo

- Ingresa `D`
- Introduce la ruta del archivo previamente encriptado
``` bash
`Ingrese 'E', para encriptar y 'D' para desencriptar: D

 Ingresa la ruta del archivo a desencriptar: /home/usuario/archivo.txt`
```
El archivo volverá a su contenido original.


###  Tipo de encriptación

El programa utiliza un **desplazamiento ASCII de +2 para encriptar y -2 para desencriptar**.

Ejemplo:
``` text
Texto original: Hola 
Texto encriptado: Jqnc
```

> Este método es educativo y no debe usarse para seguridad real.



## ⚠️ Advertencias

- El archivo original **se sobrescribe**.
- Se recomienda hacer una copia de seguridad antes de ejecutar el programa.
- Funciona correctamente con **archivos de texto**.


###  Posibles mejoras futuras

- Manejo de errores (archivo no encontrado, permisos).
- Soporte para otros ti
pos de archivo.
- Uso de algoritmos de cifrado más seguros (AES, Fernet).
- Interfaz gráfica (GUI).


### Aprendizajes 📌
Proyecto educativo para practicar manejo de archivos y lógica de encriptación en Python.

### 👤Autor 

>Jesús Salvador Sánchez De Santiago. 
	     Programador, entusiasta matemático y aprendiz de por vida...




			Gracias por leer 


