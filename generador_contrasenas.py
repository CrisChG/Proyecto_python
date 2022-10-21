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

#Entrada de dato que determina a que funcion se va a llamar        
opcion=int(input('Si deseas generar una o varias contraseñas selecciona 1!\n'
                'Si deseas guardar tu contraseña selecciona 2!\n'
                'Si deseas recuperar las contrañas guardadas selecciona 3!\n'
                'Si deseas encriptar tu mensaje selecciona 4!\n'
                'Si deseas desencriptar tu mensaje selecciona 5!\n'
                'Si deseas acceder a tus mensajes encriptados selecciona 6!\n'
                'Si deseas terminar el programa selecciona 7!\n'))

while opcion!=0:
    if opcion==1:
        #datos solicitados
        longitud=int(input('¿Cuantos caracteres quieres que tenga tu contraseña?: '))
        pedir_ma=int(input('Si quieres que tu contraseña contenga mayusculas selecciona 1\n'
                           'En el caso que no quieras selecciona 0: \n'))
        if pedir_ma==1:
             conjunto=conjunto+MAYUSCULAS
        pedir_ce=int(input('Si quieres que tu contraseña contenga caracteres especiales selecciona 1\n'
                           'En el caso que no quieras selecciona 0: \n'))
        if pedir_ce==1:
             conjunto=conjunto+CARACTERES_ESPECIALES
        num_passwords=int(input('¿Cuantas contraseñas deseas generar? :'))
        password_generator(num_passwords,conjunto,longitud)
        
    elif opcion==2:
        #datos solicitados
        usuario=input('Usuario,correo electronico o cuenta: ')
        password=input('Contraseña: ')
        save_password(usuario,password,saved_passwords)
        print('Tu contraseña fue guardada exitosamente')
        
    elif opcion==3:
        if len(saved_passwords)==0:
            print('Aun no has guardado ninguna contraseña')
        else:
            print(saved_passwords)
        
    elif opcion==4:
        #datos solicitados
        mensaje = input('Escribe tu mensaje que quieres encriptar: ')
        mensaje=mensaje.lower()
        mensaje_guardar=encriptar(mensaje,minusculas2)
        print(mensaje_guardar)
        guardar_opcion=int(input('Si deseas guardar tu mensaje encriptado preciona 1 \n'
                                 'En el caso de que no quieras guardar el mensaje preciona 2 \n'))
        if guardar_opcion == 1:
            save_messages(mensaje_guardar,mensajes_encriptados)
            print('Tu texto encriptado ha sido guardado con exito')
        else:
            print("Tu mensaje no fue guardado")
        
    elif opcion==5:
        #datos solicitados
        mensaje_encriptado=str(input('Escribe el texto a desencriptar: '))
        print(desencriptar(mensaje_encriptado,minusculas2))
        
    elif opcion==6:
        #datos solicitados
        if len(mensajes_encriptados)==0:
            print('Aun no has guardado ningun mensaje encriptado')
        else:    
            print(mensajes_encriptados)
        
    elif opcion==7:
        #se rompe el ciclo while
        break
    elif opcion>7:
        print('Opcion no valida')
    opcion=int(input('Si deseas generar una o varias contraseñas selecciona 1!\n'
                'Si deseas guardar tu contraseña selecciona 2!\n'
                'Si deseas recuperar las contrañas guardadas selecciona 3!\n'
                'Si deseas encriptar tu mensaje selecciona 4!\n'
                'Si deseas desencriptar tu mensaje selecciona 5!\n'
                'Si deseas acceder a tus mensajes encriptados selecciona 6!\n'
                'Si deseas terminar el programa selecciona 7!\n'))
