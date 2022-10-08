import random

#Se definen las variables con caracteres que llevara una contraseña
MINUSCULAS='abcdefghijklmnñopqrstuvwxyz'
MAYUSCULAS=MINUSCULAS.upper()
NUMEROS='1234567890'
CARACTERES_ESPECIALES='!@#$%^&*()_-{[}]/<>'

#variables para generar la contraseña
generar= None
password=None

conjunto=MINUSCULAS+NUMEROS

contraseñasGuardadas=[]

def generarPasswords(rango,generar,conjunto,tamano,password):
    for _ in range(rango):
        generar = random.sample(conjunto, tamano)
        password = ''.join(generar)
        print (password)

#introducir contraseñas a la lista anidada
def guardarContraseñas(contraseñasGuardadas,usuario,contraseña):
    contraseñasGuardadas.append([])
    contraseñasGuardadas[-1].append(usuario)
    contraseñasGuardadas[-1].append(contraseña)    
    
        
        
opcion=input('Si deseas generar una o varias contraseñas selecciona 1 \n'
            'Si deseas guardar tu contraseña generada selecciona 2\n'
            'Si deseas recuperar las contrañas guardadas selecciona 3\n:')
while opcion!='0' or opcion<'4' or opcion == 'no':
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
        guardarContraseñas(contraseñasGuardadas,usuario,contraseña)
        opcion=input('¿Deseas elegir otra opcion?: ')
    elif opcion=='3':
        print(contraseñasGuardadas)
        opcion=input('¿Deseas elegir otra opcion?: ')
    elif opcion=='no' or 'No':  
        break
else:
    print('Opcion invalida')
