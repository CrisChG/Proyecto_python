"""
Proyecto en Python
Generador de contraseñas y encriptacion de mensajes
Crea contraseñas de manera aleatoria, cifra cadenas de texto
y guardar lo anterior nombrado en listas, el usuario puede
acceder a esta informacion
"""

#bibliotecas
import random

"""
===============Funciones de opciones del menu=================================
"""

def password_generator(num_passwords,conjunto,longitud):
    """
    recibe: num_passwords, conjunto y longitud
    genera multiples strings determinados por el usuario por medio de un 
    ciclo for y lo manda a imprimir por la variable new_password
    """
    for i in range(num_passwords):
        generar = random.sample(conjunto, longitud)
        new_password = ''.join(generar)
        print (new_password)
        
def save_password(usuario,password,saved_passwords):
    """
    recibe: usuario, password y la lista saved_passwords
    agrega una lista anidada a la lista de saved_passwords guardando 
    el usuario y la contraseña
    """
    saved_passwords.append([])
    saved_passwords[-1].append(usuario)
    saved_passwords[-1].append(password)    

def encriptar(mensaje,minusculas2):
    """
    recibe: mensaje y minusculas2
    se crea un string el cual contendra el mensaje solo que se 
    le sustituyen las letras dependiendo su indice por medio de un ciclo for
    devuelve: mensaje_encriptado
    """
    mensaje_encriptado=''
    for i in mensaje: 
        cifrar=minusculas2.find(i) + 3
        modulo=int(cifrar)% len(minusculas2)
        mensaje_encriptado=mensaje_encriptado+str(minusculas2[modulo])
    return mensaje_encriptado
 
def save_messages(mensaje_guardar,mensajes_encriptados):
    """
    recibe: mensaje_guardar y mensajes_encriptados
    añade un texto a la lista de mensajes encriptados
    """
    mensajes_encriptados.append(mensaje_guardar)

def desencriptar(mensaje_encriptado,minusculas2): 
    """
    recibe: mensaje y minusculas2
    se crea un string el cual contedran el mensaje_encriptado solo que se
    le sustituyen las letras dependiendo su indice por medio de un ciclo for
    devuelve: mensaje_desencriptado
    """
    mensaje_desencriptado=''
    for i in mensaje_encriptado:
        descifrar=minusculas2.find(i) - 3
        modulo = int(descifrar)% len(minusculas2)
        mensaje_desencriptado= mensaje_desencriptado+str(minusculas2[modulo])
    return mensaje_desencriptado
    
#Definicion de constantes
MINUSCULAS='abcdefghijklmnñopqrstuvwxyz'
MAYUSCULAS=MINUSCULAS.upper()
NUMEROS='1234567890'
CARACTERES_ESPECIALES='!@#$%^&*()_-{[}]/<>'

#Definicion de listas
mensajes_encriptados=[]
saved_passwords=[]

#Variables normales
generar= None
password=None
minusculas2=MINUSCULAS + ' '
conjunto=MINUSCULAS+NUMEROS

        
opcion=int(input('Si deseas generar una o varias contraseñas selecciona 1!\n'
                'Si deseas guardar tu contraseña selecciona 2!\n'
                'Si deseas recuperar las contrañas guardadas selecciona 3!\n'
                'Si deseas encriptar tu mensaje selecciona 4!\n'
                'Si deseas desencriptar tu mensaje selecciona 5!\n'
                'Si deseas acceder a tus mensajes encriptados selecciona 6!\n'
                'Si deseas terminar el programa selecciona 7!\n'))

while type(option)==int:
    if opcion=='1':
        tamano=int(input('¿Cuantos caracteres quieres que tenga tu contraseña?: '))
        pedir_ma= input('¿Quieres que tu contraseña contenga mayusculas?: ')
        if pedir_ma=='si' or pedir_ma=='Si':
             conjunto=conjunto+MAYUSCULAS
        pedir_ce= input('¿Quieres que tu contraseña contenga caracteres especiales?: ')
        if pedir_ce=='si' or pedir_ce=='Si':
             conjunto=conjunto+CARACTERES_ESPECIALES
        rango=int(input('Cuantas contraseñas deseas generar? :'))
        generarPasswords(rango,generar,conjunto,tamano,password)
        opcion=input('¿Deseas elegir otra opcion?: ')
    elif opcion=='2':
        usuario=input('Usuario,correo electronico o cuenta: ')
        contraseña=input('Contraseña: ')
        save_password(saved_passwords,usuario,contraseña)
        opcion=input('¿Deseas elegir otra opcion?: ')
    elif opcion=='3':
        print(contraseñasGuardadas)
        opcion=input('¿Deseas elegir otra opcion?: ')
    elif opcion=='no' or 'No':  
        break
else:
    print('Opcion invalida')
