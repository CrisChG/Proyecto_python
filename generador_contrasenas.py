import random

MINUSCULAS='abcdefghijklmnñopqrstuvwxyz'
MAYUSCULAS=MINUSCULAS.upper()
NUMEROS='1234567890'
CARACTERES_ESPECIALES='!@#$%^&*()_-{[}]/<>'

tamano=int(input('¿Cuantos caracteres quieres que tenga tu contraseña? '))
pedir_ma= input('¿Quieres que tu contraseña contenga mayusculas? ')
pedir_ce= input('¿Quieres que tu contraseña contenga caracteres especiales? ')


conjunto=MINUSCULAS+NUMEROS

if pedir_ma=='si' or pedir_ma=='Si':
    conjunto=conjunto+MAYUSCULAS
if pedir_ce=='si' or pedir_ce=='Si':
    conjunto=conjunto+CARACTERES_ESPECIALES

generar = random.sample(conjunto, tamano)
password = ''.join(generar)
    
print (password)

