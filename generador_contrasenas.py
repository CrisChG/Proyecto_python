import random

MINUSCULAS='abcdefghijklmnñopqrstuvwxyz'
MAYUSCULAS=MINUSCULAS.upper()
NUMEROS='1234567890'
CARACTERES_ESPECIALES='!@#$%^&*()_-{[}]/<>'

generar= None
password=None

conjunto=MINUSCULAS+NUMEROS

lista=[]

def generarPasswords(rango,generar,conjunto,tamano,password):
    for _ in range(rango):
        generar = random.sample(conjunto, tamano)
        password = ''.join(generar)
        print (password)

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
        lista.append(input('¿Introduce la nueva contraseña a guardar?: '))
        opcion=input('¿Deseas elegir otra opcion?: ')
    elif opcion=='3':
        print(lista)
        opcion=input('¿Deseas elegir otra opcion?: ')
    elif opcion=='no' or 'No':  
        break
else:
    print('Opcion invalida')
